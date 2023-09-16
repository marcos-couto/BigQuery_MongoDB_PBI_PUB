provider "aws" {
  region = "Your region" # Change to your desired region
}

resource "aws_lambda_function" "your function name" {
  filename      = "package.zip" # Change to your package name
  function_name = "your function name" # Change to your function name
  role          = "your function name.arn" # Change to your Iam role
  handler       = "your function name.lambda_handler" # Change to your function name
  runtime       = "python3.10" # Change to your Python version
  timeout =  60         # Set the timeout value in seconds (e.g., 30 seconds)

    }

  
    

resource "aws_iam_role" "your function name" {
  name = "your function name"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
  
}