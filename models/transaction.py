from datetime import datetime
from models.model import Model
from models.user import User
from typing import Union


class Transaction(Model):
    '''
    Class to represent all possible types of transactions.
    '''
    data_types = {'uuid': str, 'user_uuid': str, 'amount': float | int,
                  'note': str | None}

    def __init__(self, **attributes):
        '''
        Constructor

        :param amount: amount of the transaction.
        :param user_uuid: unique identifier of the user associated with this transaction.
        :param date: date of the transaction (default is the current date).
        :param note: any additional notes or comments about this transaction.
        '''
        self.amount = attributes['amount']
        if 'uuid' not in attributes:
            super().__init__()
        else:
            self.__uuid = attributes['uuid']
        self.user_uuid = attributes['user_uuid']
        self.note = attributes.get('note', None)

class Allocation(Transaction):
    '''
    Represents money allocations.
    '''
    data_types = {'uuid': str, 'user_uuid': str, 'date': datetime,
                  'note': str | None, 'target_uuid': str, 'amount': float | int}

    def __init__(self, **attributes):
        '''
        Constructor
        :param target_uuid: unique identifier of the bucket where the money will be allocated.
        '''
        super().__init__(**attributes)
        self.target_uuid = attributes['target_uuid']
        self.date = attributes.get('date', datetime.now())


class Income(Transaction):
    '''
    Represents incomes.
    '''
    data_types = {'uuid': str, 'user_uuid': str, 'note': str | None,
                  'frequency': str, 'start_date': datetime, 'note': str | None,
                  'source': str, 'end_date': None | datetime, 'amount': float | int}
    def __init__(self, **attributes):
        '''
        Constructor
        :param source: source of the income (e.g., "Salary", "Freelance").
        :param frequency: frequency of the income (default is "One-Time").
        :param start_date: date when the income starts (relevant for recurring incomes).
        :param end_date: date when the income ends (can be None if it's indefinite).
        '''
        super().__init__(**attributes)
        self.source = attributes['source']
        self.start_date = attributes.get('start_date', datetime.now())
        self.end_date = attributes.get('end_date', None)
        self.frequency = attributes.get('frequency', 'Unique')


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
