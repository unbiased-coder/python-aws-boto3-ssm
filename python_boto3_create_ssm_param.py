import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
ssm = session.client('ssm')

print('Creating parameter: full_name')
full_name_param = ssm.put_parameter(Name='full_name', Value='Unbiased Coder', Type='String')

print ('Successfully added new parameter: full_name with value: Unbiased Coder')

