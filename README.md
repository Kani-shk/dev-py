# ☁️ S3 Backup Uploader

A simple Python script to create an S3 bucket, list existing buckets, and upload backup files to AWS S3 using the `boto3` library.

---

## 📂 Features

- ✅ Create a new S3 bucket in a specified region
- ✅ List all current S3 buckets
- ✅ Upload local backup files to S3 with a custom object key

---

## 🛠️ Requirements

- Python 3.6+
- AWS CLI configured (`aws configure`)
- `boto3` installed

---

## 📦 Installation


1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/s3-backup-uploader.git
   cd s3-backup-uploader

2. **Install dependencies**

   ```bash
   pip install boto3

3. **Configure AWS CLI**
   ```bash
   aws configure

---

# 🚀 Usage
1. Edit the script file (main.py) with your desired:
 ```python 
   bucket_name (the bucket your file will be sent to)
   region (AWS region)
   file_name (path to your backup file)
   key_name (S3 object key)
```
2. Run the following script:
   ```bash
   python main.py
   ```
---

#🧪 Functions Overview

**function description:**

- create_bucket()	Creates an S3 bucket in the given region
- show_bucket()	Lists all buckets in your AWS account
- upload_backup()	Uploads a local file to the selected bucket

---


