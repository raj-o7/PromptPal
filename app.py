import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from main import create_app, db  # Import create_app and db from main
from flask_cors import CORS

# Load environment variables from .env
load_dotenv()

print("Current working directory", os.getcwd())

# Create app using factory
app = create_app()
CORS(app)  # Enable CORS after app is created   

# JWT Configuration (after app is created)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

# Optional: Create DB tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures tables are created
    print("Flask app is running on http://127.0.0.1:5000/")
    app.run(host='127.0.0.1', port=5000, debug=True)
