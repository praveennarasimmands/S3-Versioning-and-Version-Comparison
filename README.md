# S3 Versioning and Version Comparison

## **Problem Statement**

In the domains of **Media & Entertainment**, **Legal**, and **Education**, content and documents undergo frequent revisions. Keeping track of these revisions while ensuring that earlier versions are not lost or overwritten is a critical requirement. For instance, in:
- **Media & Entertainment**: New versions of video files, audio recordings, and images are uploaded regularly.
- **Legal**: Contracts and legal documents evolve over time, requiring an ability to track, compare, and retrieve prior drafts.
- **Education**: Course materials and textbooks are often updated, with instructors needing access to previous versions.

The challenge lies in:
1. **Tracking Versions**: Managing and storing multiple versions of the same file.
2. **Avoiding Data Loss**: Preventing accidental overwrites of important files.
3. **Comparing Versions**: Providing a way to compare different file versions to analyze the changes.

## **Solution Overview**

We will leverage **Amazon S3 Versioning** to solve this problem. S3 Versioning allows us to automatically store multiple versions of an object in a bucket, helping us track changes and prevent data loss. Additionally, we will implement an automated **Version Comparison** system using Python and the Boto3 library to allow users to compare different versions of files stored in S3.

### **How We Will Solve This:**

1. **Enable S3 Versioning**: We will configure an S3 bucket to enable versioning, ensuring that every file modification creates a new version instead of overwriting the existing file.
2. **Compare Object Versions**: We will write a Python script that lists all versions of a given object and compares their metadata, allowing users to identify differences between versions.
3. **Provide Easy Integration**: The code will be structured in a modular way to integrate easily with various domains, such as **Media & Entertainment**, **Legal**, and **Education**, where frequent updates to files are common.

---

## **Features**

- **S3 Versioning**: Automatically enables version tracking for files in S3 buckets.
- **Automated Version Comparison**: Compares multiple versions of a file to help analyze changes.
- **Cross-Domain Applicability**: Works for Media & Entertainment, Legal, and Education files, ensuring broad usability across industries.
- **Simple Python Scripts**: Easy-to-use scripts that can be executed to enable versioning and compare versions directly.

---

## **How It Works**

### **Step 1: Enable S3 Versioning**
- We use the **Boto3 Python SDK** to enable S3 versioning on a specific bucket. Versioning ensures that every time a file is uploaded or modified, it is stored with a unique version ID.

### **Step 2: Version Comparison**
- Using another Python script, we will list all versions of an object stored in the S3 bucket and compare their metadata (such as `LastModified` and `VersionId`) to track changes between versions.
- We will also print out information about the versions, such as when the version was created, making it easy to spot changes.

### **Step 3: Integration with Various Domains**
- The solution will be applicable across different domains by simply applying it to the corresponding S3 buckets and objects. We will manage video files for Media & Entertainment, legal contracts for Legal teams, and course materials for Education.

---

## **Project Structure**

Below is the Git repository structure for this project:

```plaintext
s3-versioning-project/
│
├── README.md                    # Project description and setup instructions
├── requirements.txt              # Python dependencies
├── versioning.py                 # Script to enable versioning
├── compare_versions.py           # Script to compare versions of objects in S3
├── config/
│   └── s3_config.py              # S3 configuration file (bucket names, AWS credentials, etc.)
└── tests/
    ├── test_versioning.py        # Unit test for versioning-related functionality
    └── test_compare_versions.py  # Unit test for comparing versions of objects
```

---

## **Code Explanation**

### **1. `README.md`**

This file provides an overview of the project, how to set it up, and how to use it. It includes instructions on installing dependencies, setting up AWS credentials, and running the scripts.

### **2. `requirements.txt`**

```plaintext
boto3==1.24.5
pytest==7.0.1
```

This file lists the required dependencies to run the scripts, including **Boto3** (AWS SDK for Python) and **pytest** for testing.

### **3. `versioning.py`** – Enabling S3 Versioning

This Python script enables versioning on the specified S3 bucket.

```python
import boto3

def enable_s3_versioning(bucket_name):
    s3 = boto3.client('s3')
    
    # Enable versioning for the specified S3 bucket
    response = s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"Versioning enabled for bucket: {bucket_name}")
    return response

if __name__ == '__main__':
    bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
    enable_s3_versioning(bucket_name)
```

### **4. `compare_versions.py`** – Comparing Versions

This Python script compares the versions of an object in an S3 bucket.

```python
import boto3

def compare_versions(bucket_name, object_key):
    s3 = boto3.client('s3')
    
    # List all versions of the specified object
    response = s3.list_object_versions(Bucket=bucket_name, Prefix=object_key)
    versions = response.get('Versions', [])
    
    if len(versions) > 1:
        latest_version = versions[0]
        previous_version = versions[1] if len(versions) > 1 else None
        
        # Compare metadata or content (for simplicity, we're comparing version IDs)
        print(f"Latest Version ID: {latest_version['VersionId']}")
        if previous_version:
            print(f"Previous Version ID: {previous_version['VersionId']}")
            # Add logic to compare the content or metadata, like LastModified date or file hashes.
    else:
        print("Only one version found. No comparison necessary.")

if __name__ == '__main__':
    bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
    object_key = 'path/to/your/file.jpg'  # Replace with the object key
    compare_versions(bucket_name, object_key)
```

### **5. `config/s3_config.py`** – S3 Configuration (Optional)

```python
AWS_BUCKET_NAME = 'your-s3-bucket-name'  # Replace with your S3 bucket name
AWS_ACCESS_KEY = 'your-access-key'  # Replace with your AWS access key
AWS_SECRET_KEY = 'your-secret-key'  # Replace with your AWS secret key
```

### **6. Unit Tests:**

- **`test_versioning.py`**: Tests the script responsible for enabling versioning.
- **`test_compare_versions.py`**: Tests the version comparison functionality.

### **Test Example for `versioning.py`**

```python
import unittest
from versioning import enable_s3_versioning

class TestS3Versioning(unittest.TestCase):

    def test_enable_versioning(self):
        # Test the versioning enable functionality
        bucket_name = 'test-bucket-name'
        result = enable_s3_versioning(bucket_name)
        self.assertIn('Status', result['VersioningConfiguration'])

if __name__ == '__main__':
    unittest.main()
```

---

## **How to Use**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/s3-versioning-project.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS credentials** using the AWS CLI or directly in the `config/s3_config.py` file.

4. **Enable S3 versioning** by running:
   ```bash
   python versioning.py
   ```

5. **Compare versions** of a file using:
   ```bash
   python compare_versions.py
   ```

6. **Run unit tests** to verify functionality:
   ```bash
   pytest tests/
   ```

---

## **Conclusion**

This project leverages **Amazon S3 Versioning** to ensure proper version tracking and version comparison across different domains. The solution is flexible, easy to integrate, and provides a way to manage file revisions without losing data, helping teams in **Media & Entertainment**, **Legal**, and **Education** stay organized and efficient.
