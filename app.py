from flask import render_template, flash, redirect, url_for, Flask, request
from flask_login import login_required, login_user, logout_user, LoginManager, current_user
from models.bucket import Bucket
from models.user import User
from controllers.bucket_controller import BucketController
from controllers.user_controller import UserController
from views.forms.user_forms import LoginForm, RegisterForm
from views.forms.bucket_forms import BucketForm

uc = UserController()
uc.load_instances()

bc = BucketController()
bc.load_instances()

app = Flask(__name__, template_folder='views', static_folder='views/static')
app.secret_key = 'kgakjgkjg'
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
        form_data = {key: value for key, value in form.data.items() if key in ['name', 'goal', 'deadline', 'frequency', 'comment']}
        bc.create_bucket(**form_data, **{'user_uuid': current_user.uuid})
        bc.export_instances()
        flash('Congratulations, you have created a bucket!')
        return redirect(url_for('index'))
    return render_template('/buckets/create_bucket.html', title='Create Bucket', form=form)

@app.route('/logout')
@login_required
def logout():
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
    return render_template('/buckets/show_bucket.html', title='Show Bucket',
                           user=current_user, bucket=bc.retrieve(uuid))

if __name__ == '__main__':
	uc.load_instances()
	app.run(port=5000, debug=True)
