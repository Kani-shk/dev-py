import boto3
s3 = boto3.resource("s3")
def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket = bucket_name,  CreateBucketConfiguration={
        'LocationConstraint': region,
        },)
    print("bucket created successfully!!")
def upload_backup(s3, file_name , bucket_name , key_name):
      data = open(file_name , 'rb')
      s3.bucket(bucket_name).put_object(key= key_name ,body= data)
      print("backup uploaded successfully!!!")

bucket_name = "kanishk-devop-python"
region = "us-east-2"


#create_bucket(s3, bucket_name, region )
#show_bucket(s3)
file_name= "/home/kanishk/dev-py/backups/backup_2025-06-10.tar.gz"
upload_backup(s3,file_name, bucket_name, "backup_myback.tar.gz")