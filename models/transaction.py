from datetime import datetime
import os
import re
from model import Model

class Transaction(Model):
    '''
    Class to represent all possible types of transactions
    that will take place on the platform
    '''

    def __init__(self, amount, user_uuid, date=datetime.now(), comment=None):
        '''
        Constructor that assigns a transaction to a given user
        :param amount: a positive amount for a given transaction
        :type amount: float
        :param user_uuid: uuid of the user
        :type user_uuid: str
        :param date: a date entered in one of several formats
        (DD/MM/YYYY, DD.MM.YYYY, DD/MM/YY, DD.MM.YY), will be turned into datetime object (will be parsed with regular expression)
        Default value: datetime.now()
        :type date: datetime object
        :param comment: facultative comment that can be entered along with transaction,
        Default value: None
        :type comment: str
        '''
        ## TO DO
        ## Create regex to parse possible date formats
        ## Set amount, date, comment attributes as a PRIVATE attributes
        ## Use constructor method from parent class
        ## (modification shouldn't be possible by directly accessing their corresponding values)
        pass

    @property

    def date(self, type="date"):
        '''
        Getter method to get the date of a transaction
        :param type: string which defines the type of the object to be returned by this function
        Possible values: date (for datetime object) and str (for string)
        Default value: date
        :type type: str
        :return: value containing the date
        '''

    @property

    def amount(self):
        '''
        Getter method to get the amount value of a transaction
        :return: float type value containing amount of a given transaction
        '''
        pass

class Allocation(Transaction):

    def __init__(self, bucket):
        '''
        Constructor
        :param bucket: bucket object to which the amount is allocated
        Uses the constructor method of the parent class Transaction
        '''
        pass


class RecurringExpense(Transaction):

    def __init__(self, frequency):
        '''
        Constructor
        :param frequency: frequency at which a
        Uses the constructor method of the parent class Transaction
        '''
        pass
