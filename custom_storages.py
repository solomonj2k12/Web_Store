from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

"""
used to play static and media files in amazonaws static and media directory

"""
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION