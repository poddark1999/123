from controllers.model_controller import ModelController
from models.bucket import Bucket

class BucketController(ModelController):
	'''
	Controller class for managing operations related to Buckets.
	'''
	def __init__(self):
		super().__init__()
		self.load_instances()

	def create_bucket(self, **attributes):
		'''
		Creates a new bucket.

		Params
		------
			:param **attributes: attributes of the Bucket
				these attributes include:
					- name: name of the bucket.
					- goal: target amount of the bucket.
					- user_uuid: unique identifier of the user associated with this bucket.
					- deadline: date of the bucket's deadline.
					- current_amount: current amount of the bucket.
					- comment: any additional notes or comments about this bucket.
					- frequency: frequency of the bucket.
					- icon: icon of the bucket.
					- currency: currency of the bucket.
		Return
		------
			:return: Newly created bucket instance or relevant error message.
		'''
		return super().create(**attributes, obj=Bucket)

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
		return super().retrieve(bucket_uuid)

	def update_bucket(self, bucket_uuid, **attributes):
		'''
		Updates attributes of a given bucket.

		Params
		------
			:param bucket_uuid: uuid of the bucket to be updated
			:type bucket_uuid: str
			:param attributes: a dictionary of attributes to be updated with their new values
			:type attributes: dict
		Return
		------
			:return: Updated bucket instance or None.
			:rtype: Bucket or None
		'''
		return super().update(bucket_uuid, **attributes)

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
		return super().delete(bucket_uuid)

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

	def export_instances(self, load=False):
			return super().export_instances(csv='buckets.csv', cls=Bucket, load=load)

	def load_instances(self, cls=Bucket, csv='buckets.csv'):
		return super().load_instances('Bucket', csv, cls, Bucket.data_types)

	def update_amount_bucket(self, allocations, bucket_uuid):
		'''
		Allocates a given amount of money to a bucket.

		Params
		------
			:param allocation: amount of money to be allocated to a bucket
			:type allocation: float, int
			:param bucket_uuid: uuid of the bucket
			:type bucket_uuid: str

		Return
		------
			:return: Updated bucket instance or relevant error message.
		'''
		total = sum(float(allocation.amount) for allocation in allocations)
		for i, bucket in enumerate(self.all):
			if bucket.uuid == bucket_uuid:
				self.all[i].current_amount = total



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

