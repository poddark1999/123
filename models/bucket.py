from model import Model
from datetime import datetime


class Bucket(Model):
    '''
    The Bucket class models the goals that a user aims to attain, represented as "buckets".
    Each bucket has a financial target amount, a deadline, and additional meta information.
    '''

    def __init__(self, name, goal, user_uuid, deadline, comment=None):
        '''
        Constructor method

        Params
        ------
        :param name: Name of the bucket
        :type name: str

        :param goal: Monetary goal to achieve for this bucket
        :type goal: float or int

        :param user_uuid: UUID of the user creating the bucket
        :type user_uuid: str

        :param deadline: Date by which the bucket's goal should be met
        :type deadline: datetime object

        :param comment: Optional comment or note about the bucket
        :type comment: str, default is None

        Additionally, upon creation of a bucket, an attribute creation_date
        records when a bucket is created and an attribute completed to track the status.
        '''

        # Private attributes: creation_date, completed
        # TODO: Initialize the attributes. The creation_date should be set to datetime.now()
        # and completed should be set to False by default.
        pass

    @property
    def creation_date(self, type="date"):
        '''
        Getter method for the date a bucket was created

        Params
        ------
        :param type: String defining the type of return.
                     Can be "date" for datetime object or "str" for string.
                     Default is "date".
        :type type: str

        Return
        ------
        :return: Date the bucket was created
        :rtype: datetime object or str
        '''
        # TODO: Implement method to return the creation date based on the type parameter
        pass

    @property
    def is_completed(self):
        '''
        Getter method to check if a bucket's goal has been achieved

        Return
        ------
        :return: Status of bucket's goal completion
        :rtype: bool
        '''
        # TODO: Return the status of the bucket's completion attribute
        pass

    def mark_as_completed(self):
        '''
        Method to set the bucket's goal as achieved

        Return
        ------
        :return: None
        '''
        # TODO: Set the bucket's completed attribute to True
        pass


if __name__ == '__main__':
    pass
