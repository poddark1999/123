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
        :param user_uuid: UUID of the user who owns the income.
        :param date: Date of the income.
        :param note: Optional note about the income.
        :param frequency: Frequency of the income.
        :param start_date: Start date of the income.
        :param source: Source of the income.
        :param end_date: Optional end date of the income.
        :param amount: Amount of the income.

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

        :param income_uuid: UUID of the income to delete.
        :return: Confirmation of deletion or relevant error.
        """
        return super().delete(income_uuid)

    def retrieve_income(self, income_uuid):
        """
        Retrieve a specific income using its UUID.

        :param income_uuid: UUID of the income to retrieve.
        :return: income instance or None if not found.
        """
        return super().retrieve(income_uuid)

    def list_incomes(self, user_uuid:str):
        """
        List all incomes for a specific user, optionally filtered by date range.

        :param user_uuid: UUID of the user whose incomes to list.
        :param start_date: Optional start date to filter incomes.
        :param end_date: Optional end date to filter incomes.
        :return: List of income instances.
        """
        return filter(lambda income: income.user_uuid == user_uuid,  self.all)

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

        :param user_uuid: UUID of the user creating the allocation.
        :param date: Date of the allocation.
        :param note: Optional note for the allocation.
        :param target_uuid: UUID of the target bucket where the money will be allocated.
        :return: The created allocation instance.
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

        :param allocation_uuid: UUID of the allocation to delete.
        """
        return super().delete(allocation_uuid)

    def retrieve_allocation(self, allocation_uuid):
        """
        Retrieve a specific allocation using its UUID.

        :param allocation_uuid: UUID of the allocation to retrieve.
        :return: Allocation instance or None if not found.
        """
        return super().retrieve(allocation_uuid)

    def retrieve_allocations_by_user(self, user_uuid: str):
        """
        List all allocations for a specific user.

        :param user_uuid: UUID of the user whose allocations to list.
        :return: List of allocation instances.
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
