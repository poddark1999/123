from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime
from models.bucket import Bucket

class BucketForm(FlaskForm):
	"""
	Form for creating a bucket
	"""
	name = StringField('Name', validators=[DataRequired()])
	goal = FloatField('Goal', validators=[DataRequired()])
	currency = SelectField('Currency', choices=[('CHF','CHF'),
												('CNY', 'CNY'),
												('EUR', 'EUR'),
												('INR', 'INR'),
												('USD', 'USD')])
	deadline = DateField('Deadline', validators=[DataRequired()])
	comment = StringField('Comment')
	frequency = SelectField('Frequency', choices=[('non-recurring','non-recurring'),
												  ('weekly', 'weekly'),
												  ('biweekly', 'biweekly'),
												  ('monthly', 'monthly'),
												  ('quarterly', 'quarterly'),
												  ('semi-annually', 'semi-annually'),
												  ('yearly', 'yearly')])
	icon = StringField('Icon', validators=[DataRequired()])
	submit = SubmitField('Create')

	def validate_deadline(self, deadline):
		"""
		Checks if the deadline is in the future
  
		Params
		------
			:param deadline: DateField
				The deadline of the bucket

		Raises
		------
			ValidationError
				If the deadline is not in the future
		"""
		if deadline.data < datetime.now().date():
			raise ValidationError('Deadline must be in the future')

	def validate_frequency(self, frequency):
		"""
		Checks if the frequency is valid
  
		Params
		------
			:param frequency: SelectField
				The frequency of the bucket
   
		Raises
		------
			ValidationError
				If the frequency is not valid
		"""
		if frequency.data not in Bucket.valid_frequencies:
			raise ValidationError(f"Invalid frequency: {frequency.data}. \
Must be one of {', '.join([key for key in Bucket.valid_frequencies])}")


