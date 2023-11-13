from uuid import uuid4

import os
import pandas as pd
from datetime import datetime

def convert_type(value, type_):
    '''
    Typecasting function
    '''
    if type_ == str:
        return str(value)
    elif type_ == int:
        return int(value)
    elif type_ == float:
        return float(value)
    elif type == datetime:
        return datetime.fromisoformat(value)

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
        if not attributes:
            self.__uuid = uuid4()
        else:
            self.__uuid = attributes['uuid']
        Model.all.append(self)

    """@classmethod
    def load_instances(cls):
        '''
        Class method to load instances from a csv file

        Params
        ------
            :param csv_path: path to the csv file
            :param name: name of the class
        '''
        # load the csv file
        path_to_file = os.path.join('data', cls.csv_path)
        ## check if file exists
        if os.path.exists(path_to_file):
            df = pd.read_csv(path_to_file)
            attributes = {column: df[column] for column in df.columns}
            if len(Model.data_types) != len(attributes):
                raise AttributeError
            f"Columns do not match the attributes of the class {cls.name}"
            for i in range(df.shape[0]):
                attributes_instance = {column:values[i] for column, values in attributes.items()}
                attributes_instance = {column: (value if isinstance(value, cls.data_types[column])
                                            else convert_type(value, cls.data_types[column]))
                                        for column, value in attributes_instance.items()}
                Model(**attributes_instance)

    @classmethod
    def export_instances(cls):
        '''
        Class method to export instances to a csv file

        :param csv_path: path to a csv file
        :type csv_path: str
        '''
        path_to_file = os.sep.join(['data', cls.csv_path])
        df = pd.DataFrame([instance.__dict__ for instance in cls.all])
        # renaming columns of private attributes
        df.columns = [column.replace(f'_{cls.name}__', '') for column in df.columns]
        df.to_csv(path_to_file, index=False)
    """
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

    #print(test_model.uuid)
    # Test Case 3: Load instances from csv file
    """
    Model.load_instances()
    for _ in range(10):
        Model()
    for model in Model.all:
        print(model.uuid)
    Model.export_instances()
    """
