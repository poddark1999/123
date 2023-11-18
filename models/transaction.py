from datetime import datetime
from model import Model
from user import User
from typing import Union


class Transaction(Model):
    '''
    Class to represent all possible types of transactions.
    '''
    all = []
    data_types = {'uuid': str, 'user_uuid': str, 'amount': Union[float, int],
                  'note': Union[str, None], 'date': datetime}

    def __init__(self, **attributes):
        '''
        Constructor

        :param amount: amount of the transaction.
        :param user_uuid: unique identifier of the user associated with this transaction.
        :param date: date of the transaction (default is the current date).
        :param note: any additional notes or comments about this transaction.
        '''
        self.__amount = attributes['amount']
        if 'uuid' not in attributes:
            super().__init__()
        else:
            self.__uuid = attributes['uuid']
        self.user_uuid = attributes['user_uuid']
        self.date = attributes.get('date', datetime.now())
        self.note = attributes.get('note', None)
        if isinstance(self, Transaction):
            Transaction.all.append(self)

    @property
    def amount(self):
        return self.__amount

    ## TO DO
    ## - Add a setter method for the amount attribute
    ##  - this method will check that the amount which is added is non-negative and raise a ValueError
    ##    if it is.



#class RecurringExpense(Transaction): ------commented as it needs to be moved to buckets
    '''
    Represents recurring expenses.
    '''

#    def __init__(self, frequency, start_date=datetime.now(), expiry_date=None, is_paused=False):
    '''
        Constructor
        :param frequency: frequency of the expense (daily/weekly/monthly/yearly).
        :param start_date: starting date of the recurring expense.
        :param expiry_date: end date of the recurring expense. Can be None if it's indefinite.
        :param is_paused: boolean to indicate if the recurring expense is currently paused.
        '''
#        pass


class Allocation(Transaction):
    '''
    Represents money allocations.
    '''
    all = []
    data_types = {'uuid': str, 'user_uuid': str, 'date': Union[float, int],
                  'note': Union[str, None], 'target_uuid': str}

    def __init__(self, **attributes):
        '''
        Constructor
        :param target_uuid: unique identifier of the bucket where the money will be allocated.
        '''
        if 'uuid' in attributes:
            super().__init__(amount=attributes['amount'], user_uuid=attributes['user_uuid'],
                            note=attributes.get('note', None), date=attributes.get('date', datetime.now()),
                            uuid=attributes['uuid'])
        else:
            super().__init__(amount=attributes['amount'], user_uuid=attributes['user_uuid'],
                            note=attributes.get('note', None), date=attributes.get('date', datetime.now()))
        self.target_uuid = attributes['target_uuid']
        Allocation.all.append(self)


class Income(Transaction):
    '''
    Represents incomes.
    '''
    all = []
    data_types = {'uuid': str, 'user_uuid': str, 'date': Union[float, int],
                  'note': Union[str, None], 'frequency': str, 'start_date': datetime,
                  'source': str, 'end_date': Union[None, datetime]}
    def __init__(self, **attributes):
        '''
        Constructor
        :param source: source of the income (e.g., "Salary", "Freelance").
        :param frequency: frequency of the income (default is "One-Time").
        :param start_date: date when the income starts (relevant for recurring incomes).
        :param end_date: date when the income ends (can be None if it's indefinite).
        '''
        if 'uuid' in attributes:
            super().__init__(amount=attributes['amount'], user_uuid=attributes['user_uuid'],
                            note=attributes.get('note', None), date=attributes.get('date', datetime.now()),
                            uuid=attributes['uuid'])
        else:
            super().__init__(amount=attributes['amount'], user_uuid=attributes['user_uuid'],
                            note=attributes.get('note', None), date=attributes.get('date', datetime.now()))
        self.source = attributes['source']
        self.start_date = attributes.get('start_date', datetime.now())
        self.end_date = attributes.get('end_date', None)
        self.frequency = attributes.get('frequency', 'One-Time')


if __name__ == '__main__':
    # Create a User object
    u = User(first_name="John", last_name="Doe", username="johndoe", password="StrongPass123!")
    user_uuid = u.uuid  # Assuming User class has a uuid attribute

    # Capture the current time before creating the Transaction object
    current_time = datetime.now()
    # Test if Transaction and derived classes correctly inherit from Model
    t = Transaction(amount=100, user_uuid=user_uuid, date=current_time)
    #re = RecurringExpense(100, user_uuid, "daily")
    a = Allocation(amount=100, user_uuid=user_uuid, target_uuid="transaction-bucket-id")
    i = Income(amount=100, user_uuid=user_uuid, source="Salary")

    # Test inheritance of Transaction class from Model class
    try:
        t.uuid
        print("Transaction class correctly inherits attributes from Model!")
    except AttributeError:
        assert False, "Transaction class does not inherit from Model!"

    assert isinstance(t,
                      Model), "Transaction class does not inherit from Model!"
    #assert isinstance(
    #    re, Model), "RecurringExpense class does not inherit from Model!"
    assert isinstance(a,
                      Model), "Allocation class does not inherit from Model!"
    assert isinstance(i, Model), "Income class does not inherit from Model!"
    print("Inheritance tests passed!")

    # Test attribute types
    assert isinstance(
        t.amount,
        (int, float)), "Transaction amount is not of type int or float!"
    #assert isinstance(
    #    re.amount,
    #    (int, float)), "RecurringExpense amount is not of type int or float!"
    assert isinstance(
        a.amount,
        (int, float)), "Allocation amount is not of type int or float!"
    assert isinstance(
        i.amount, (int, float)), "Income amount is not of type int or float!"
    print("Attribute type tests for 'amount' passed!")

    # Test privacy of relevant attributes
    try:
        t.amount = 100 # Direct access to the private attribute should not work outside the class
        print("Transaction amount is not private as expected!")
    except AttributeError:
        print("Privacy test passed!")

    # Test other behaviors, like the correct default assignment, etc.
    assert t.date == current_time, "Transaction date not correctly assigned!"
    assert i.frequency == "One-Time", "Income frequency default value not correctly assigned!"
    print("Default assignment tests passed!")

    print("All tests passed!")
