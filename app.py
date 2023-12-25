from flask import render_template, flash, redirect, url_for, Flask, session
from flask_login import login_required, login_user, logout_user, LoginManager, current_user
from datetime import timedelta
from views.visualizations.bucket_visualization import bucket_completion
from controllers.bucket_controller import BucketController
from controllers.user_controller import UserController
from controllers.transaction_controller import IncomeController, AllocationController
from views.forms.user_forms import LoginForm, RegisterForm
from views.forms.bucket_forms import BucketForm
from views.forms.transaction_forms import AllocationForm, IncomeForm
from views.static.utils import format_thousands, format_date

uc = UserController()
bc = BucketController()
ic = IncomeController()
ac = AllocationController()

app = Flask(__name__, template_folder='views', static_folder='views/static')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
app.secret_key = 'kgakjgkjg'
app.jinja_env.filters['format_thousands'] = format_thousands
app.jinja_env.filters['format_date'] = format_date
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
# Return the User object whose ID matches the given user_id
	return uc.retrieve(user_id)

@app.route('/')
@login_required
def index():
	return render_template('/users/index.html', title='Home',
						   user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""
	Login a user.
	"""
	form = LoginForm()
	if form.validate_on_submit():
		# Check if the username and password are correct
		# For example, using a hypothetical 'check_login' function
		user = uc.check_login(form.username.data, form.password.data)
		print(form.username.data)
		print(form.password.data)
		if user is not None:
			# Log the user in
			# And then redirect to another page
			login_user(user)
			session['user_id'] = user.get_id()
			session.permanent = True
			return redirect(url_for('index'))
		else:
			flash('Invalid username or password')
	return render_template('/users/login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	"""
	Register a new user.
	"""
	form = RegisterForm()
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['username', 'password', 'first_name', 'last_name']}
		user = uc.create_user(**form_data)
		uc.export_instances()
		login_user(user)
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('index'))
	return render_template('/users/register.html', title='Register', form=form)

@app.route('/create_bucket', methods=['GET', 'POST'])
@login_required
def create_bucket():
	"""
	Create a new bucket.
	"""
	form = BucketForm()
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['name', 'goal', 'deadline', 'frequency', 'comment', 'icon', 'currency']}
		bc.create_bucket(**form_data, **{'user_uuid': current_user.uuid})
		bc.export_instances(load=True)
		flash('Congratulations, you have created a bucket!')
		return redirect(url_for('index'))
	return render_template('/buckets/create_bucket.html', title='Create Bucket', form=form)

@app.route('/logout')
@login_required
def logout():
	session.pop('user_id', None)
	logout_user()
	return redirect(url_for('index'))

@app.route('/buckets', methods=['GET'])
@login_required
def list_buckets():
	return render_template('/buckets/index_bucket.html', title='List Buckets',
						   user=current_user,buckets=bc.list_buckets(current_user.get_id()))

@app.route('/buckets/<uuid>', methods=['GET'])
@login_required
def show_bucket(uuid):
	bucket = bc.retrieve(uuid)
	allocations = ac.retrieve_allocations_by_bucket(uuid)

	div = bucket_completion(bucket)
	return render_template('/buckets/show_bucket.html', title='Show Bucket',
						   user=current_user, bucket=bucket,
						   plot=div, allocations=allocations)

@app.route('/buckets/<uuid>/edit', methods=['GET', 'POST'])
@login_required
def edit_bucket(uuid):
	bucket = bc.retrieve(uuid)
	form = BucketForm(obj=bucket)
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['name', 'goal', 'deadline', 'frequency', 'comment', 'icon']}
		bc.update_bucket(bucket_uuid=uuid, **form_data)
		bc.export_instances(load=True)
		return redirect(url_for('show_bucket', uuid=uuid))
	return render_template('/buckets/edit_bucket.html', title='Edit Bucket', form=form,
						   user=current_user, bucket=bc.retrieve(uuid))

@app.route('/buckets/<uuid>/delete', methods=['GET'])
@login_required
def delete_bucket(uuid):
	bc.delete_bucket(uuid)
	bc.export_instances(load=True)
	return redirect(url_for('list_buckets'))

@app.route('/create_allocation/<bucket_uuid>', methods=['GET', 'POST'])
@login_required
def create_allocation(bucket_uuid):
	"""
	Create a new allocation.
	"""
	bucket = bc.retrieve(bucket_uuid)
	form = AllocationForm()
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['date', 'amount', 'note']}
		ac.create_allocation(**form_data, **{'user_uuid': current_user.get_id(), 'target_uuid': bucket_uuid})
		ac.export_instances(load=True)
		bc.allocate_to_bucket(form_data['amount'], bucket_uuid)
		bc.export_instances(load=True)
		return redirect(url_for('show_bucket', uuid=bucket_uuid))
	return render_template('/transactions/allocations/create_allocation.html',
						   title='Create Allocation', form=form, bucket=bucket)

@app.route('/delete_allocation/<uuid>', methods=['GET'])
@login_required
def delete_allocation(uuid):
    allocation = ac.retrieve(uuid)
    ac.delete_allocation(uuid)
    ac.export_instances(load=True)
    bc.allocate_to_bucket(-allocation.amount, allocation.target_uuid)
    bc.export_instances(load=True)
    return redirect(url_for('show_bucket', uuid=allocation.target_uuid))

if __name__ == '__main__':
	uc.load_instances()
	app.run(port=5000, debug=True)
