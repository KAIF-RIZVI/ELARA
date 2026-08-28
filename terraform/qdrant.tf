resource "aws_security_group" "qdrant_sg" {
  name        = "elara-qdrant-sg"
  vpc_id      = aws_vpc.elara_vpc.id
  description = "Allow backend access to Qdrant"

  ingress {
    from_port       = 6333
    to_port         = 6334
    protocol        = "tcp"
    security_groups = [aws_security_group.ecs_sg.id]
  }
}

# The single, deterministic, persistent EBS Volume for Qdrant Data
resource "aws_ebs_volume" "qdrant_data" {
  availability_zone = data.aws_availability_zones.available.names[0]
  size              = 50
  type              = "gp3"
  iops              = 3000
  throughput        = 125
  tags = { Name = "elara-qdrant-data-volume" }
  
  lifecycle {
    prevent_destroy = true
  }
}

# Launch Template for the Single-Node Qdrant EC2 ASG
resource "aws_launch_template" "qdrant_lt" {
  name_prefix   = "elara-qdrant-"
  image_id      = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04 LTS (Update to exact region AMI)
  instance_type = "t3.medium"
  
  iam_instance_profile {
    name = aws_iam_instance_profile.qdrant_profile.name
  }

  vpc_security_group_ids = [aws_security_group.qdrant_sg.id]

  user_data = base64encode(<<-EOF
    #!/bin/bash
    set -e
    # 1. Identity & State Verification
    INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
    AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
    VOLUME_ID="${aws_ebs_volume.qdrant_data.id}"
    
    # 2. Wait for Volume Availability and Attach
    while true; do
      STATE=$(aws ec2 describe-volumes --volume-ids $VOLUME_ID --query 'Volumes[0].State' --output text --region $AZ)
      if [ "$STATE" == "available" ]; then
        aws ec2 attach-volume --volume-id $VOLUME_ID --instance-id $INSTANCE_ID --device /dev/sdf --region $AZ
        break
      elif [ "$STATE" == "in-use" ]; then
        # Force detach from dead node if stuck
        aws ec2 detach-volume --volume-id $VOLUME_ID --force --region $AZ
        sleep 10
      else
        sleep 5
      fi
    done
    
    # Wait for block device to appear
    while [ ! -b /dev/nvme1n1 ] && [ ! -b /dev/xvdf ]; do sleep 1; done
    DEVICE=$(lsblk -nd -o NAME | grep -E 'nvme1n1|xvdf' | awk '{print "/dev/"$1}')
    
    # 3. Mount without Formatting (NEVER MKFS!)
    mkdir -p /qdrant/storage
    mount $DEVICE /qdrant/storage
    chown -R 1000:1000 /qdrant/storage
    
    # 4. Pull TLS certificates from Secrets Manager (Mocked placeholder)
    # aws secretsmanager get-secret-value --secret-id elara/tls_cert --query SecretString --output text > /qdrant/tls/cert.pem
    
    # 5. Start Qdrant Docker Container safely mapped to the volume
    # docker run -d -p 6333:6333 -p 6334:6334 -v /qdrant/storage:/qdrant/storage qdrant/qdrant:v1.9.0
  EOF
  )
}

# Auto Scaling Group enforcing exactly 1 instance running in the EXACT same AZ as the EBS volume
resource "aws_autoscaling_group" "qdrant_asg" {
  name                = "elara-qdrant-asg"
  vpc_zone_identifier = [aws_subnet.private[0].id]
  min_size            = 1
  max_size            = 1
  desired_capacity    = 1
  target_group_arns   = [aws_lb_target_group.qdrant_tg.arn]

  launch_template {
    id      = aws_launch_template.qdrant_lt.id
    version = "$Latest"
  }
}

# Network Load Balancer (NLB) for Stable Private DNS Endpoint (Option B)
resource "aws_lb" "qdrant_nlb" {
  name               = "elara-qdrant-nlb"
  internal           = true
  load_balancer_type = "network"
  subnets            = [aws_subnet.private[0].id]
}

resource "aws_lb_target_group" "qdrant_tg" {
  name     = "elara-qdrant-tg"
  port     = 6333
  protocol = "TCP"
  vpc_id   = aws_vpc.elara_vpc.id

  health_check {
    protocol = "TCP"
    port     = "6333"
  }
}

resource "aws_lb_listener" "qdrant_listener" {
  load_balancer_arn = aws_lb.qdrant_nlb.arn
  port              = "6333"
  protocol          = "TCP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.qdrant_tg.arn
  }
}

# Bind Route 53 to the static NLB DNS name
resource "aws_route53_record" "qdrant_dns" {
  zone_id = aws_route53_zone.internal.zone_id
  name    = "qdrant"
  type    = "A"
  
  alias {
    name                   = aws_lb.qdrant_nlb.dns_name
    zone_id                = aws_lb.qdrant_nlb.zone_id
    evaluate_target_health = true
  }
}
