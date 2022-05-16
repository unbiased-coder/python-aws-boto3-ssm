import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
ssm = session.client('ssm')
params = ssm.describe_parameters()
for param in params['Parameters']:
    print (f'Name: {param["Name"]}, Type: {param["Type"]}')
