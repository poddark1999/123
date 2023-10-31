from model_controller import ModelController
from models.bucket import Bucket

class BucketController(ModelController):
    '''
    Controller class for managing operations related to Buckets.
    '''

    @staticmethod
    def create_bucket(name, goal, deadline, user_uuid, comment=None):
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
        pass

    @staticmethod
    def retrieve_bucket(bucket_uuid):
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
        pass

    @staticmethod
    def update_bucket(bucket_uuid, **kwargs):
        '''
        Updates attributes of a given bucket.

        Params
        ------
            :param bucket_uuid: uuid of the bucket to be updated
            :type bucket_uuid: str
            :param kwargs: a dictionary of attributes to be updated with their new values

        Return
        ------
            :return: Updated bucket instance or relevant error message.
        '''
        pass

    @staticmethod
    def delete_bucket(bucket_uuid):
        '''
        Deletes a bucket based on its UUID.

        Params
        ------
            :param bucket_uuid: uuid of the bucket to be deleted
            :type bucket_uuid: str

        Return
        ------
            :return: Confirmation message indicating successful deletion or relevant error message.
        '''
        pass

    @staticmethod
    def list_buckets(user_uuid):
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
        pass

    @staticmethod
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


class TransactionController(ModelController):
    '''
    Controller class for managing operations related to Transactions.
    '''

    @staticmethod
    def create_transaction(type_, amount, date, user_uuid, description=None,
                           recurrence=None, end_date=None):
        """
        Create a new transaction and save it.

        :param type_: Type of the transaction (Expense, Income, etc.)
        :param amount: Amount of the transaction.
        :param date: Date of the transaction.
        :param user_uuid: UUID of the user associated with the transaction.
        :param description: Optional description for the transaction.
        :param recurrence: Recurrence of the transaction (None if not recurring).
        :param end_date: Optional end date for recurring transactions.
        :return: Instance of the created transaction.
        """
        # Logic for creating and saving the transaction goes here...
        pass

    @staticmethod
    def update_transaction(transaction_uuid, **kwargs):
        """
        Update details of a specific transaction.

        :param transaction_uuid: UUID of the transaction to update.
        :param kwargs: Updated fields for the transaction.
        :return: Updated transaction instance or relevant error.
        """
        # Logic for updating the transaction goes here...
        pass

    @staticmethod
    def delete_transaction(transaction_uuid):
        """
        Delete a specific transaction.

        :param transaction_uuid: UUID of the transaction to delete.
        :return: Confirmation of deletion or relevant error.
        """
        # Logic for deleting the transaction goes here...
        pass

    @staticmethod
    def get_transaction_by_uuid(transaction_uuid):
        """
        Retrieve a specific transaction using its UUID.

        :param transaction_uuid: UUID of the transaction to retrieve.
        :return: Transaction instance or None if not found.
        """
        # Logic for retrieving the transaction goes here...
        pass

    @staticmethod
    def list_transactions(user_uuid, start_date=None, end_date=None):
        """
        List all transactions for a specific user, optionally filtered by date range.

        :param user_uuid: UUID of the user whose transactions to list.
        :param start_date: Optional start date to filter transactions.
        :param end_date: Optional end date to filter transactions.
        :return: List of transaction instances.
        """
        # Logic for listing the transactions goes here...
        pass
