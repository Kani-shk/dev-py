# dev-py
📦 Backup to AWS S3 – Python Script
This simple Python script allows you to list S3 buckets, create a new bucket, and upload backup files to a specified S3 bucket using the boto3 library.

🚀 Features
List all existing S3 buckets in your AWS account.

Create a new S3 bucket in a specified region.

Upload a backup file to an S3 bucket with a custom key name.

🛠️ Technologies Used
Python 3

boto3 (AWS SDK for Python)

AWS S3

📂 File Structure
bash
Copy
Edit
backup_to_s3.py  # Main script file
🧩 Prerequisites
Python installed (>=3.6)

AWS CLI installed and configured (aws configure)

boto3 installed:

bash
Copy
Edit
pip install boto3
📝 Setup
Configure AWS Credentials:

bash
Copy
Edit
aws configure
Set your file path and bucket details in the script:

python
Copy
Edit
bucket_name = "your-unique-bucket-name"
region = "us-east-2"
file_name = "/path/to/your/backup.tar.gz"
📦 Usage
Uncomment the actions you want to perform inside the script:

python
Copy
Edit
#create_bucket(s3, bucket_name, region )
#show_bucket(s3)
upload_backup(s3, file_name, bucket_name, "backup_filename.tar.gz")
Then run the script:

bash
Copy
Edit
python backup_to_s3.py
✅ Output
Example output:

nginx
Copy
Edit
bucket created successfully!!
backup uploaded successfully!!!
⚠️ Notes
Make sure the bucket name is globally unique across all AWS users.

The script assumes AWS credentials are properly configured.

Only use us-east-2 or supported regions for bucket creation.
