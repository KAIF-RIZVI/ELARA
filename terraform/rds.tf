resource "aws_db_instance" "postgres" {
  identifier           = "elara-production-db"
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t4g.small"
  username             = "postgres"
  password             = jsondecode(data.aws_secretsmanager_secret_version.db_password.secret_string)["password"]
  skip_final_snapshot  = false
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name = aws_db_subnet_group.default.name
}

resource "aws_db_subnet_group" "default" {
  name       = "elara-db-subnet"
  subnet_ids = aws_subnet.private[*].id
}

resource "aws_security_group" "rds_sg" {
  name   = "elara-rds-sg"
  vpc_id = aws_vpc.elara_vpc.id
}
