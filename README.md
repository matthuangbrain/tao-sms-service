# Tao SMS Service

A service that sends daily passages from the Tao Te Ching via SMS and allows users to chat with an AI-powered Lao Tzu.

## Features

- Daily Tao Te Ching passages delivered at 9am
- Interactive chat with an AI-powered Lao Tzu
- Session-based conversation management
- Easy opt-in/opt-out via SMS

## Tech Stack

- Python 3.x
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Twilio (SMS Service)
- Anthropic Claude (AI Responses)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/matthuangbrain/tao-sms-service.git
   cd tao-sms-service
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your credentials:
   ```
   # Twilio Configuration
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=your_twilio_phone_number_here

   # Database Configuration
   DATABASE_URL=sqlite:///tao_sms.db

   # Anthropic (Claude) Configuration
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

5. Initialize the database:
   ```bash
   python run.py
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python run.py
   ```

2. For development, use ngrok to create a public URL:
   ```bash
   ngrok http 5000
   ```

3. Configure your Twilio webhook to point to your ngrok URL + `/sms`

## Usage

1. Text the service's phone number to sign up
2. Receive daily Tao Te Ching passages at 9am
3. Reply to any message to chat with Lao Tzu
4. Text "STOP" to unsubscribe

## Project Structure

```
tao-sms-service/
├── app/
│   ├── __init__.py      # Flask application setup
│   ├── config.py        # Configuration settings
│   ├── models.py        # Database models
│   └── services/
│       └── twilio_service.py  # SMS handling
├── data/                # Data files (e.g., Tao Te Ching passages)
├── migrations/          # Database migrations
├── .env                 # Environment variables
├── .gitignore          # Git ignore file
├── requirements.txt    # Python dependencies
├── run.py             # Application entry point
└── README.md          # This file
```

## Development Status

- [x] Basic project structure
- [x] Database schema
- [x] Twilio integration
- [ ] Daily message scheduler
- [ ] Claude integration
- [ ] Passage database population
- [ ] Session management
- [ ] Error handling
- [ ] Testing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details
