from uuid import uuid4


class Model:
    ## define class variable all as an empty list
    all = []
    data_types = {'uuid': str}

    def __init__(self, **attributes):
        '''
        Constructor
        instantiates a model and creates a random UUID (uuid4()) to identify it as a private attribute

        Params
        ------
            :param **attributes: attributes of the model
            :type **attributes: dict
        '''
        self.__uuid = attributes.get('uuid', uuid4())
        if isinstance(self, Model):
            Model.all.append(self)

    @property
    def uuid(self):
        '''
        Getter method to get the UUID of a transaction
        :return: UUID of a given model
        '''
        return str(self.__uuid)

if __name__ == '__main__':
    # Test Case 1: Model instantiation and UUID check
    test_model = Model()
    assert isinstance(test_model, Model), "Error: Unable to instantiate Model class."
    assert isinstance(test_model.uuid, str) and len(test_model.uuid) == 36, "Error: UUID not generated correctly. Ensure it's a string of 36 characters."

    # Test Case 2: UUID privacy check
    try:
        test_model.uuid = "TryingDirectAccess"
        assert False, "Error: Able to directly modify the private '_uuid' attribute. Ensure that it's private and not accessible."
    except AttributeError:
        pass  # This is expected if _uuid is truly private

    print("All tests passed for Model class!")
