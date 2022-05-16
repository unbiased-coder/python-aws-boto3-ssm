import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
ssm = session.client('ssm')

print('Retrieving parameter: name')
name_param = ssm.get_parameter(Name='name')['Parameter']['Value']

print('Retrieving parameter: surname')
surname_param = ssm.get_parameter(Name='surname')['Parameter']['Value']

print (f'Found Name Surname: {name_param} {surname_param}')

print('Retrieving parameter: full_name')
full_name_param = ssm.get_parameter(Name='full_name')['Parameter']['Value']

print (f'Found full_name: {full_name_param}')