import boto3
import json
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)

    bucket = event['pathParameters']['bucket']
    key = event['pathParameters']['key']

    print(f"Getting image [{key}] from bucket [{bucket}].")

    try:
        data = s3.get_object(Bucket=bucket, Key=key)
        json_data = data["Body"].read()
        base64_content = base64.b64encode(json_data)

        print(f"Image [{key}] was processed.")

        return {
            "response_code": 200,
            "data": base64_content
        }
    except Exception as e:
        print(e)
        return {
            "response_code": 500,
            "data": "The image could not be processed."
        }
        #raise e
