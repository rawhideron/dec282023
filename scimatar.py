#!/usr/bin/python3
# testing
import boto3

def create_jenkins_environment():
    cloudformation = boto3.client('cloudformation')
    
    template = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Resources": {
            "JenkinsMaster": {
                "Type": "AWS::EC2::Instance",
                "Properties": {
                    # Define the properties for the Jenkins master instance
                    # such as instance type, AMI, security groups, etc.
                    "InstanceType": "t2.micro",
                    "ImageId": "ami-0c7217cdde317cfec",
                    "SecurityGroupIds": ["sg-09bb33d2e56736cb6"],
                    # Add other properties as needed
                }
            },
            "JenkinsNode1": {
                "Type": "AWS::EC2::Instance",
                "Properties": {
                    # Define the properties for the first Jenkins node instance
                    "InstanceType": "t2.micro",
                    "ImageId": "ami-0c7217cdde317cfec",
                    "SecurityGroupIds": ["sg-09bb33d2e56736cb6"],
                    # Add other properties as needed
                }
            },
            "JenkinsNode2": {
                "Type": "AWS::EC2::Instance",
                "Properties": {
                    # Define the properties for the second Jenkins node instance
                    "InstanceType": "t2.micro",
                    "ImageId": "ami-0c7217cdde317cfec",
                    "SecurityGroupIds": ["sg-09bb33d2e56736cb6"],
                    # Add other properties as needed
                }
            },
            "JenkinsNode3": {
                "Type": "AWS::EC2::Instance",
                "Properties": {
                    # Define the properties for the third Jenkins node instance
        
                "InstanceType": "t2.micro",
                    "ImageId": "ami-0c7217cdde317cfec",
                    "SecurityGroupIds": ["sg-09bb33d2e56736cb6"],
                    # Add other properties as needed
            }
            }
        }
    }
    
    response = cloudformation.create_stack(
        StackName='JenkinsEnvironment',
        TemplateBody=str(template),
        # Add other parameters as needed, such as VPC, subnets, etc.
        
    )
    
    print("Stack creation initiated. Stack ID:", response['StackId'])

create_jenkins_environment()
