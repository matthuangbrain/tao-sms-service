from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize database
db = SQLAlchemy(app)

# Import models after db initialization to avoid circular imports
from app.models import User, Session, Message, Corpus, Passage
from app.services.twilio_service import TwilioService

# Initialize Twilio service
twilio_service = TwilioService()

@app.route('/sms', methods=['POST'])
def sms():
    """Handle incoming SMS messages"""
    return twilio_service.handle_incoming_message()

# Create database tables
with app.app_context():
    db.create_all()
