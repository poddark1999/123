from models.model import Model
import pandas as pd
import os
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

class ModelController:
    """
    Base controller for all model-related actions.

    This class provides foundational methods that can be inherited by more specific controllers.
    Warning: Ensure that when inheriting from this class, override methods if necessary
    to provide specific functionality for the associated model.
    """

    def __init__(self, cls=Model, name='Model', csv_path='models.csv'):
        self.cls = cls
        self.name = name
        self.__csv_path = csv_path

    def create(self, **kwargs):
        """
        Creates a new instance of a model.

        Args:
            **kwargs: Arguments required to instantiate the model.

        Returns:
            Model instance

        Note:
            This method should be overridden in specific controllers if additional functionality or validation
            is needed during the creation of a model instance.
        """
        pass

    def retrieve(self, model_uuid):
        """
        Retrieves a specific instance of a model based on its UUID.

        Args:
            model_uuid (str): The unique identifier of the model instance.

        Returns:
            Model instance or None if not found.
        """
        pass

    def update(self, model_uuid, **kwargs):
        """
        Updates a specific instance of a model based on its UUID.

        Args:
            model_uuid (str): The unique identifier of the model instance.
            **kwargs: Updated attributes for the model instance.

        Returns:
            Updated model instance or None if not found.
        """
        pass

    def delete(self, model_uuid):
        """
        Deletes a specific instance of a model.

        Args:
            model_uuid (str): The unique identifier of the model instance.

        Returns:
            True if deletion was successful, False otherwise.
        """
        pass

    def list_all(self):
        """
        Lists all instances of a model.

        Returns:
            List of model instances.
        """
        return self.cls.all

    def export_instances(self):
        '''
        Class method to export instances to a csv file

        '''
        path_to_file = os.sep.join(['data', self.__csv_path])
        df = pd.DataFrame([instance.__dict__ for instance in self.cls.all])
        # renaming columns of private attributes
        df.columns = [column.split('__')[-1] for column in df.columns]
        df.to_csv(path_to_file, index=False)

    def load_instances(self):
        '''
        Class method to load instances from a csv file

        '''
        # load the csv file
        path_to_file = os.path.join('data', self.__csv_path)
        ## check if file exists
        if os.path.exists(path_to_file):
            df = pd.read_csv(path_to_file)
            attributes = {column: df[column] for column in df.columns}
            if len(self.cls.data_types) != len(attributes):
                raise AttributeError
            f"Columns do not match the attributes of the class {self.name}"
            for i in range(df.shape[0]):
                attributes_instance = {column:values[i] for column, values in attributes.items()}
                attributes_instance = {column: (value if isinstance(value, self.cls.data_types[column])
                                            else convert_type(value, self.cls.data_types[column]))
                                        for column, value in attributes_instance.items()}
                Model(**attributes_instance)

if __name__ == '__main__':

    controller = ModelController()
    controller.load_instances()

    for _ in range(10):
        Model()
    for model in controller.list_all():
        print(model.uuid)
    controller.export_instances()
