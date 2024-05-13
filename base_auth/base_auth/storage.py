from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static"
    
    #static 폴더 안에 넣어라