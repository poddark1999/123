from model import Model

def is_strong(password):
    '''
    Function to check if a password is strong enough
    Requirements for a strong password:
    - Must contain at least an uppercase letter
    - Must contain at least a lowercase letter
    - Must contain at least a number
    - Must contain at least a special character (!@#$%{}[]&*<>?+=,./)
    - Must contain between 8-30 characters

    Params
    ------
        :param password: a potential password
        :type password: str

    Return
    ------
        :return: Is the password strong enough
        :rtype: bool
    '''
    pass


class User(Model):
    '''
    The User class will allow us to model users as well as link the other
    components together
    '''

    def __init__(self, first_name, last_name, username, password):
        '''
        Constructor method

        Params
        ------
            :param first_name: first name of user
		    :type first_name: str
            :param last_name: last name of user
		    :type last_name: str
            :param username: username of user
		    :type username: str
            :param password: strong password (strength can be checked with is_strong)
		    :type password: str
        '''
        pass

    def check_password(self, password):
        '''
        Check if the provided password matches the stored one.

        Params
        ------
            :param password: Password to check
            :type password: str

        Return
        ------
            :return: True if the password matches, otherwise False
            :rtype: bool
        '''
        pass

    def change_password(self, old_password, new_password):
        '''
        Method to change password of a given user
        Replaces the user's old password with a new one provided that:
        - The user provides the correct former passport
        - The user provides a new strong password (can be checked with is_strong)

        Params
        ------
            :param old_password: is equal to User.password
            :type old_password: str
            :param new_password: new strong password
            :type new_password: str
        '''
        pass


if __name__ == '__main__':
    # Tests for is_strong function
    test_cases = [
        ("Password123!", True,
         "A strong password with uppercase, lowercase, number, and special character"
         ),
        ("password123!", True,
         "A strong password with lowercase, number, and special character but no uppercase"
         ),
        ("PASSWORD123!", True,
         "A strong password with uppercase, number, and special character but no lowercase"
         ), ("Password123", False, "Missing special character"),
        ("Password!", False, "Missing number"),
        ("password123!", False, "Missing uppercase letter"),
        ("PASSWORD123!", False, "Missing lowercase letter"),
        ("Pass1!", False, "Too short"), ("a" * 31 + "!", False, "Too long"),
        ("", False, "Empty password")
    ]

    for i, (pwd, expected, msg) in enumerate(test_cases, 1):
        result = is_strong(pwd)
        assert result == expected, f"Test {i} failed for password: '{pwd}' - {msg}"
        print(f"Test {i} for is_strong passed!")

    # Test User Creation
    user = User("John", "Doe", "johndoe", "Password123!")
    print("User creation test passed!")

    # Test Attribute Types
    assert isinstance(user.first_name,
                      str), "first_name attribute type test failed!"
    assert isinstance(user.last_name,
                      str), "last_name attribute type test failed!"
    assert isinstance(user.username,
                      str), "username attribute type test failed!"
    print("User attributes type test passed!")

    # Test Privacy
    try:
        user._password
    except AttributeError:
        print("Password attribute privacy test passed!")
    else:
        assert False, "Password attribute should be private and not directly accessible."

    # Test password check method
    assert user.check_password(
        "Password123!") == True, "Password check test failed!"
    print("Password check test passed!")

    # Test change password method
    try:
        user.change_password("WrongPassword123!", "NewPassword123!")
    except ValueError as e:
        assert str(
            e
        ) == "The provided old password is incorrect.", f"Unexpected error message: {e}"
        print("Password change with wrong old password test passed!")
    else:
        assert False, "change_password should raise an error for wrong old password."

    try:
        user.change_password("Password123!", "Short!")
    except ValueError as e:
        assert str(
            e
        ) == "The new password is not strong enough.", f"Unexpected error message: {e}"
        print("Password change with weak new password test passed!")
    else:
        assert False, "change_password should raise an error for weak new password."

    user.change_password("Password123!", "NewPassword123!")
    assert user.check_password(
        "NewPassword123!") == True, "Password change test failed!"
    print("Password change test passed!")
