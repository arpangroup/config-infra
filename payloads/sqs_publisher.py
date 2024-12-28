import boto3

DEFAULT_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"
sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = 'https://sqs.us-east-1.amazonaws.com/491085411576/order-processing-queue'

def publish_message(message_body: dict, queue_url: str = DEFAULT_QUEUE_URL):
    message_body = '{"orderId": "12345", "status": "created"}'

    response = sqs.send_message( # send_message_batch for batch
        QueueUrl=queue_url,
        MessageBody=message_body
    )

    print("Messages pushed:", response)


def publish_messages_batch(messages: list, queue_url: str = DEFAULT_QUEUE_URL):
    messages = [
        {"Id": "1", "MessageBody": "{\"orderId\": \"12345\", \"status\": \"created\"}"},
        {"Id": "2", "MessageBody": "{\"orderId\": \"67890\", \"status\": \"pending\"}"},
        {"Id": "3", "MessageBody": "{\"orderId\": \"54321\", \"status\": \"shipped\"}"},
    ]

    response = sqs.send_message_batch(
        QueueUrl=queue_url,
        Entries=messages
    )

    print("Messages pushed:", response)


def publish_messages_with_groupId(): # GroupId applicable only for FIFO Queue
    # Define the message body and MessageGroupId
    message_body = '{"orderId": "12345", "status": "created"}'
    message_group_id = 'group1'  # MessageGroupId to group the message

    # Send the message to the FIFO queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body,
        MessageGroupId=message_group_id,  # MessageGroupId for grouping
        # Optional: deduplication ID for avoiding duplicate messages
        # MessageDeduplicationId='unique-deduplication-id'
    )

    print(f"Message sent! Message ID: {response['MessageId']}")


if __name__ == "__main__":
    publish_messages()