import boto3

## Get vpc_id and subnet_id.
ec2 = boto3.client('ec2')
response_vpc = ec2.describe_vpcs()
vpc_id = response_vpc.get('Vpcs', [{}])[0].get('VpcId', '')
response_subnet = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
subnet_id = response_subnet["Subnets"][0]["SubnetId"]
print("The Default Subnet : ", subnet_id)

## Security group creation with rules.
def create_sg():
    global group_id
    ec2.create_security_group(Description='demo_for_boto3',
        GroupName='boto3_train',
        VpcId=vpc_id,)

    group_name = 'boto3_train'
    response_sg = ec2.describe_security_groups(
        Filters=[
            dict(Name='group-name', Values=[group_name])
        ]
    )
    group_id = response_sg['SecurityGroups'][0]['GroupId']
    print("The boto3_train group_id : ", group_id)


    ec2.authorize_security_group_ingress(
        GroupId=group_id,
        IpPermissions = [
                {'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 443,
                'ToPort': 443,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
            ],

    )

## ec2 instance creation with assign to the security group created earlier.
def create_instance():
    global instance_id
    ec2.run_instances(
                ImageId="ami-##########",
                MinCount=1,
                MaxCount=1,
                InstanceType="t2.micro",
                KeyName="Key_pair_aws", ## Insert your key pair.
                SecurityGroupIds=[group_id],
                SubnetId=subnet_id,
            )

    ## Get instance id regarding Tag.
    response_instance = ec2.describe_instances()
    instances = response_instance["Reservations"]
    instance_id = response_instance["Reservations"][0]["Instances"][0]["InstanceId"]
    print(instance_id)


## Tag the new instance.
def instance_tag():
    tag_creation = ec2.create_tags(
        # DryRun=True,
        Resources=[
            instance_id,
        ],
        Tags=[
            {
                'Key': 'EnvName',
                'Value': 'Test Environment'
            },
        ]
    )

create_sg()
create_instance()
instance_tag()




