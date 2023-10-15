from model import Model
from datetime import datetime

class Bucket(Model):
    '''
    The class Bucket will allow us to model
    the buckets representing the goals that the user
    wants to attain.
    '''
    def __init__(self, name, goal, deadline, user_uuid,comment=None):
        '''
        Constructor method
        Uses __init__ method of parent class Model
        :param name: name of the bucket
        :type name: str
        :param goal: monetary goal to reach to reach the desired goal
        :type goal: float, int
        :param deadline: date by which the goal of a given bucket should be reached
        :type deadline: datetime object
        :param uuid: uuid of the user creating the bucket
        :type uuid: str
        :param comment: additional comment regarding a bucket
        Default value: None
        :type comment: str

        Additionally, at the moment of creation of a bucket, we create
        an attribute creation_date (datetime object) which records when
        a bucket is created.
        '''
        ## write init method
        ## add attribute creation_date (datetime.now())
        ## private attributes: creation_date

        pass

    @property

    def creation_date(self, type="date"):
        '''
        Getter method to get the date of a bucket creation
        :param type: string which defines the type of the object to be returned by this function
        Possible values: date (for datetime object) and str (for string)
        Default value: date
        :type type: str
        :return: value containing the date
        '''

if __name__ == '__main__':
    pass
