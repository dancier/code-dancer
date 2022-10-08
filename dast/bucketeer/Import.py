from minio import Minio
from minio.error import S3Error
from minio.credentials import ClientGrantsProvider

import urllib3
import json


class EventLog:
    host = None
    bucket_name = None
    client = None

    def __init__(self, host, bucket_name):
        self.host = host
        self.bucket_name = bucket_name
        self.client = Minio("test-s3.dancier.net")

    def import_events(self):
        for obj in self.client.list_objects("test"):
            print(obj.object_name)

    def list_with_prefix(self):
        for obj in self.client.list_objects("test", prefix="test123-"):
            print(obj.object_name)
