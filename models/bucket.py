from model import Model
from datetime import datetime


class Bucket(Model):
    '''
    The Bucket class models the goals that a user aims to attain, represented as "buckets".
    Each bucket has a financial target amount, a deadline, a user_UUID,
    a current_amount (standing for the amount which has already been allocated)
    and additional meta information.
    '''

    def __init__(self, name, goal, user_uuid, deadline, current_amount=0, comment=None):
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

        :param current_amount: Amount which has already been allocated to the bucket
        :type current_amount: integer, default is 0

        :param comment: Optional comment or note about the bucket
        :type comment: str, default is None

        Additionally, upon creation of a bucket, an attribute creation_date
        records when a bucket is created and an attribute completed to track the status.
        '''

        # Private attributes: creation_date, is_completed, current_amount
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
        # The string format of the date should be in the format DD.MM.YYYY
        pass

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
    # Test Case 1: Bucket instantiation and UUID check
    test_bucket = Bucket(name="Test Bucket", goal=100, user_uuid="sample_uuid", deadline=datetime(2023, 12, 31))
    assert isinstance(test_bucket, Bucket), "Error: Unable to instantiate Bucket class."
    assert isinstance(test_bucket.uuid, str) and len(test_bucket.uuid) == 36, "Error: UUID not generated correctly. Ensure it's a string of 36 characters."
    print("Bucket instantiation test passed!")

    # Test Case 2: creation_date privacy check
    try:
        test_value = test_bucket.__creation_date
        assert False, "Error: Able to directly access the private '_creation_date' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome
    print("Privacy test passed for creation_date!")

    # Test Case 3: is_completed privacy check
    try:
        test_value = test_bucket.__is_completed
        assert False, "Error: Able to directly access the private '_is_completed' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome
    print("Test Case privacy is_completed passed!")

    # Test Case 4: current_amount privacy check
    try:
        test_value = test_bucket.__current_amount
        assert False, "Error: Able to directly access the private '_current_amount' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # Expected outcome
    print("Test Case privacy current_amount passed!")
    print("Privacy tests passed!"")

    # Test Case 5: creation_date type check & getter check
    assert isinstance(test_bucket.creation_date, datetime), "Error: 'creation_date' should be of type datetime when accessed without specifying type."
    assert isinstance(test_bucket.creation_date(type="str"), str), "Error: 'creation_date' should return string when type='str'."
    assert len(test_bucket.creation_date(type="str").split('.')) == 3, "Error: The string format of the creation date should be in the format DD.MM.YYYY."
    print("Test Case 5 passed!")

    # Test Case 6: Goal achievement check using is_completed and mark_as_completed
    assert not test_bucket.is_completed, "Error: Bucket should not be marked as completed when instantiated with a goal greater than current_amount."
    test_bucket.mark_as_completed()
    assert test_bucket.is_completed, "Error: Bucket should be marked as completed after calling the mark_as_completed method."
    print("Test Case 6 passed!")

    # Test Case 7: Type checks for attributes
    assert isinstance(test_bucket.name, str), "Error: 'name' attribute should be of type string."
    assert isinstance(test_bucket.goal, (int, float)), "Error: 'goal' attribute should be of type int or float."
    assert isinstance(test_bucket.user_uuid, str), "Error: 'user_uuid' attribute should be of type string."
    assert isinstance(test_bucket.deadline, datetime), "Error: 'deadline' attribute should be of type datetime."
    assert isinstance(test_bucket.comment, (str, type(None))), "Error: 'comment' attribute should be of type string or None."
    print("Type checks passed!")

    print("All tests passed for Bucket class!")

