from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main_bases.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
