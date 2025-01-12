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
