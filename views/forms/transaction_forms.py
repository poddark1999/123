from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import date

class MaxValueValidator(object):
    """
    Validator that checks if the value is less than or equal to the max_value
    """
    def __init__(self, max_value):
        """
        Constructor for the MaxValueValidator class
        
        Params
        ------
        	:param max_value: float
				The maximum value allowed
   		"""
        self.max_value = max_value

    def __call__(self, form, field):
        """
        Checks if the value is less than or equal to the max_value
        
        Params
        ------
			:param form: FlaskForm
				The form the field belongs to
			:param field: StringField
				The field to validate
		
		Raises
		------
			ValidationError
				If the value is greater than the max_value
		"""
        if field.data is None:
            return
        if float(field.data) > self.max_value:
            raise ValidationError(f'Allocation value can\'t be greater than remaining amount: {self.max_value:.0f}.')

class AllocationForm(FlaskForm):
    """
    Form for creating an allocation
    """
    def __init__(self, max_value, *args, **kwargs):
        """
        Constructor for the AllocationForm class
        
        Params
        ------
			:param max_value: float
				The maximum value allowed
			:param *args: list
				Positional Arguments for the FlaskForm constructor
			:param **kwargs: dict
				Keyword Arguments for the FlaskForm constructor
   		"""
        super(AllocationForm, self).__init__(*args, **kwargs)
        if not any(isinstance(v, MaxValueValidator) for v in self.amount.validators):
            self.amount.validators.append(MaxValueValidator(max_value))

    amount = StringField('amount', validators=[DataRequired()])
    note = StringField('note')
    date = DateField('date', validators=[DataRequired()], default=date.today)
    submit = SubmitField('create allocation')

class IncomeForm(FlaskForm):
	"""
	Form for creating an income
	"""
	source = StringField('source', validators=[DataRequired()])
	amount = StringField('amount', validators=[DataRequired()])
	frequency = SelectField('frequency', choices=[('non-recurring','non-recurring'),
												  ('weekly', 'weekly'),
												  ('biweekly', 'biweekly'),
												  ('monthly', 'monthly'),
												  ('quarterly', 'quarterly'),
												  ('semi-annual', 'semi-annual'),
												  ('yearly', 'yearly')])
	note = StringField('comment')
	currency = SelectField('currency', choices=[('CHF','CHF'),
												('CNY', 'CNY'),
												('EUR', 'EUR'),
												('INR', 'INR'),
												('USD', 'USD')])
	start_date = DateField('start date', validators=[DataRequired()])
	end_date = DateField('end date', validators=[DataRequired()])
	submit = SubmitField('create income')
