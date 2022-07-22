from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, SearchForm, HotelForm
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from functions import find_hotel, dict_to_html, get_hotel_rate


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '0ea0fddf88db1442bf02fd39c2ea5e5d'

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# engine = db.create_engine('sqlite:///site.db')

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.password}')"


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('search_for_hotel')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                # login_user(user, remember=form.remember.data)
                return redirect(url_for("search_for_hotel"))

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)


@app.route("/search_for_hotel", methods=['GET', 'POST'])
def search_for_hotel():
    form = SearchForm()
    if form.validate_on_submit():
        city = form.city.data
        city_info = find_hotel(city)
        return render_template('search_for_hotel.html', form=form, hotel_info = city_info)
    return render_template('search_for_hotel.html', form=form)


@app.route("/display_rates", methods=['GET', 'POST'])
def display_rates():
    form = HotelForm()
    if form.validate_on_submit():
        check_in_date = form.check_in_date.data
        check_out_date = form.check_out_date.data
        # hotel_id = request.form.get('hotelId')
        rate = get_hotel_rate('1050165', check_in_date, check_out_date)
        return render_template('display_rates.html', form=form, hotel_rate = rate)

    return render_template('display_rates.html', form=form)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

