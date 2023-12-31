from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import date

class MaxValueValidator(object):
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, form, field):
        if field.data is None:
            return
        if float(field.data) > self.max_value:
            raise ValidationError(f'Allocation value can\'t be greater than remaining amount: {self.max_value:.0f}.')

class AllocationForm(FlaskForm):
    """
    Form for creating an allocation
    """
    def __init__(self, max_value, *args, **kwargs):
        super(AllocationForm, self).__init__(*args, **kwargs)
        self.amount.validators.append(MaxValueValidator(max_value))

    amount = StringField('amount', validators=[DataRequired()])
    note = StringField('note')
    date = DateField('Deadline', validators=[DataRequired()], default=date.today)
    submit = SubmitField('create allocation')

class IncomeForm(FlaskForm):
	"""
	Form for creating an income
	"""
	amount = StringField('amount', validators=[DataRequired()])
	frequency = SelectField('frequency', choices=[('unique','non-recurring'),
												  ('weekly', 'weekly'),
												  ('2_weeks', 'biweekly'),
												  ('monthly', 'monthly'),
												  ('quarterly', 'quarterly'),
												  ('half_yearly', 'semi-annual'),
												  ('yearly', 'annually')])
	comment = StringField('comment')
	currency = SelectField('Currency', choices=[('CHF','CHF'),
												('CNY', 'CNY'),
												('EUR', 'EUR'),
												('INR', 'INR'),
												('USD', 'USD')])
	date = DateField('Deadline', validators=[DataRequired()])
	submit = SubmitField('create income')
