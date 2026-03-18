provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "devops_bucket" {
    bucket = "jobready-devops-bucket-jinna-1234"
}

resource "aws_ecr_repository" "app_repo" {
    name = "jobready-fastapi"
}