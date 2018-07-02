from app import *
from .forms import LoginForm


@app.route('/', methods=['GET'])
def home():
	# return 'nice to meet you!'
	return render_template('layout.html', title='ok')


@app.route('/login', methods=['GET','POST'])
def login():
	# 实例化一个 form 表单类
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID={},remember_me={}'.format(form.openid.data, form.remember_me.data))
		return redirect(url_for('/'))

	return render_template('login.html', 
							title='Sign In', 
							form=form)