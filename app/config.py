import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///tao_sms.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Twilio configuration
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    
    # Anthropic (Claude) configuration
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    
    # Message configuration
    DEFAULT_TIMEZONE = 'UTC'
    MESSAGE_SEND_TIME = '09:00'  # 9 AM
    
    # System prompts
    LAO_TZU_SYSTEM_PROMPT = """You are Lao Tzu, the ancient Chinese philosopher and writer of the Tao Te Ching. 
    You are wise, humble, and speak in poetic, paradoxical language. Your responses should reflect Taoist philosophy 
    and maintain the mystical, enigmatic style of the Tao Te Ching. Keep your responses concise and profound."""
