from models.model import Model
import pandas as pd
import os
from datetime import datetime
from typing import Union

def convert_type(value, type_):
    '''
    Typecasting function to allow smooth loading of instances from csv files
    
    Params
    ------
        :param value: value to be typecasted
        :type value: str
        :param type_: type to be typecasted to
        :type type_: type
        
    Returns
    -------
        :return: typecasted value
    '''
    if type_ == str:
        return str(value)
    elif type_ == int:
        return int(value)
    elif type_ in [float, float | int]:
        return float(value)
    elif type_ == datetime:
        if value == None:
            return None
        return datetime.fromisoformat(value)

class ModelController:
    """
    Base controller for all model-related actions.

    This class provides foundational methods that can be inherited by more specific controllers.
    Warning: Ensure that when inheriting from this class, override methods if necessary
    to provide specific functionality for the associated model.
    """
    def __init__(self):
        """
        Constructor
        """
        self.load_instances()

    def create(self, obj=Model, **attributes):
        """
        Creating a new instance

        Params
        ------
            :param **attributes: attributes of the model
            :type **attributes: dict
            :param obj: model class to be instantiated
            :type obj: class
        
        Returns
        -------

            :return: Model instance

        Note:
            This method should be overridden in specific controllers if additional functionality or validation
            is needed during the creation of a model instance.
        """
        model = obj(**attributes)
        self.all.append(model)
        return model

    def retrieve(self, model_uuid):
        """
        Retrieves a specific instance of a model based on its UUID.

        Params
        ------
        :param model_uuid: The unique identifier of the model instance.
        :type model_uuid: str

        Returns
        -------
        :return: instance of the model or None if not found.
        :rtype: Model or None
        """
        for instance in self.all:
            if instance.get_id() == model_uuid:
                return instance

    def update(self, model_uuid, **attributes):
        """
        Updates a specific instance of a model based on its UUID.
        This method double-checks whether the attributes
        that are being changed belong to the model in question and raises an
        AttributeError if they aren't.


        Params
        ------
        :param model_uuid: The unique identifier of the model instance.
        :param **attributes: Updated attributes for the model instance.

        Returns
        -------
        Updated model instance or None if not found.
        """
        for model in self.all:
            if model.uuid == model_uuid:
                for key, value in attributes.items():
                    setattr(model, key, value)
                return model

    def delete(self, model_uuid):
        """
        Deletes a specific instance of a model.

        Params
        ------
        :param model_uuid: The unique identifier of the model instance.
        :type model_uuid: str

        Returns
        -------
        :return: True if deletion was successful, False otherwise.
        :rtype: bool
        """
        for model in self.all:
            if model.uuid == model_uuid:
                self.all.remove(model)
                return True

    def list_all(self):
        """
        Lists all instances of a model.

        Returns
        -------
        :return: List of model instances.
        :rtype: list
        """
        return self.all

    def export_instances(self, csv='models.csv', cls=Model, load=False):
        '''
        Class method to export instances to a csv file
        
        Params
        ------
            :param csv: name of the csv file
            :type csv: str
            :param cls: class of the model
            :type cls: class
            :param load: whether to load the instances from the csv file
            :type load: bool
        
        '''
        path_to_file = os.sep.join(['data', csv])
        if not self.all:
            os.remove(path_to_file)
            return
        df = pd.DataFrame([instance.__dict__ for instance in self.all])
        # renaming columns of private attributes
        df.columns = [column.split('__')[-1] for column in df.columns]
        df.drop_duplicates(inplace=True)
        df.to_csv(path_to_file, index=False)
        if load:
            self.load_instances(cls=cls, csv=csv)

    def load_instances(self, name='Model', csv='models.csv',cls=Model, data_types=Model.data_types):
        '''
        Class method to load instances from a csv file and 
        stores them in the all attribute of the controller
        
        Params
        ------
            :param name: name of the class
            :type name: str
            :param csv: name of the csv file
            :type csv: str
            :param cls: class of the model
            :type cls: class
            :param data_types: dictionary of data types of the attributes of the class
            :type data_types: dict
        
        '''
        self.all = []
        # load the csv file
        path_to_file = os.path.join('data', csv)
        ## check if file exists
        if os.path.exists(path_to_file):
            df = pd.read_csv(path_to_file)
            attributes = {column: df[column] for column in df.columns}
            if len(data_types) != len(attributes):
                raise AttributeError
            f"Columns do not match the attributes of the class {name}"
            for i in range(df.shape[0]):
                attributes_instance = {column: values[i] for column, values in attributes.items()}
                attributes_instance = {column: (value if isinstance(value, data_types[column])
                                            else convert_type(value, data_types[column]))
                                        for column, value in attributes_instance.items()}
                model = cls(**attributes_instance)
                self.all.append(model)

if __name__ == '__main__':

    controller = ModelController()
    controller.load_instances()

    for _ in range(10):
        Model()
    for model in controller.list_all():
        print(model.uuid)
    controller.export_instances()
