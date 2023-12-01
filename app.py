from flask import render_template, flash, redirect, url_for, Flask
from controllers.user_controller import UserController
from flask_login import login_required, login_user, logout_user, LoginManager
from models.bucket import Bucket
from models.user import User
from views.forms.user_forms import LoginForm, RegisterForm
from views.forms.bucket_forms import BucketForm
from flask import request

uc = UserController()

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
def index():
	return 'Hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the username and password are correct
        # For example, using a hypothetical 'check_login' function
        user = uc.check_login(form.username.data, form.password.data)
        if user is not None:
            # Log the user in (e.g., using Flask-Login)
            # And then redirect to another page
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('/users/login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form_data = {key: value for key, value in form.data.items() if key in ['username', 'password', 'first_name', 'last_name']}
        user = uc.create_user(**form_data)
        login_user(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('/users/register.html', title='Register', form=form)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


@app.route('/create_bucket', methods=['GET', 'POST'])
@login_required
def create_bucket():
    form = BucketForm()
    if form.validate_on_submit():
        Bucket(**form.data)
        flash('Congratulations, you have created a bucket!')
        return redirect(url_for('index'))
    return render_template('/buckets/create_bucket.html', title='Create Bucket', form=form)

"""
@app.route('/buckets', methods=['GET'])
def list_buckets():
    return render_template('/buckets/list_buckets.html', title='List Buckets', buckets=uc.all())
"""
if __name__ == '__main__':
	app.run(port=5000, debug=True)
	uc.export_instances()
