from flask import Flask,request,render_template,redirect,url_for
from flask_login import LoginManager, login_user, logout_user, UserMixin, login_required,current_user
# from flask_wtf import FlaskFormin

app = Flask(__name__)
app.config['SECRET_KEY'] = '123df'
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_message = '请登录以访问此页面'  

users = [
    {'username': 'a', 'password': '1'},
    {'username': 'b', 'password': '2'}
]
def query(username):
	for user in users:
		if user['username'] == username:
			return user
class User(UserMixin):
	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id




@login_manager.user_loader
def load_user(username):
	user = User()
	# c_user = User()
	# print((user.username))
	print(username)
	return user
	# return user.get_id()
	# if query(username) is not None:
		
	# 	c_user.id = (username)
	# 	return c_user
# 		print(c_user)
	# return None

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		user = query(username)
		if user is not None and request.form['password'] == user['password']:
			c_user = User()
			c_user.id = username

			login_user(c_user)
			# print(username)
			# print(current_user.get_id(), login_user(c_user))
			return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/')
@login_required
def index():
    return 'you login in!'


@app.route('/settings')
@login_required
def settings():
	return 'ok'


if __name__ == '__main__':
	app.run(debug=True)


















