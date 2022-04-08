from os import name
from urllib import response
import boto3
import botocore
import argparse

client = boto3.client("s3")

import json
def read_bucket_policy(bucket_name):
   try:
       client.get_bucket_policy(Bucket=bucket_name)
       #policy_str=response.get("Policy")
       #print(json.loads(policy_str))
       print("Bucket Policy already Exists")
   except:
       print("Bucket Policy dos not Exists")

def generate_policy(bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject19",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": [f"arn:aws:s3:::{bucket_name}/dev/*", f"arn:aws:s3:::{bucket_name}/test/*" ]
            }
                ]
        }
    return json.dumps(policy)

def create_policy(bucket_name):
    if not read_bucket_policy(bucket_name):
        try:
            client.put_bucket_policy(Bucket=bucket_name,
                                     Policy=generate_policy(bucket_name))
        except botocore.exceptions.ClientError as ex:
            print(ex)
        except:
            return False
       

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket",
                        help="to create bucket policy you can write 'python create-policy.py -b=bucketname")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    bucket_name = f"{args.bucket}"
    #read_bucket_policy(bucket_name)
    create_policy(bucket_name)
    #print(read_bucket_policy(bucket_name))

 
if __name__ == '__main__':
    main()
