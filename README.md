# Telegram-Gemini Bot

This project is a Telegram bot that interacts with the Gemini cryptocurrency exchange API. It allows users to perform various operations related to cryptocurrency trading and information retrieval through Telegram.

## Project Structure

```
telegram-gemini-bot/
├── main.py              # Main entry point for the bot
├── requirements.txt     # List of dependencies
├── Procfile             # Deployment commands
├── render.yaml          # Deployment configuration
├── .env                 # Environment variables
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd telegram-gemini-bot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add your API keys and tokens:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   TELEGRAM_TOKEN=your_telegram_bot_token
   ```

## Usage

To run the bot, execute the following command:
```bash
python main.py
```

## Deployment

For deployment, ensure that your environment variables are set correctly in the deployment platform. Use the `Procfile` to specify how to run the application.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.