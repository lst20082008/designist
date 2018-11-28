# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config.from_object('designist.setting')

db = SQLAlchemy(app)

from designist.controller import designist_controller