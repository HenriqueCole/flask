from mercado import db, login_manager
from mercado import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    value = db.Column(db.Integer, nullable=False, default=5000)
    items = db.relationship('Item', backref='owner_user', lazy=True)

    @property
    def valueFormat(self):
        if len(str(self.value)) >= 4:
            return f'R$ {str(self.value)[:-3]},{str(self.value)[-3:]}'
        else:
            return f'R$ {str(self.value)}'

    @property
    def passwordcrip(self):
        return self.password

    @passwordcrip.setter
    def passwordcrip(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def convert_password(self, raw_password):
        return bcrypt.check_password_hash(self.password, raw_password)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    bar_code = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
