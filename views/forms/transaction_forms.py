from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AllocationForm(FlaskForm):
	"""
	Form for creating an allocation
	"""
	amount = StringField('amount', validators=[DataRequired()])
	note = StringField('note')
	date = DateField('Deadline', validators=[DataRequired()])
	submit = SubmitField('create allocation')

class IncomeForm(FlaskForm):
	"""
	Form for creating an income
	"""
	amount = StringField('amount', validators=[DataRequired()])
	frequency = SelectField('Frequency', choices=[('unique','non-recurring'),
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
