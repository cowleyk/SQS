import boto3
from nio.block.base import Block
from nio.properties import (VersionProperty, PropertyHolder, StringProperty,
                            ObjectProperty)
from nio.util.discovery import not_discoverable


class AWSCreds(PropertyHolder):
    aws_access_key_id = StringProperty(
        title="Access Key ID", default="", allow_none=False)
    aws_secret_access_key = StringProperty(
        title="Secret Access Key", default="", allow_none=False)
    aws_session_token = StringProperty(
        title="Session Token", default="", allow_none=True)
    region_name = StringProperty(
        title="Region Name", default="us-east-2", allow_none=True)
    # TODO: FIGURE OUT PROPERTY CONFIGURATION (unittest)


@not_discoverable
class SQSBase(Block):
    """This is the base block for integrating n.io with AWS SQS"""
    version = VersionProperty("1.0.0")
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    # Queue to connect to
    queue_url = StringProperty(title="Queue URL", default="")

    def __init__(self):
        self.client = None
        super().__init__()

    def configure(self, context):
        super().configure(context)
        self.client = boto3.client(
            'sqs',
            region_name=self.creds().region_name(),
            aws_access_key_id=self.creds().aws_access_key_id(),
            aws_secret_access_key=self.creds().aws_secret_access_key(),
            aws_session_token=self.creds().aws_secret_access_key())
