import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 for printout in pythonins['Instances']:
  print(Myec2['Reservations'])   
#   print(pythonins['Instances'])
  print(printout['InstanceId'])