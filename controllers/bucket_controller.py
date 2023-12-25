from controllers.model_controller import ModelController
from models.bucket import Bucket

class BucketController(ModelController):
    '''
    Controller class for managing operations related to Buckets.
    '''
    def __init__(self):
        super().__init__()
        self.load_instances()

    def create_bucket(self, name, goal, deadline, user_uuid, frequency, icon=None,comment=None, currency='EUR'):
        '''
        Creates a new bucket.

        Params
        ------
            :param name: name of the bucket
            :type name: str
            :param goal: monetary goal to reach for the desired bucket
            :type goal: float, int
            :param deadline: date by which the goal of a given bucket should be reached
            :type deadline: datetime object
            :param user_uuid: uuid of the user creating the bucket
            :type user_uuid: str
            :param comment: additional comment regarding a bucket
            :type comment: str, optional

        Return
        ------
            :return: Newly created bucket instance or relevant error message.
        '''
        bucket = Bucket(name=name, goal=goal, deadline=deadline,
                        user_uuid=user_uuid, comment=comment, icon=icon,
                        currency='EUR', frequency=frequency)
        self.all.append(bucket)

    def export_instances(self, load=False):
        return super().export_instances(csv='buckets.csv', cls=Bucket, load=load)

    def load_instances(self, cls=Bucket, csv='buckets.csv'):
        return super().load_instances('Bucket', csv, cls, Bucket.data_types)

    def retrieve_bucket(self, bucket_uuid):
        '''
        Retrieves a bucket based on its UUID.

        Params
        ------
            :param bucket_uuid: uuid of the bucket
            :type bucket_uuid: str

        Return
        ------
            :return: Bucket instance corresponding to the provided UUID or relevant error message.
        '''
        for bucket in self.all:
            if bucket.uuid == bucket_uuid:
                return bucket

    def update_bucket(self, bucket_uuid, **kwargs):
        '''
        Updates attributes of a given bucket.

        Params
        ------
            :param bucket_uuid: uuid of the bucket to be updated
            :type bucket_uuid: str
            :param kwargs: a dictionary of attributes to be updated with their new values
            :type kwargs: dict
        Return
        ------
            :return: Updated bucket instance or None.
            :rtype: Bucket or None
        '''
        for bucket in self.all:
            if bucket.uuid == bucket_uuid:
                for key, value in kwargs.items():
                    setattr(bucket, key, value)
                return bucket

    def delete_bucket(self, bucket_uuid):
        '''
        Deletes a bucket based on its UUID.

        Params
        ------
            :param bucket_uuid: uuid of the bucket to be deleted
            :type bucket_uuid: str

        Return
        ------
            :return: True if Bucket was successfully deleted.
            :rtype: bool
        '''
        for bucket in self.all:
            if bucket.uuid == bucket_uuid:
                self.all.remove(bucket)
                return True

    def list_buckets(self, user_uuid):
        '''
        Lists all buckets associated with a user.

        Params
        ------
            :param user_uuid: uuid of the user
            :type user_uuid: str

        Return
        ------
            :return: List of bucket instances associated with the user or relevant error message.
        '''
        return filter(lambda bucket: bucket.user_uuid == user_uuid,  self.all)

    def check_bucket_status(bucket_uuid):
        '''
        Checks the status of a bucket (e.g., how close it is to its goal, if it's expired, etc.).

        Params
        ------
            :param bucket_uuid: uuid of the bucket
            :type bucket_uuid: str

        Return
        ------
            :return: A status message indicating the bucket's progress, expiration status, etc.
        '''
        pass

