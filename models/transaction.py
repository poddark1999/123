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
        super().__init__()

        if not isinstance(amount, (int,float)):
            raise ValueError('Amount must be an integer or float')
        self.__amount = float(amount)

        self.user_uuid = user_uuid
        self.date = date
        self.note = note

    @property
    def amount(self):
        return self.__amount



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

    def __init__(self, amount, user_uuid, target_uuid, date=datetime.now(), note=None ):
        '''
        Constructor
        :param target_uuid: unique identifier of the bucket where the money will be allocated.
        '''
        super().__init__(amount, user_uuid, date, note)
        self.target_uuid = target_uuid


class Income(Transaction):
    '''
    Represents incomes.
    '''

    def __init__(self,amount,user_uuid, source, frequency="One-Time", start_date=datetime.now(), end_date=None):
        '''
        Constructor
        :param source: source of the income (e.g., "Salary", "Freelance").
        :param frequency: frequency of the income (default is "One-Time").
        :param start_date: date when the income starts (relevant for recurring incomes).
        :param end_date: date when the income ends (can be None if it's indefinite).
        '''
        super().__init__(amount, user_uuid)
        self.source = source
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date



if __name__ == '__main__':
    # Create a User object
    u = User("John", "Doe", "johndoe", "StrongPass123!")
    user_uuid = u.uuid  # Assuming User class has a uuid attribute

    # Capture the current time before creating the Transaction object
    current_time = datetime.now()
    # Test if Transaction and derived classes correctly inherit from Model
    t = Transaction(100, user_uuid, date=current_time)
    #re = RecurringExpense(100, user_uuid, "daily")
    a = Allocation(100, user_uuid, "transaction-bucket-id")
    i = Income(100, user_uuid, "Salary")

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
        assert False, "Transaction amount is private as expected!"

    # Test other behaviors, like the correct default assignment, etc.
    assert t.date == current_time, "Transaction date not correctly assigned!"
    assert i.frequency == "One-Time", "Income frequency default value not correctly assigned!"
    print("Default assignment tests passed!")

    print("All tests passed!")
