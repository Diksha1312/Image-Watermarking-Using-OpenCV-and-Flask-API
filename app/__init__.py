from flask import Flask
import os
from markupsafe import escape

app = Flask(__name__)

# Set a default environment if FLASK_ENV is not set
env = os.getenv('FLASK_ENV', 'development')
app.config['ENV'] = env

if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views

# C:\Users\Lenovo\Documents\PersonalProjects\Project2-Image Watermarking\app
