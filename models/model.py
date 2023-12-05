from uuid import uuid4


class Model:
    ## define class variable all as an empty list
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
        self.uuid = attributes.get('uuid', uuid4())

    def get_id(self):
        return self.uuid

if __name__ == '__main__':
    # Test Case 1: Model instantiation and UUID check
    test_model = Model()
    assert isinstance(test_model, Model), "Error: Unable to instantiate Model class."
    assert isinstance(test_model.uuid, str) and len(test_model.uuid) == 36, "Error: UUID not generated correctly. Ensure it's a string of 36 characters."

    print("All tests passed for Model class!")
