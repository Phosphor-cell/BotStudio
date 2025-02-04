import os

from flask import Flask
app = Flask(__name__)

from config import Config
app.config.from_object('config')

from  app import routes