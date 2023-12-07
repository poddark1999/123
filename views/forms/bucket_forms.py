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
	deadline = DateField('Deadline', validators=[DataRequired()])
	comment = StringField('Comment')
	frequency = SelectField('Frequency', choices=[('unique','non-recurring'),
     											  ('weekly', 'weekly'),
												  ('2_weeks', 'biweekly'),
												  ('monthly', 'monthly'),
												  ('quarterly', 'quarterly'),
												  ('half_yearly', 'semi-annual'),
												  ('yearly', 'annually')])

	icon = SelectField('Category', choices=[('🎓', '🎓Education'),
												 ('🏥', '🏥Medical'),
												 ('🥎', '🥎Sports'),
												 ('✈️', '✈️Travel'),
												 ('💻', '💻Technology'),
												 ('🏠', '🏠House'),
												 ('💸', '💸Taxes')])
	submit = SubmitField('Create')

	def validate_deadline(self, deadline):
		"""
		Checks if the deadline is in the future
		"""
		if deadline.data < datetime.now().date():
			raise ValidationError('Deadline must be in the future')

	def validate_frequency(self, frequency):
		"""
		Checks if the frequency is valid
		"""
		if frequency.data not in Bucket.valid_frequencies:
			raise ValidationError(f"Invalid frequency: {frequency.data}. \
Must be one of {', '.join([key for key in Bucket.valid_frequencies])}")


