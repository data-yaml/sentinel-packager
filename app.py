import os
from aws_cdk import App, Environment
from sentinel_packager.main import SentinelPackagerStack

# for development, use account/region from cdk cli
dev_env = Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    region=os.getenv("CDK_DEFAULT_REGION")
)

app = App()
SentinelPackagerStack(app, "sentinel-packager-dev", env=dev_env)
# SentinelPackagerStack(app, "sentinel-packager-prod", env=prod_env)

app.synth()
