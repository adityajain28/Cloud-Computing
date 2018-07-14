import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')

# List all instances
def list_instances():
        instances = []
	ec2 = boto3.resource('ec2')
	for instance in ec2.instances.all():
		print("\nInstance ID : ",instance.id, "\nState : ", instance.state,"\nLocation : ", instance.placement['AvailabilityZone'], "\nIP : ", instance.public_ip_address)
                instances.append(instance.id)
        return instances

# Create new instance
def create_instance(security_group_id, keyname = 'MiniAssignment2'):
	ec2 = boto3.resource('ec2')
	instance = ec2.create_instances(ImageId='ami-97785bed', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName= keyname, SecurityGroupIds = [security_group_id])
	print("\nNew Instance Created\nInstance ID : ",instance[0].id)

# Terminate instance
def terminate_instance(instances):
	ec2 = boto3.resource('ec2')
	for instance_id in instances:
		instance = ec2.Instance(instance_id)
		response = instance.terminate()
		print("\nInstance Terminated:\n",response)

def create_keypair():
        ec2 = boto3.resource('ec2')
        outfile = open('MiniAssignment2.pem','w')
        key_pair = ec2.create_key_pair(KeyName='MiniAssignment2')
        KeyPairOut = str(key_pair.key_material)
        outfile.write(KeyPairOut)

def create_security_group():
        
        ec2 = boto3.client('ec2')

        response = ec2.describe_vpcs()
        vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

        try: 
            response = ec2.create_security_group(GroupName='MiniAssignment2',Description='creating a security group programmatically',VpcId=vpc_id)
            security_group_id = response['GroupId']

            data = ec2.authorize_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[
                    {'IpProtocol': 'tcp',
                     'FromPort': 22,
                     'ToPort': 22,
                     'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
                ])
            print('Ingress Successfully Set %s' % data)
            return security_group_id
        except ClientError as e:
            print(e)
            return ['default']


if __name__ == '__main__':
        
        if len(sys.argv) < 2:
                print "Please pass the arguments as for Create Instance:'create_instance' or for List Instance:'list_instances' or for Terminate Instance:'terminate_instances'"
                sys.exit(1)
        elif sys.argv[1] == 'create_instance':
                create_keypair()
                security_group_id = create_security_group()
                create_instance(security_group_id)
        elif sys.argv[1] == 'list_instances':
                instances = list_instances()
        elif sys.argv[1] == 'terminate_instances':
                instances = list_instances()
                terminate_instance(instances)
        else:
                print "Please pass the arguments as for Create Instance:'create_instance' or for List Instance:'list_instances' or for Terminate Instance:'terminate_instances'"
                sys.exit(1)           
