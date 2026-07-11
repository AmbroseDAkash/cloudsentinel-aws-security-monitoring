import json
import boto3
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')

SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    bucket_name = None

    try:
        detail = event.get("detail", {})
        request_params = detail.get("requestParameters", {})

        bucket_name = request_params.get("bucketName")

        # Some events may structure bucket info differently
        if not bucket_name:
            bucket_name = request_params.get("bucket")

        if not bucket_name:
            message = f"Could not identify bucket name from event: {json.dumps(event)}"
            print(message)
            return {"statusCode": 400, "body": message}

        # 1. Re-enable block public access at bucket level
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )

        # 2. Try removing any public bucket ACL by setting bucket owner full control
        try:
            s3.put_bucket_acl(
                Bucket=bucket_name,
                ACL='private'
            )
        except Exception as acl_error:
            print(f"Could not reset ACL for bucket {bucket_name}: {str(acl_error)}")

        # 3. Send SNS alert
        alert_message = f"""
[ALERT] S3 Public Access Change Detected and Remediated

Bucket: {bucket_name}
Action Taken:
- Re-enabled Block Public Access
- Attempted to reset bucket ACL to private

Please review CloudTrail logs for the initiating user and API call.
"""
        if SNS_TOPIC_ARN:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="S3 Public Access Auto-Remediation Alert",
                Message=alert_message
            )

        return {
            "statusCode": 200,
            "body": f"Successfully remediated bucket: {bucket_name}"
        }

    except Exception as e:
        error_message = f"Error during remediation for bucket {bucket_name}: {str(e)}"
        print(error_message)

        if SNS_TOPIC_ARN:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="S3 Auto-Remediation Failed",
                Message=error_message
            )

        return {
            "statusCode": 500,
            "body": error_message
        }
