resource "aws_ecs_cluster" "elara_cluster" {
  name = "elara-production-cluster"
}

resource "aws_security_group" "ecs_sg" {
  name        = "elara-ecs-sg"
  vpc_id      = aws_vpc.elara_vpc.id
  description = "ECS Fargate tasks security group"
}

resource "aws_ecs_task_definition" "backend" {
  family                   = "elara-backend"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "1024" # 1 vCPU
  memory                   = "2048" # 2 GB
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn

  container_definitions = jsonencode([{
    name  = "elara-backend"
    image = "elara-backend:latest"
    secrets = [
      { name = "QDRANT_API_KEY", valueFrom = aws_secretsmanager_secret.qdrant_key.arn },
      { name = "POSTGRES_PASSWORD", valueFrom = aws_secretsmanager_secret.db_password.arn }
    ]
    environment = [
      { name = "QDRANT_URL", value = "https://qdrant.elara.internal:6333" },
      { name = "ENVIRONMENT", value = "production" }
    ]
  }])
}

resource "aws_ecs_task_definition" "worker" {
  family                   = "elara-worker"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "2048" # Initial estimate, needs benchmark
  memory                   = "4096" # Initial estimate, needs benchmark
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn

  container_definitions = jsonencode([{
    name  = "elara-worker"
    image = "elara-worker:latest"
    command = ["celery", "-A", "app.worker.celery_app", "worker", "-l", "info"]
    secrets = [
      { name = "QDRANT_API_KEY", valueFrom = aws_secretsmanager_secret.qdrant_key.arn },
      { name = "POSTGRES_PASSWORD", valueFrom = aws_secretsmanager_secret.db_password.arn }
    ]
    environment = [
      { name = "QDRANT_URL", value = "https://qdrant.elara.internal:6333" },
      { name = "ENVIRONMENT", value = "production" }
    ]
  }])
}
