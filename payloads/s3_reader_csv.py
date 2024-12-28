import boto3
import csv
import os
import json


DEFAULT_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"


def s3_read_file():
    s3_client = boto3.client('s3')  # Use client, not resourc

    try:
        # Extract S3 bucket name and file key from the event
        # bucket_name = event['Records'][0]['s3']['bucket']['name']
        # file_key = event['Records'][0]['s3']['object']['key']
        bucket_name = 'tf-example-bucket123'
        file_key = 'emp_data'

        print(f"Reading file {file_key} from bucket {bucket_name}")

        # Ensure the 'tmp' directory exists
        local_tmp_dir = "./tmp"
        os.makedirs(local_tmp_dir, exist_ok=True)
        local_file_path = f"{local_tmp_dir}/{os.path.basename(file_key)}"

        # Download the file from S3
        # local_file_path = f"/tmp/{os.path.basename(file_key)}"
        s3_client.download_file(bucket_name, file_key, local_file_path)

        # Read and process the CSV file
        with open(local_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)  # Print each row to logs
                message_body = json.dumps(row) # Convert row to JSON format

                publish_message(message_body)

        return {
            'statusCode': 200,
            'body': 'CSV file read successfully'
        }

    except Exception as e:
        print(f"Error reading file: {e}")
        return {
            'statusCode': 500,
            'body': f"Error reading file: {e}"
        }


