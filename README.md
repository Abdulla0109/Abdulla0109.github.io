# Telegram AI Bot with Gemini API

A Telegram bot powered by Google's Gemini AI that provides intelligent responses to user messages.

## Features

- 🤖 AI-powered responses using Google Gemini
- 💬 Natural conversation interface
- 🚀 Easy to deploy and configure
- 📝 Conversation management commands
- 🐳 Docker support for containerized deployment

## Prerequisites

Before running this bot, you need:

1. **Telegram Bot Token**
   - Talk to [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot with `/newbot` command
   - Copy the bot token

2. **Google Gemini API Key**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create an API key
   - Copy the key

## Installation

### Method 1: Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdulla0109/Abdulla0109.github.io.git
   cd Abdulla0109.github.io
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your API keys:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the bot**
   ```bash
   python bot.py
   ```

### Method 2: Docker

1. **Build the Docker image**
   ```bash
   docker build -t telegram-gemini-bot .
   ```

2. **Run the container**
   ```bash
   docker run -d --name gemini-bot \
     -e TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
     -e GEMINI_API_KEY=your_gemini_api_key \
     telegram-gemini-bot
   ```

## Usage

Once the bot is running:

1. Open Telegram and search for your bot
2. Start a conversation with `/start`
3. Send any message and get AI-powered responses!

### Available Commands

- `/start` - Welcome message and introduction
- `/help` - Show help and usage information
- `/new` - Start a new conversation (clear context)

## Deployment Options

### Heroku
```bash
heroku create your-bot-name
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

### Railway
1. Create a new project on [Railway](https://railway.app)
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard
4. Deploy automatically

### VPS/Cloud Server
```bash
# Using systemd service
sudo cp bot.service /etc/systemd/system/
sudo systemctl enable bot
sudo systemctl start bot
```

## Configuration

All configuration is done through environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from BotFather | Yes |
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

## Troubleshooting

**Bot doesn't respond:**
- Check if the bot is running: `ps aux | grep bot.py`
- Verify API keys are correct in `.env` file
- Check logs for error messages

**Gemini API errors:**
- Ensure your API key is valid
- Check if you've exceeded API rate limits
- Verify you have access to Gemini API

**Connection issues:**
- Check your internet connection
- Verify firewall settings
- Ensure Telegram isn't blocked in your region

## Development

To contribute or modify the bot:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions

## Acknowledgments

- Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)

---

Made with ❤️ for the Telegram community