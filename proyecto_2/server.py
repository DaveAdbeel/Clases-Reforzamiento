from flask import Flask
from controllers.app_controllers import bp

app = Flask(__name__)

app.register_blueprint(bp)