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
