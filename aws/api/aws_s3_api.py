
class S3BucketLister:
    def __init__(self, aws_client):
        """
        Initializes S3BucketLister with AWS client.
        :param aws_client: AWSClient object
        """
        self.s3_client = aws_client.client

    def list_buckets(self):
        """
        Lists all S3 buckets.
        """
        response = self.s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets
