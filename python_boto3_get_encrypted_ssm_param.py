import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
ssm = session.client('ssm')

print('Retrieving parameter: secure')
secure_param = ssm.get_parameter(Name='secure', WithDecryption=True)['Parameter']['Value']

print (f'Got encrypted value for secure: {secure_param}')
