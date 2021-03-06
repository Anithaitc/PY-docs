import boto3
import json
from os import path
from src import utils

LAMBDA_ACCESS_POLICY_ARN=''
#here we copy the arn from this console.
LAMBDA_ROLE='Lambda_Execution_Role'
LAMBDA_ROLE_ARN=''
#after execute the create_execution_role_for_lambda(), we get ARN url , copy here.
LAMBDA_TIMEOUT=10
LAMBDA_MEMORY=128
PYTHON_36_RUNTIME='python3.6'
PYTHON_LAMBDA_NAME='PythonLambdaFunction'
LAMBDA_HANDLER='lambda_function.handler'



def lambda_client():
    aws_lambda=boto3.client('lambda',region_name="es-west-1")
    return aws_lambda
def iam_client():
    iam=boto3.client('iam')
    """" :type:pyboto3.iam"""
    return iam
def create_access_policy_for_lambda():
    s3_access_policy_document={
        "version":"2012-10-17",
        "Statement":[
            {
                "Action":[
                    "s3:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Effect":"Allow",
                "Resource":"*"
            }
        ]
    }
    return iam_client().create_policy(
        PolicyName='LambdaS3AccessPolicy',
        PolicyDocument=json.dumps(s3_access_policy_document),
        Description='Allow lambda functions to access S3 resources'
    )
def create_execution_role_for_lambda():
    lambda_execution_assumption_role={
        "Version":"2022-10-17",
        "Statement":[
            {
            "Effect":"Allow",
    "Principal":{
        "Service":"lambda.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
            }
        ]
    }
    return iam_client().create_role(
        RoleName=LAMBDA_ROLE,
        AssumeRolePolicyDocument=json.dumps(lambda_execution_assumption_role),
        Description="Gives necessary permissions for lambda to be executed"
    )
def attach_access_policy_to_execution_role():
    return iam_client().attach_role_policy(
        RoleName=LAMBDA_ROLE,
        PolicyArn=LAMBDA_ACCESS_POLICY_ARN
    )
def deploy_lambda_function(function_name, runtime,handler,role_arn,source_folder):
    folder_path=path.join(path.dirname(path.abspath(__file__)),source_folder)
    #zip_file=Utils.make_zip_file_bytes(path=folder_path)
    return lambda_client().create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={
            'ZipFile':zip_file
        },
        Timeout=LAMBDA_TIMEOUT,
        MemorySize=LAMBDA_MEMORY,
        Publish=False
    )

if __name__== '__main__':
    #print(create_access_policy_for_lambda())
    #print(create_execution_role_for_lambda())
    #print(attach_access_policy_to_execution_role())
    print(deploy_lambda_function(PYTHON_LAMBDA_NAME,PYTHON_36_RUNTIME,LAMBDA_HANDLER,LAMBDA_ROLE_ARN,'python_lambda'))

