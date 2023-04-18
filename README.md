# Hello,
## this readme file will give instruction of how to run the project.

This is a boto3 and ansible project,
The project purpose is to provision a ec2 instance on AWS with security group
assigned to the new instance and tag it.
Then install on the instance web-application that present your name(I used ansible).

## **Prerequisites:**

### AWS IAN user
* Navigate to your AWS user.
* Search for IAM --> Create new user(Only if do not exsists).
* Give progrematic access
* Add administrator policy.
* Save access ID and secret key.

### Packages install
- pip/3 install boto3
- pip/3 install awscli

### Configure your AWScli user:
- Type in Terminal: aws configure
- Insert your access ID and secret key from AWS IAN user creation.
- Enter the region your AWS user working on.

## Run the script
Run the Python Boto3 code - <ec2_instance_with_security_group.py>
Take the new Public IPv4 address from the new instance (Using the AWS GUI (Sorry didnt found a way to get the instance public IP))
Place it in the ansible_hosts file located in playboks directory.


## To add your id_rsa to the new instance Playbook - Type: (If you do not have public key, please create one using ssh-keygen)
cd playbooks/
ansible-playbook add-key.yml -i ansible_hosts  --user ec2-user --key-file <Your_AWS_key_pair_path> -e "key=<Your_public_key_path>"
### Example:
ansible-playbook add-key.yml -i ansible_hosts  --user ec2-user --key-file ~/Downloads/Key_pair_aws.pem -e "key=~/.ssh/id_rsa.pub"

## To Run Playbook - Type:
ansible-playbook install_apache.yaml -i ansible_hosts  --user ec2-user

Visit:<Instance_public_ip:80>





ansible hosts_to_add_key -m ping -i ansible_hosts --user ec2-user --key-file ~/Downloads/Key_pair_aws.pem
