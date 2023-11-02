from datetime import datetime
from model import Model
from user import User


class Transaction(Model):
    '''
    Class to represent all possible types of transactions.
    '''

    def __init__(self, amount, user_uuid, date=datetime.now(), note=None):
        '''
        Constructor
        :param amount: amount of the transaction.
        :param user_uuid: unique identifier of the user associated with this transaction.
        :param date: date of the transaction (default is the current date).
        :param note: any additional notes or comments about this transaction.
        '''
        pass


class RecurringExpense(Transaction):
    '''
    Represents recurring expenses.
    '''

    def __init__(self, frequency, start_date=datetime.now(), expiry_date=None, is_paused=False):
        '''
        Constructor
        :param frequency: frequency of the expense (daily/weekly/monthly/yearly).
        :param start_date: starting date of the recurring expense.
        :param expiry_date: end date of the recurring expense. Can be None if it's indefinite.
        :param is_paused: boolean to indicate if the recurring expense is currently paused.
        '''
        pass


class Allocation(Transaction):
    '''
    Represents money allocations.
    '''

    def __init__(self, target_uuid):
        '''
        Constructor
        :param target_uuid: unique identifier of the bucket where the money will be allocated.
        '''
        pass


class Income(Transaction):
    '''
    Represents incomes.
    '''

    def __init__(self, source, frequency="One-Time", start_date=datetime.now(), end_date=None):
        '''
        Constructor
        :param source: source of the income (e.g., "Salary", "Freelance").
        :param frequency: frequency of the income (default is "One-Time").
        :param start_date: date when the income starts (relevant for recurring incomes).
        :param end_date: date when the income ends (can be None if it's indefinite).
        '''
        pass


if __name__ == '__main__':
    # Create a User object
    u = User("John", "Doe", "johndoe", "StrongPass123!")
    user_uuid = u.uuid  # Assuming User class has a uuid attribute

    # Test if Transaction and derived classes correctly inherit from Model
    t = Transaction(100, user_uuid)
    re = RecurringExpense(100, user_uuid, "daily")
    a = Allocation(100, user_uuid, user_uuid)
    i = Income(100, user_uuid, "Salary")

    assert isinstance(t,
                      Model), "Transaction class does not inherit from Model!"
    assert isinstance(
        re, Model), "RecurringExpense class does not inherit from Model!"
    assert isinstance(a,
                      Model), "Allocation class does not inherit from Model!"
    assert isinstance(i, Model), "Income class does not inherit from Model!"
    print("Inheritance tests passed!")

    # Test attribute types
    assert isinstance(
        t.amount,
        (int, float)), "Transaction amount is not of type int or float!"
    assert isinstance(
        re.amount,
        (int, float)), "RecurringExpense amount is not of type int or float!"
    assert isinstance(
        a.amount,
        (int, float)), "Allocation amount is not of type int or float!"
    assert isinstance(
        i.amount, (int, float)), "Income amount is not of type int or float!"
    print("Attribute type tests for 'amount' passed!")

    # Test privacy of relevant attributes
    try:
        t.amount
        raise AssertionError("Transaction amount is not private!")
    except AttributeError:
        pass

    # Test other behaviors, like the correct default assignment, etc.
    assert t.date == datetime.now(), "Transaction date not correctly assigned!"
    assert i.frequency == "One-Time", "Income frequency default value not correctly assigned!"
    print("Default assignment tests passed!")

    print("All tests passed!")