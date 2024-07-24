import boto3
import time

def send_logs():
    client = boto3.client('logs', region_name='us-east-1')
    log_group = 'telemetry-logs'
    log_stream = 'system-monitor'

    create_log_stream_if_not_exists(client, log_group, log_stream)

    while True:
        timestamp = int(time.time() * 1000)
        message = f'System status at {timestamp}'
        response = client.put_log_events(
            logGroupName=log_group,
            logStreamName=log_stream,
            logEvents=[
                {
                    'timestamp': timestamp,
                    'message': message
                },
            ],
        )
        time.sleep(3600)

def create_log_stream_if_not_exists(client, log_group, log_stream):
    log_streams = client.describe_log_streams(logGroupName=log_group)
    log_stream_names = [stream['logStreamName'] for stream in log_streams['logStreams']]
    if log_stream not in log_stream_names:
        client.create_log_stream(
            logGroupName=log_group,
            logStreamName=log_stream
        )

if __name__ == "__main__":
    send_logs()
