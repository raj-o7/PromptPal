# app/routes.py

from flask import Blueprint, render_template, request, jsonify
import re
from main.utils import format_response
from main.chat import ChatManager

# Create a Blueprint for the main application
main = Blueprint('main', __name__)

# Initialize the ChatManager
chat_manager = ChatManager()  # Ensure this class is defined in app/chat.py

@main.route('/')
def index():
    """Render the chat interface."""
    return render_template('chat.html')  # Renders the chat.html template

@main.route('/test')
def test():
    return render_template('base.html')  # Assuming base.html exists in templates/

@main.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from users."""
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    # Get AI response using updated ChatManager logic
    ai_response = chat_manager.get_response(user_message)

    # Format the response if necessary (e.g., replace newlines)
    formatted_response = format_response(ai_response)

    return jsonify({"response": formatted_response})  # Return the formatted AI's response as JSON

from flask import Blueprint, request, jsonify
from main.models import User, db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'Username already exists'}), 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg': 'User registered successfully'}), 201





@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'msg': 'Invalid username or password'}), 401

    # Generate JWT token
    access_token = create_access_token(identity={"username": user.username})
    return jsonify({'msg': 'Login successful', 'access_token': access_token}), 200
