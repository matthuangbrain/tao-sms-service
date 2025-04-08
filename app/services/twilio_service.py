from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import request, current_app
import os
from datetime import datetime
from ..models import User, Session, Message, MessageDirection
from .. import db

class TwilioService:
    def __init__(self):
        self.client = Client(
            os.getenv('TWILIO_ACCOUNT_SID'),
            os.getenv('TWILIO_AUTH_TOKEN')
        )
        self.phone_number = os.getenv('TWILIO_PHONE_NUMBER')

    def handle_incoming_message(self):
        """Handle incoming SMS messages"""
        # Get the message details from the request
        incoming_msg = request.values.get('Body', '').strip()
        sender_phone = request.values.get('From', '')
        
        # Find or create user
        user = User.query.filter_by(phone_number=sender_phone).first()
        if not user:
            # New user signing up
            user = User(phone_number=sender_phone)
            db.session.add(user)
            db.session.commit()
            return self._send_welcome_message(user)
        
        # Get or create active session
        session = Session.query.filter_by(
            user_id=user.id,
            is_active=True
        ).first()
        
        if not session:
            session = Session(user_id=user.id)
            db.session.add(session)
            db.session.commit()
        
        # Record the incoming message
        self._record_message(session, incoming_msg, MessageDirection.INBOUND)
        
        # TODO: Handle the message content and generate response
        # For now, just send a placeholder response
        response = "Thank you for your message. I am Lao Tzu, and I will respond to you soon."
        self._send_message(user.phone_number, response)
        self._record_message(session, response, MessageDirection.OUTBOUND)
        
        # Update user's last interaction
        user.last_interaction = datetime.utcnow()
        db.session.commit()
        
        return str(MessagingResponse())

    def _send_welcome_message(self, user):
        """Send welcome message to new users"""
        welcome_msg = (
            "Welcome to the Daily Tao! You will receive a passage from the Tao Te Ching "
            "every day at 9am. Reply to any message to chat with Lao Tzu. "
            "Text STOP to unsubscribe at any time."
        )
        self._send_message(user.phone_number, welcome_msg)
        return str(MessagingResponse())

    def _send_message(self, to_number, message):
        """Send an SMS message"""
        self.client.messages.create(
            body=message,
            from_=self.phone_number,
            to=to_number
        )

    def _record_message(self, session, content, direction):
        """Record a message in the database"""
        message = Message(
            session_id=session.id,
            direction=direction,
            content=content,
            timestamp=datetime.utcnow()
        )
        db.session.add(message)
        db.session.commit() 