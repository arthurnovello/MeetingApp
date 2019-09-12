from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from flask_mail import Mail

app = Flask(__name__)

app.config['USER_APP_NAME'] = 'MyApp'
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3307/testDB'
app.config['CSRF_ENABLE'] = True
app.config['USER_ENABLE_EMAIL'] = True
app.config['USER_EMAIL_SENDER'] = app.config['USER_APP_NAME']
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)
mail = Mail(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default=' ')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())


# Setup Flask-User
user_manager = UserManager(app, db, User)


@app.route('/')
def index():
    return '<h1>Home</h1>'


@app.route('/profile')
@login_required
def profile():
    return '<h1>Protect</h1>'


if __name__ == "__main__":
    app.run(debug=True)
