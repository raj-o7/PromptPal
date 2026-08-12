from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import CustomLogger
from .models import db  # Import db instance from models.py

# Load environment variables from .env file
load_dotenv()

class AppConfig:
    """Class to handle application configuration"""
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from config.yaml"""
        with open("config/config.yaml", 'r') as file:
            config = yaml.safe_load(file)

        # Replace API key placeholder with the actual value from environment variables
        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('API_KEY')  # Get the API key from .env

        return config

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, template_folder='templates')

    # Load Configuration 
    app_config = AppConfig()
    app.config.update(app_config.config)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Set up logging
    logger = CustomLogger().get_logger()
    logger.info("Flask Application starting..")

    # Import and register routes (Blueprint)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Shell context processor (so db and User auto-load in flask shell)
    @app.shell_context_processor
    def make_shell_context():
        from .models import User  # Import models here
        return {'db': db, 'User': User}

   with app.app_context():
        db.create_all()

    return app
