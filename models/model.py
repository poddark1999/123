from uuid import uuid4

class Model:

    def __init__(self):
        '''
        Constructor
        instantiates a model and creates a random UUID (uuid4()) to identify it as a private attribute
        '''
        pass

    @property

    def uuid(self):
        '''
        Getter method to get the UUID of a transaction
        :return: UUID of a given model
        '''
        pass
