from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="ernest@quiltdata.io",
    author_name="Dr. Ernie Prabhakar",
    cdk_version="2.1.0",
    module_name="sentinel_packager",
    name="sentinel-packager",
    version="0.1.0",
)

project.add_dependency("aws-cdk.aws-lambda-python-alpha")
project.add_dev_dependency("black")
project.add_dev_dependency("flake8")
project.add_dev_dependency("isort")
project.add_dev_dependency("mypy")

project.synth()
