import boto3

def upload_diagnostics_log():
    s3_client = boto3.client('s3')
    bucket_name = 'telemetry-diagnostics-logs'
    file_name = 'diagnostics.log'
    s3_key = f'diagnostics/{file_name}'

    s3_client.upload_file(file_name, bucket_name, s3_key)

if __name__ == "__main__":
    upload_diagnostics_log()
