from urllib import response
import boto3
import botocore
import argparse

client = boto3.client("s3")

def bucket_exists(bucket_name):
    try:
        response = client.head_bucket(Bucket=bucket_name)
    except:
        return False
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return True
    return False 

def create_bucket(bucket_name):
    if not bucket_exists(bucket_name):
        try:
            client.create_bucket(Bucket=bucket_name)
            print(f"Create New '{bucket_name}' Bucket")
        except botocore.exceptions.ClientError as ex:
            print(ex)
    else:
        print(f"Bucket '{bucket_name}' already exists")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket",
                        help="to create bucket you can write 'python create-bucket-if-not.py -b=bucketname" )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    bucket_name = f"{args.bucket}"
    create_bucket(bucket_name)
        


if __name__ == '__main__':
    main()

