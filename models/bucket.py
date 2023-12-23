from models.model import Model
from datetime import datetime
from datetime import timedelta

from typing import Union

class Bucket(Model):
    '''
    The Bucket class models the goals that a user aims to attain, represented as "buckets".
    Each bucket has a financial target amount, a deadline, a user_UUID,
    a current_amount (standing for the amount which has already been allocated)
    and additional meta information.
    '''
    data_types = {'uuid': str, 'name': str, 'goal': float | int,
                  'user_uuid': str, 'deadline': datetime, 'creation_date': datetime,
                  'current_amount': float | int, 'comment':str | None,
                   'frequency':str | None, 'complete':bool, 'icon': str | None}

    valid_frequencies = {"unique": None,
                         "weekly": timedelta(days=7),
                         "2_weeks": timedelta(weeks=2),
                         "monthly": timedelta(days=30),
                         "quarterly": timedelta(days=91),
                         "half_yearly" : timedelta(days=180),
                         "annually": timedelta(days=365)}

    def __init__(self, **attributes):
        '''
        Constructor method

        Params
        ------
            :param **attributes: attributes of the bucket
            :type **attributes: dict

        Additionally, upon creation of a bucket, an attribute creation_date
        records when a bucket is created and an attribute completed to track the status.
        '''
        self.name = attributes['name']
        self.goal = attributes['goal']
        self.user_uuid = attributes['user_uuid']
        self.deadline = attributes['deadline']
        self.current_amount = attributes.get('current_amount', 0)
        self.comment = attributes.get('comment', None)
        self.complete = False
        self.icon = attributes.get('icon', None)
        self.currency = attributes.get('currency', 'EUR')
        self.creation_date = attributes.get('creation_date', datetime.now())
        #create a list of accepted frequencies
        self.frequency = attributes.get('frequency',None)
        if self.frequency not in Bucket.valid_frequencies and self.frequency != None:
            raise ValueError(f"Invalid frequency: {self.frequency}. \
Must be one of {', '.join([key for key in Bucket.valid_frequencies])}")
        if 'uuid' not in attributes:
            super().__init__()
        else:
            self.uuid = attributes['uuid']

    def creation_date(self, type_="date"): ## "date", "05.10.2022"
        '''
        Getter method for the date a bucket was created

        Params
        ------
        :param type_: String defining the type of return.
                     Can be "date" for datetime object or "str" for string.
                     Default is "date".
        :type type_: str

        Return
        ------
        :return: Date the bucket was created
        :rtype: datetime object or str
        '''
        # TODO: Implement method to return the creation date based on the type parameter
        # The string format of the date should be in the format DD.MM.YYYY
        # "05.10.2022" - > datetime(05, 10, 2022)
        if type_ == "date": # 判斷輸進去的格式是不是 datetime.datetime
            return self.__creation_date
        else:
            return self.__creation_date.strftime("%d.%m.%Y")

    @property
    def is_completed(self):
        '''
        Getter method to check if a bucket's goal has been achieved.
        If the value for the attribute is_completed is False, checks
        if the current_amount is greater than or equal to the goal before returning False
        and updates the value using the mark_as_completed method.

        Return
        ------
        :return: Status of bucket's goal completion
        :rtype: bool
        '''

        if not self.complete:
            if self.current_amount >= self.goal:
                self.__mark_as_completed()
        return self.complete

    def __mark_as_completed(self):
        '''
        Method to set the bucket's goal as achieved

        Return
        ------
        :return: None
        '''
        self.complete = True

    def update_deadline(self):
        '''
        Method to check if the deadline for a bucket has passed.
        If the bucket is recurrent, the deadline is updated to the next deadline,
        based on the attribute frequency.

        '''
        current_datetime = datetime.now()
        if (self.frequency is not None) and (self.deadline < current_datetime):
            self.deadline += Bucket.valid_frequencies[self.frequency]


if __name__ == '__main__':
    # Test Case 1: Bucket instantiation and UUID check
    test_bucket = Bucket(name="Test Bucket", goal=100, user_uuid="sample_uuid", deadline=datetime(2023, 12, 31), frequency='weekly')
    assert isinstance(test_bucket, Bucket), "Error: Unable to instantiate Bucket class."
    assert isinstance(test_bucket.uuid, str) and len(test_bucket.uuid) == 36, "Error: UUID not generated correctly. Ensure it's a string of 36 characters."
    print("Test Case 1 passed!")

    # Test Case 2: creation_date privacy check
    try:
        test_value = test_bucket._creation_date
        assert False, "Error: Able to directly access the private '_creation_date' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome
    print("Test Case 2 passed!")

    # Test Case 3: is_completed privacy check
    try:
        test_value = test_bucket._is_completed
        assert False, "Error: Able to directly access the private '_is_completed' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome
    print("Test Case 3 passed!")

    # Test Case 4: current_amount privacy check
    try:
        test_value = test_bucket._current_amount
        assert False, "Error: Able to directly access the private '_current_amount' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome

    print("Test Case 4 passed!")
    print("Test Case privacy current_amount passed!")
    print("Privacy tests passed!")


    # Test Case 5: creation_date type check & getter check
    assert isinstance(test_bucket.creation_date(), datetime), "Error: 'creation_date' should be of type datetime when accessed without specifying type."
    assert isinstance(test_bucket.creation_date(type_="str"), str), "Error: 'creation_date' should return string when type='str'."
    assert len(test_bucket.creation_date(type_="str").split('.')) == 3, "Error: The string format of the creation date should be in the format DD.MM.YYYY."
    print("Test Case 5 passed!")

    # Test Case 6: Goal achievement check using is_completed and mark_as_completed
    assert not test_bucket.is_completed, "Error: Bucket should not be marked as completed when instantiated with a goal greater than current_amount."
    try:
        test_bucket.mark_as_completed()
    except AttributeError:
        print("Mark as completed is private")
    test_bucket.current_amount = 100
    assert test_bucket.is_completed, "Error: Bucket should be marked as completed after calling the mark_as_completed method."
    print("Test Case 6 passed!")

    # Test Case 7: Type checks for attributes
    assert isinstance(test_bucket.name, str), "Error: 'name' attribute should be of type string."
    assert isinstance(test_bucket.goal, (int, float)), "Error: 'goal' attribute should be of type int or float."
    assert isinstance(test_bucket.user_uuid, str), "Error: 'user_uuid' attribute should be of type string."
    assert isinstance(test_bucket.deadline, datetime), "Error: 'deadline' attribute should be of type datetime."
    assert isinstance(test_bucket.comment, (str, type(None))), "Error: 'comment' attribute should be of type string or None."
    print("Test Case 7 passed!")

    print("All tests passed for Bucket class!")
