import os

import boto3
import pandas as pd

AWS_ACCESS_KEY = os.environ["AWS_PERSONAL"]
AWS_ACCESS_SECRET = os.environ["AWS_PERSONAL_SECRET"]
AWS_S3_BUCKET = "racheldunne-test"


def get_s3_data(key):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_ACCESS_SECRET,
    )
    response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key=key)
    df = pd.read_csv(response.get("Body"))
    return df
