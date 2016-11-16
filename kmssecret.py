import os, boto3

kms = boto3.client('kms')

class KmsSecret:
    def __init__(self):
        cwd = os.getcwd()
        for secret in os.listdir('{}/secrets'.format(cwd)):
            with open('{}/secrets/{}'.format(cwd, secret), 'rb') as f:
                setattr(self, secret, kms.decrypt(
                    CiphertextBlob=f.read()
                )['Plaintext'])

secret = KmsSecret()
