from flask import render_template, flash, redirect, url_for, Flask, session, request
from flask_login import login_required, login_user, logout_user, LoginManager, current_user
from datetime import timedelta
from views.visualizations.bucket_visualization import bucket_completion
from controllers.bucket_controller import BucketController
from controllers.user_controller import UserController
from controllers.transaction_controller import IncomeController, AllocationController
from views.forms.user_forms import LoginForm, RegisterForm, BalanceForm
from views.forms.bucket_forms import BucketForm
from views.forms.transaction_forms import AllocationForm, IncomeForm
from views.static.utils import format_thousands, format_date, format_comment, free_money_calculation

uc = UserController()
bc = BucketController()
ic = IncomeController()
ac = AllocationController()



app = Flask(__name__, template_folder='views', static_folder='views/static')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
app.secret_key = 'kgakjgkjg'
app.jinja_env.filters['format_thousands'] = format_thousands
app.jinja_env.filters['format_date'] = format_date
app.jinja_env.filters['format_comment'] = format_comment
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	"""
	Load a user.
 	
  	Params
	------
		:param user_id: The unique identifier of the user.
		:type user_id: str
  
	Returns
	-------
		:return: User instance or None if not found.
   	"""
	return uc.retrieve(user_id)

@app.route('/')
@login_required
def index():
	"""
	Home page. Redirects to the enter_balance page if 
	the user has not entered their balance yet.

	Login is required to view this page.

	Returns
	-------
	:return: Home page.
	"""
	user = uc.retrieve(current_user.get_id())
	allocations = ac.retrieve_allocations_by_user(user.uuid)
	income = ic.next_income(user.uuid)
	free_money = free_money_calculation(user, allocations, income)
	if session.get('just_logged_in'):
		session['just_logged_in'] = False
		return redirect(url_for('enter_balance'))
	return render_template('/users/index.html', title='Home',
						   user=current_user, user=user, allocations=allocations, 
         free_money=free_money)

@app.route('/enter_balance', methods=['GET', 'POST'])
@login_required
def enter_balance():
    """
    Enter the user's balance.
	
    Login is required to view this page.
    
    Returns
    -------
    :return: Enter balance page.
    """
    user = uc.retrieve(current_user.get_id())
    form = BalanceForm()
    if user.balance != 0:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user.balance = form.balance.data
        return redirect(url_for('index'))
    return render_template('/users/enter_balance.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""
	Login a user.
	
	Redirects to the home page if the user is already logged in.
	"""
	form = LoginForm()
	if form.validate_on_submit():
		# Check if the username and password are correct
		# For example, using a hypothetical 'check_login' function
		user = uc.check_login(form.username.data, form.password.data)
		if user is not None:
			# Log the user in
			# And then redirect to another page
			login_user(user)
			session['just_logged_in'] = True
			session['user_id'] = user.get_id()
			session.permanent = True
			return redirect(url_for('index') or request.args.get('next'))
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
		bc.create_bucket(**form_data, user_uuid=current_user.uuid)
		bc.export_instances(load=True)
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
	max_value = bucket.goal - bucket.current_amount
	form = AllocationForm(max_value=max_value)
	allocations = ac.retrieve_allocations_by_bucket(bucket_uuid)
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['date', 'amount', 'note']}
		ac.create_allocation(**form_data, user_uuid=current_user.get_id(), target_uuid=bucket_uuid)
		ac.export_instances(load=True)
		bc.update_amount_bucket(allocations, bucket_uuid)
		bc.export_instances(load=True)
		return redirect(url_for('show_bucket', uuid=bucket_uuid))
	return render_template('/transactions/allocations/create_allocation.html',
						   title='Create Allocation', form=form, bucket=bucket)

@app.route('/delete_allocation/<uuid>', methods=['GET'])
@login_required
def delete_allocation(uuid):
    allocation = ac.retrieve(uuid)
    allocations = ac.retrieve_allocations_by_bucket(allocation.target_uuid)
    ac.delete_allocation(uuid)
    ac.export_instances(load=True)
    bc.update_amount_bucket(allocations, allocation.target_uuid)
    bc.export_instances(load=True)
    return redirect(url_for('show_bucket', uuid=allocation.target_uuid))


@app.route('/edit_allocation/<uuid>', methods=['GET', 'POST'])
@login_required
def edit_allocation(uuid):
	allocation = ac.retrieve(uuid)
	bucket = bc.retrieve(allocation.target_uuid)
	max_value = bucket.goal - bucket.current_amount + allocation.amount
	form = AllocationForm(max_value=max_value, obj=allocation)
	if form.validate_on_submit():
		allocations = ac.retrieve_allocations_by_bucket(allocation.target_uuid)
		form_data = {key: value for key, value in form.data.items() if key in ['date', 'amount', 'note']}
		ac.update_allocation(allocation_uuid=uuid, **form_data)
		ac.export_instances(load=True)
		bc.update_amount_bucket(allocations, allocation.target_uuid)
		bc.export_instances(load=True)
		return redirect(url_for('show_bucket', uuid=allocation.target_uuid))
	return render_template('/transactions/allocations/edit_allocation.html',
						   title='Edit Allocation', form=form, allocation=allocation,
						   bucket=bucket)


@app.route('/index_income', methods=['GET'])
@login_required
def list_incomes():
	for income in ic.list_incomes(current_user.get_id()):
		print(income.__dict__)
	return render_template('/transactions/incomes/index_income.html', title='List Incomes',
						   user=current_user, incomes=ic.list_incomes(current_user.get_id()))


@app.route('/create_income', methods=['GET', 'POST'])
@login_required

def create_income():
	"""
	Create a new income.
	"""
	form = IncomeForm()
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['start_date', 'end_date',
                                                                         'currency', 'amount', 'note', 'frequency', 'source']}
		ic.create_income(**form_data, user_uuid=current_user.get_id())
		ic.export_instances(load=True)
		return redirect(url_for('index'))
	return render_template('/transactions/incomes/create_income.html',
						   title='Create Income', form=form)
 
@app.route('/show_income/<uuid>', methods=['GET', 'POST'])
@login_required
def show_income(uuid):
	income = ic.retrieve(uuid)
	return render_template('/transactions/incomes/show_income.html', title='Show Income',
						   user=current_user, income=income)

@app.route('/edit_income/<uuid>', methods=['GET', 'POST'])
@login_required
def edit_income(uuid):
	income = ic.retrieve(uuid)
	form = IncomeForm(obj=income)
	if form.validate_on_submit():
		form_data = {key: value for key, value in form.data.items() if key in ['start_date', 'end_date',
                                                                         'currency', 'amount', 'note', 'frequency', 'source']}
		ic.update_income(income_uuid=uuid, **form_data)
		ic.export_instances(load=True)
		return redirect(url_for('show_income', uuid=uuid))
	return render_template('/transactions/incomes/edit_income.html', title='Edit Income',
						   form=form, user=current_user, income=income)

@app.route('/delete_income/<uuid>', methods=['GET'])
@login_required
def delete_income(uuid):
	ic.delete_income(uuid)
	ic.export_instances(load=True)
	return redirect(url_for('list_incomes'))

if __name__ == '__main__':
	uc.load_instances()
	app.run(port=5000, debug=True)
