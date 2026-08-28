resource "aws_secretsmanager_secret" "qdrant_key" {
  name = "elara/production/qdrant_api_key"
}

resource "aws_secretsmanager_secret_version" "qdrant_key" {
  secret_id     = aws_secretsmanager_secret.qdrant_key.id
  secret_string = "CHANGE_ME_MANUALLY_IN_CONSOLE"
}

resource "aws_secretsmanager_secret" "db_password" {
  name = "elara/production/db_password"
}

resource "aws_secretsmanager_secret_version" "db_password" {
  secret_id     = aws_secretsmanager_secret.db_password.id
  secret_string = jsonencode({ password = "CHANGE_ME_MANUALLY_IN_CONSOLE" })
}

data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = aws_secretsmanager_secret.db_password.id
  depends_on = [aws_secretsmanager_secret_version.db_password]
}
