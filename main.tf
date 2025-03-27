provider "aws" {
	region = "us-east-1"
}

data "archive_file" "zip_the_python_code" {
type        = "zip"
source_dir  = "${path.module}/python/"
output_path = "${path.module}/python/hello-python.zip"
}

resource "aws_lambda_function" "live-lights" {
	filename      = "live-lights.zip"
	function_name = "live-lights"
	role          = aws_iam_role.lambda_role.arn
	handler       = "govee.handler"
	runtime = "python3.13"
}

resource "aws_lambda_permission" "this" {
 statement_id  = "AllowAPIGatewayInvoke"
 action        = "lambda:InvokeFunction"
 function_name = aws_lambda_function.this.function_name
 principal     = "apigateway.amazonaws.com"
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
 name              = "/aws/lambda/my_lambda_function"
 retention_in_days = 14
}


resource "aws_iam_policy" "iam_policy_for_lambda" {

 name         = "aws_iam_policy_for_terraform_aws_lambda_role"
 path         = "/"
 description  = "AWS IAM Policy for managing aws lambda role"
 policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": [
       "logs:CreateLogGroup",
       "logs:CreateLogStream",
       "logs:PutLogEvents"
     ],
     "Resource": "arn:aws:logs:*:*:*",
     "Effect": "Allow"
   }
 ]
}
EOF
}
