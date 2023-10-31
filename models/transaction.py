from datetime import datetime
from model import Model


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
    pass
