from models.transaction import Income, Allocation
from controllers.model_controller import ModelController
from datetime import datetime


class IncomeController(ModelController):
    '''
    Controller class for managing operations related to Incomes.
    '''
    def __init__(self):
        super().__init__()

    def create_income(self, **attributes):
        """
        Creates a new income.

        Params
        ------
        :param attributes: Keyword arguments representing the attributes of the income.
            attributes include:
                - user_uuid: UUID of the user creating the income.
                - date: Date of the income.
                - note: Optional note for the income.
                - frequency: Frequency of the income.
                - start_date: Start date of the income.
                - source: Source of the income.
                - end_date: Optional end date of the income.
                - amount: Amount of the income.
        Return
        ------
        :return: Newly created income instance.
        """
        return super().create(obj=Income, **attributes)


    def update_income(self, income_uuid, **attributes):
        """
        Update details of a specific income.

        :param income_uuid: UUID of the income to update.
        :param attributes: Updated fields for the income.
        :return: Updated income instance or relevant error.
        """
        return super().update(income_uuid, **attributes)

    def delete_income(self, income_uuid):
        """
        Delete a specific income.
        
        Params
        ------
            :param income_uuid: UUID of the income to delete.
            :type income_uuid: str
        
        Return
        ------
            :return: Confirmation of deletion or relevant error.
            :rtype: str
        """
        return super().delete(income_uuid)

    def retrieve_income(self, income_uuid):
        """
        Retrieve a specific income using its UUID.

        Params
        ------
            :param income_uuid: UUID of the income to retrieve.
            :type income_uuid: str
        
        Return
        ------
            :return: income instance or None if not found.
            :rtype: Income
        """
        return super().retrieve(income_uuid)

    def list_incomes(self, user_uuid:str):
        """
        List all incomes for a specific user.

        Params
        ------
            :param user_uuid: UUID of the user whose incomes to list.
            :type user_uuid: str
        
        Return
        ------
            :return: List of income instances.
            :rtype: list
        """
        return filter(lambda income: income.user_uuid == user_uuid,  self.all)
    
    def next_income(self, user_uuid:str):
        """
        Get the next income of a given user.

        Params
        ------
            :param user_uuid: UUID of the user for whom we want to get the next available income.
            :type user_uuid: str
        
        Return
        ------
            :return: Income instance of the closest next income.
            :rtype: Income
        """
        incomes = self.list_incomes(user_uuid)
        next_income = None
        for income in incomes:
            if next_income is None:
                next_income = income
            elif income.date < next_income.date:
                next_income = income
        return next_income

    def load_instances(self, name='Income', csv='incomes.csv', cls=Income, data_types=Income.data_types):
        return super().load_instances(name, csv, cls, data_types)

    def export_instances(self, load=False):
        return super().export_instances(csv='incomes.csv', cls=Income, load=load)


class AllocationController(ModelController):
    '''
    Controller class for managing operations related to Allocations.
    '''
    def __init__(self):
        super().__init__()

    def create_allocation(self, **attributes):
        """
        Create a new allocation.

        Params
        ------
        :param attributes: Keyword arguments representing the attributes of the allocation.
            attributes include:
                - user_uuid: UUID of the user creating the allocation.
                - date: Date of the allocation.
                - note: Optional note for the allocation.
                - target_uuid: UUID of the target bucket where the money will be allocated.
                
        Return
        ------
        :return: Newly created allocation instance.
        :rtype: Allocation
        """
        return super().create(obj=Allocation, **attributes)

    def update_allocation(self, allocation_uuid, **attributes):
        """
        Update an existing allocation.

        :param allocation_uuid: UUID of the allocation to update.
        :param attributes: Keyword arguments representing the attributes to update.
        """
        return super().update(allocation_uuid, **attributes)

    def delete_allocation(self, allocation_uuid):
        """
        Delete an existing allocation.
        
        Params
        ------
            :param allocation_uuid: UUID of the allocation to delete.
        
        Return
        ------
            :return: Confirmation of deletion or relevant error.
            :rtype: str
        """
        return super().delete(allocation_uuid)

    def retrieve_allocation(self, allocation_uuid):
        """
        Retrieve a specific allocation using its UUID.

        Params
        ------
            :param allocation_uuid: UUID of the allocation to retrieve.
            :type allocation_uuid: str
        
        Return
        ------
            :return: Allocation instance or None if not found.
            :rtype: Allocation
        """
        return super().retrieve(allocation_uuid)

    def retrieve_allocations_by_user(self, user_uuid: str):
        """
        List all allocations for a specific user.

        Params
        ------
            :param user_uuid: UUID of the user whose allocations to list.
            :type user_uuid: str
        
        Return
        ------
            :return: List of allocation instances.
            :rtype: list
        """
        return filter(lambda allocation: allocation.user_uuid == user_uuid, self.all)

    def retrieve_allocations_by_bucket(self, target_uuid: str):
        """
        List all allocations for a specific user.

        :param user_uuid: UUID of the user whose allocations to list.
        :return: List of allocation instances.
        """
        return filter(lambda allocation: allocation.target_uuid == target_uuid, self.all)

    def load_instances(self, name='Allocation', csv='allocations.csv', cls=Allocation, data_types=Allocation.data_types):
        return super().load_instances(name, csv, cls, data_types)

    def export_instances(self, load=False):
        return super().export_instances(csv='allocations.csv', cls=Allocation, load=load)
