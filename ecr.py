import boto3

ecr_client = boto3.client('ecr', region_name = 'us-east-1')

repo_name = "my-cloud-native-repo"

response = ecr_client.create_repository(repositoryName=repo_name)


repository_uri = response['repository']['repositoryUri']
print(repository_uri)