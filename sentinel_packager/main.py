from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as _lambda_python
# from aws_cdk import aws_s3 as s3

from constructs import Construct


class SentinelPackagerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Lambda that runs
        # when SENTINEL_FILE is present on SENTINEL_BUCKET
        sentinel_file_lambda = _lambda_python.PythonFunction(
            self,
            "SentinelFileLambda",
            entry="path/to/lambda/code",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.handler",
        )
        print(sentinel_file_lambda)
