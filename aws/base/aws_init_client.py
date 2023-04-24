import boto3

ACCESS_KEY = 'AKIARRA7YBVQJVZLNCFL'
SECRET_KEY = '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'


class AWSClient:
    def __init__(self, service_type, access_key=None, secret_key=None, role_arn=None, session_name=None, ext_id=None):
        """
        Initializes AWS client for the given service type using either access key and secret key or role ARN.
        :param service_type: AWS service type, e.g. 'ec2', 's3'
        :param access_key: AWS access key
        :param secret_key: AWS secret key
        :param role_arn: AWS role ARN
        """
        if access_key and secret_key:
            self.client = boto3.client(service_type, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        elif role_arn:
            sts_client = boto3.client('sts', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
            assumed_role_object = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name, ExternalId=ext_id)
            credentials = assumed_role_object['Credentials']
            self.client = boto3.client(service_type, aws_access_key_id=credentials['AccessKeyId'],
                                       aws_secret_access_key=credentials['SecretAccessKey'],
                                       aws_session_token=credentials['SessionToken'])
        else:
            self.client = boto3.client(service_type)