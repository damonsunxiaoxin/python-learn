
class Ec2Lister:
    def __init__(self, aws_client):
        """
        Initializes Ec2Lister with AWS client.
        :param aws_client: AWSClient object
        """
        self.ec2_client = aws_client.client

    def list_instances(self):
        """
        Lists all instance.
        """
        response = self.ec2_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets
