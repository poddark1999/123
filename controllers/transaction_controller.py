from models.transaction import Income, Allocation
from controllers.model_controller import ModelController
from datetime import datetime


class IncomeController(ModelController):
    '''
    Controller class for managing operations related to Incomes.
    '''
    def __init__(self):
        super().__init__()

    def create_income(self, user_uuid: str, date: float | int,
                  note: str | None, frequency: str, start_date: datetime,
                  source: str, end_date: None | datetime, amount: float | int):
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
        income = Income(user_uuid=user_uuid, note=note, frequency=frequency,
                        start_date=start_date, source=source, end_date=end_date)
        self.all.append(income)


    def update_income(self, income_uuid, **kwargs):
        """
        Update details of a specific income.

        :param income_uuid: UUID of the income to update.
        :param kwargs: Updated fields for the income.
        :return: Updated income instance or relevant error.
        """
        for income in self.all:
            if income.uuid == income_uuid:
                for key, value in kwargs.items():
                    setattr(income, key, value)
                return income

    def delete_income(self, income_uuid):
        """
        Delete a specific income.

        :param income_uuid: UUID of the income to delete.
        :return: Confirmation of deletion or relevant error.
        """
        for income in self.all:
            if income.uuid == income_uuid:
                self.all.remove(income)
                return True

    def retrieve_income(self, income_uuid):
        """
        Retrieve a specific income using its UUID.

        :param income_uuid: UUID of the income to retrieve.
        :return: income instance or None if not found.
        """
        for income in self.all:
            if income.uuid == income_uuid:
                return income

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

    def create_allocation(self, user_uuid: str, date: datetime,
                  note: str | None, target_uuid: str, amount: float | int):
        """
        Create a new allocation.

        :param user_uuid: UUID of the user creating the allocation.
        :param date: Date of the allocation.
        :param note: Optional note for the allocation.
        :param target_uuid: UUID of the target bucket where the money will be allocated.
        :return: The created allocation instance.
        """
        allocation = Allocation(user_uuid=user_uuid, date=date,
                                note=note, target_uuid=target_uuid,
                                amount=amount)
        self.all.append(allocation)
        return allocation

    def update_allocation(self, allocation_uuid, **kwargs):
        """
        Update an existing allocation.

        :param allocation_uuid: UUID of the allocation to update.
        :param kwargs: Keyword arguments representing the attributes to update.
        """
        allocation = self.retrieve_allocation(allocation_uuid)
        if allocation:
            for key, value in kwargs.items():
                setattr(allocation, key, value)

    def delete_allocation(self, allocation_uuid):
        """
        Delete an existing allocation.

        :param allocation_uuid: UUID of the allocation to delete.
        """
        allocation = self.retrieve_allocation(allocation_uuid)
        if allocation:
            self.all.remove(allocation)

    def retrieve_allocation(self, allocation_uuid):
        """
        Retrieve a specific allocation using its UUID.

        :param allocation_uuid: UUID of the allocation to retrieve.
        :return: Allocation instance or None if not found.
        """
        for allocation in self.all:
            if allocation.uuid == allocation_uuid:
                return allocation

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
