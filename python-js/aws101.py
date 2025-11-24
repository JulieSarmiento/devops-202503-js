from dotenv import load_dotenv
import boto3
import os

load_dotenv()

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_REGION")


""" 
## resource mode
ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

instances_list = ec2.instances.all()

for inst in instances_list:
    id = inst.id
    state = inst.state['Name']
    print("instance:", id , f"is in state: {state}") 
"""



## client mode, more detailed
ec2_serv = boto3.client( 
    "ec2",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)
desc_instances = ec2_serv.describe_instances() 

for reserv in desc_instances["Reservations"]:
    for inst in reserv["Instances"]:
        id = inst["InstanceId"]
        state = inst["State"]["Name"]
        print("instance:", id , f"is in state: {state}")
## in this mode we can extract more details about the instances
## like tags.