from models.model import Model
from models.user import User, is_strong
from controllers.model_controller import ModelController


class UserController(ModelController):
    '''
    Controller for the User model.
    Manages operations related to the User.
    '''

    def __init__(self, cls=User, name='User', csv_path='users.csv'):
        super().__init__(cls, name, csv_path)

    def export_instances(self):
        return super().export_instances()

    def import_instances(self):
        return super().import_instances()

    @staticmethod
    def create_user(first_name, last_name, username, password):
        '''
        Creates a new User object if the provided password is strong enough.

        Params:
        - first_name: str - First name of the user.
        - last_name: str - Last name of the user.
        - username: str - Username chosen by the user.
        - password: str - Password chosen by the user.

        Returns:
        - User object if successfully created, None otherwise.
        '''
        if is_strong(password):
            return User(first_name=first_name, last_name=last_name,
                        username=username, password=password)
        raise Exception('Password is not strong enough')

    @staticmethod
    def change_user_password(user, old_password, new_password):
        '''
        Changes the password of a given User object if old_password matches
        the current password and new_password is strong enough.

        Params:
        - user: User - The user whose password needs to be changed.
        - old_password: str - The old/current password of the user.
        - new_password: str - The new password user wants to set.

        Returns:
        - bool: True if password is successfully changed, False otherwise.
        '''
        # The actual logic will involve checking user's current password
        # and using the User's instance method to change the password if conditions are met.
        pass

    @staticmethod
    def check_login(username, password):
        for user in User.all:
            if user.username == user.password:
                return True
        return False
    # Additional methods related to user can be added here.


if __name__ == '__main__':
    pass

