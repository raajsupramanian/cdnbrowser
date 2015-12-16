from datetime import datetime
from boto.s3.connection import S3Connection
from .models import Bucket


class S3Connect(object):
    def __init__(self, access_key, secret):
        self.con_obj = S3Connection(access_key, secret)

    @staticmethod
    def _get_datetime_obj(time_str):
        return datetime.strptime(time_str.split('.')[0], '%Y-%m-%dT%H:%M:%S')

    def _get_bucket_list(self):
        bucket_list = self.con_obj.get_all_buckets()
        bucket_details = []
        for bucket_obj in bucket_list:
            bucket_dict = {'name': bucket_obj.name, 'created_date': self._get_datetime_obj(bucket_obj.creation_date)}
            bucket_details.append(bucket_dict)
        print bucket_details
        return bucket_details

    def update_create_bucket(self, access_obj):
        buckets_list = self._get_bucket_list()
        for bucket in buckets_list:
            Bucket.objects.update_or_create(access=access_obj, name=bucket['name'],
                                            creation_date=bucket['created_date'])
        return


if __name__ == '__main__':
    s3obj = S3Connect('AKIAIK63KH2K3UQGFCHQ', 'CkoWP0zd/P4ufOHi+rYocdLowQmrRgFoFJfwhD/r')
    s3obj._get_bucket_list()
