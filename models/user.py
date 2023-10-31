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
        ## TO DO
        ## Private attributes: password
        ## Should raise an error if the password is not strong enough
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
    pass
