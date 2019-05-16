import boto3

# set your region
region = 'us-east-1'

# instances ID: ['EC2 Name1', 'EC2 Name2']
instances = ['i-xxxxx1', 'i-xxxxxx2']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: ' + str(instances))
