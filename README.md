# ZHEERA (ژییرە) - Intelligent Kurdish Sorani Telegram Bot

<div dir="rtl">

## ژییرە - یاریدەدەری زیرەکی کوردی سۆرانی

**ژییرە** بۆتێکی تەلیگرامە کە بە هەرەندەی **Gemini 2.0 Flash** کاردەکات و تایبەتە بە قسەکەرانی کوردی سۆرانی.

</div>

---

## 🌟 Features | تایبەتمەندیەکان

### English
- 🤖 Powered by Google's latest **Gemini 2.0 Flash** AI model
- 🗣️ Specialized for **Kurdish Sorani** language interactions
- 💬 Maintains conversation context for natural dialogue
- 🔒 Secure configuration with environment variables
- 📱 Easy-to-use Telegram interface
- 🌍 Multilingual support (primarily Kurdish Sorani)

### کوردی سۆرانی
<div dir="rtl">

- 🤖 هێزی وەرگرتووە لە مۆدێلی **Gemini 2.0 Flash** ی گووگڵ
- 🗣️ تایبەتە بە زمانی **کوردی سۆرانی**
- 💬 هێڵی گفتوگۆ دەپارێزێت بۆ دروستکردنی گفتوگۆیەکی سروشتی
- 🔒 ڕێکخستنێکی پارێزراو بە بەکارهێنانی گۆڕاوەکانی ژینگە
- 📱 ڕووکارێکی ئاسان لە تەلیگرام
- 🌍 پشتگیری زمانە جیاوازەکان (بە تایبەتی کوردی سۆرانی)

</div>

---

## 📋 Requirements | پێداویستیەکان

- Python 3.11 or higher
- Telegram Bot Token
- Google Gemini API Key

---

## 🚀 Quick Start | دەستپێکردنی خێرا

### 1. Get Your API Keys | وەرگرتنی کلیلە API ـەکان

#### Telegram Bot Token

<div dir="rtl">

**بە کوردی:**
1. بۆتی [@BotFather](https://t.me/BotFather) لە تەلیگرام بکەرەوە
2. فەرمانی `/newbot` بنێرە
3. ناوێک بۆ بۆتەکەت هەڵبژێرە (وەک: ZHEERA Bot)
4. یوزەرنەیمێک هەڵبژێرە کە بە `bot` کۆتایی دێت (وەک: zheera_bot)
5. توکنەکەت وەربگرە و بیپارێزە

</div>

**In English:**
1. Open [@BotFather](https://t.me/BotFather) on Telegram
2. Send the `/newbot` command
3. Choose a name for your bot (e.g., ZHEERA Bot)
4. Choose a username ending in `bot` (e.g., zheera_bot)
5. Save the token you receive

#### Gemini API Key

<div dir="rtl">

**بە کوردی:**
1. سەردانی [Google AI Studio](https://aistudio.google.com/app/apikey) بکە
2. بە هەژماری گووگڵەکەت بچۆرە ژوورەوە
3. لەسەر "Create API Key" کرتە بکە
4. کلیلە API ـەکەت وەربگرە و بیپارێزە

</div>

**In English:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy and save your API key

### 2. Installation | دامەزراندن

```bash
# Clone the repository
git clone https://github.com/Abdulla0109/Abdulla0109.github.io.git
cd Abdulla0109.github.io

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env file and add your API keys
# nano .env  # or use any text editor
```

### 3. Configuration | ڕێکخستن

Edit the `.env` file and add your credentials:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Bot | کارپێکردنی بۆت

```bash
python bot.py
```

<div dir="rtl">

**بە کوردی:** ئێستا دەتوانیت بۆتەکەت لە تەلیگرام بدۆزیتەوە و دەست بە قسەکردن بکەیت!

</div>

**In English:** Now you can find your bot on Telegram and start chatting!

---

## 💻 Commands | فەرمانەکان

| Command | English | کوردی |
|---------|---------|-------|
| `/start` | Start the bot and see welcome message | دەستپێکردنی بۆت و بینینی پەیامی بەخێرهاتن |
| `/help` | Get help and see available commands | وەرگرتنی یارمەتی و بینینی فەرمانەکان |
| `/clear` | Clear conversation history | سڕینەوەی مێژووی گفتوگۆ |

---

## 🚢 Deployment Options | بژارەکانی بڵاوکردنەوە

### Heroku

1. Create a Heroku account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Deploy:

```bash
heroku create your-bot-name
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set GEMINI_API_KEY=your_key
git push heroku main
```

### Railway

1. Create account at [railway.app](https://railway.app)
2. Create new project from GitHub repo
3. Add environment variables in Railway dashboard
4. Deploy automatically

### VPS (Ubuntu/Debian)

```bash
# Install Python
sudo apt update
sudo apt install python3 python3-pip

# Clone and setup
git clone <your-repo-url>
cd <repo-directory>
pip3 install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Add your API keys

# Run with systemd (for persistent running)
sudo nano /etc/systemd/system/zheera-bot.service
```

**systemd service file:**
```ini
[Unit]
Description=ZHEERA Telegram Bot
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/bot
ExecStart=/usr/bin/python3 bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable zheera-bot
sudo systemctl start zheera-bot
sudo systemctl status zheera-bot
```

### Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

Build and run:

```bash
docker build -t zheera-bot .
docker run -d --env-file .env zheera-bot
```

---

## 📁 Project Structure | پێکهاتەی پرۆژە

```
.
├── bot.py              # Main bot implementation
├── config.py           # Configuration handler
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore         # Git ignore file
├── Procfile           # Heroku deployment
├── runtime.txt        # Python version specification
└── README.md          # This file
```

---

## 🔒 Security Best Practices | باشترین پراکتیسەکانی پاراستن

<div dir="rtl">

**بە کوردی:**
- ⚠️ **هەرگیز** کلیلە API ـەکانت بە ڕاستەوخۆ لە کۆدەکەدا مەنووسە
- 🔐 هەمیشە فایلی `.env` لە `.gitignore` دا بەجێبهێڵە
- 🔄 کلیلەکانت بە بەردەوامی نوێبکەرەوە
- 📝 لۆگەکان بپشکنە بۆ هەر چالاکییەکی گومان لێکراو
- 🚫 کلیلە API ـەکانت لەگەڵ کەسی تر هاوبەش مەکە

</div>

**In English:**
- ⚠️ **Never** hardcode API keys in your code
- 🔐 Always keep `.env` in `.gitignore`
- 🔄 Rotate your API keys regularly
- 📝 Monitor logs for suspicious activity
- 🚫 Don't share your API keys with others

---

## 🐛 Troubleshooting | چارەسەری کێشەکان

### Bot not responding

<div dir="rtl">

**بە کوردی:**
- بڕوانە کە بۆتەکە کارپێکراوە (`python bot.py`)
- دڵنیابە لە دروستی توکنەکانی API لە فایلی `.env`
- لۆگەکان بپشکنە بۆ هەڵەکان

</div>

**In English:**
- Check if bot is running (`python bot.py`)
- Verify API tokens in `.env` file
- Check logs for errors

### Import errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Rate limiting

<div dir="rtl">

**بە کوردی:** ئەگەر زۆر داواکاری خێرا ناردبێت، دەکرێت سنوردار بکرێیت. کەمێک چاوەڕێ بکە و دووبارە هەوڵبدەرەوە.

</div>

**In English:** If you're sending too many requests too quickly, you might hit rate limits. Wait a moment and try again.

---

## 📝 Development | گەشەپێدان

### Adding new features

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Include type hints where possible
- Write descriptive commit messages

---

## 🤝 Contributing | بەشداری

Contributions are welcome! Please feel free to submit a Pull Request.

<div dir="rtl">

**بە کوردی:** بەژداری وەرگیراوە! تکایە بێ دوودڵی داواکارییەکی Pull Request بنێرە.

</div>

---

## 📄 License | مۆڵەت

This project is open source and available under the MIT License.

---

## 👨‍💻 Author | نووسەر

Created with ❤️ for the Kurdish Sorani community

<div dir="rtl">

دروستکراوە بە ❤️ بۆ کۆمەڵگای کوردی سۆرانی

</div>

---

## 📞 Support | پشتگیری

<div dir="rtl">

**بە کوردی:**
- کێشەیەکت هەیە؟ کراوەیەک (Issue) بکەرەوە لە GitHub
- پرسیارت هەیە؟ پەیامێک بنێرە بۆ بۆتەکە لە تەلیگرام

</div>

**In English:**
- Have an issue? Open an issue on GitHub
- Have a question? Send a message to the bot on Telegram

---

## 🙏 Acknowledgments | سپاسگوزاری

- Google Gemini team for the amazing AI model
- python-telegram-bot library maintainers
- Kurdish Sorani speaking community

---

<div align="center">

**ZHEERA (ژییرە)** - Your Intelligent Kurdish Sorani Assistant

Made with 💚 for Kurdistan

</div>