from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from intsance.config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])

db = SQLAlchemy()
db.init_app(app)
mongo = PyMongo(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class NHIS(db.Model):
    __tablename__ = 'NHIS'
    __bindkey__ = 'postgres_bind'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.first_name, self.last_name)


class EC(db.Model):
    __tablename__ = 'EC'
    __bind_key__ = 'mysql_bind'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.first_name, self.last_name)


class GIS(db.Model):
    __tablename__ = 'GIS'
    __bind_key__ = 'sqlite_bind'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return '<Name: {} {}>'.format(self.first_name, self.last_name)


if __name__ == '__main__':
    manager.run()
