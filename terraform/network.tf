data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "elara_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = { Name = "elara-production-vpc" }
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.elara_vpc.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  tags = { Name = "elara-private-subnet-${count.index + 1}" }
}

resource "aws_route53_zone" "internal" {
  name = "elara.internal"
  vpc {
    vpc_id = aws_vpc.elara_vpc.id
  }
}
