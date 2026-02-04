#!/usr/bin/env python3
"""
Telegram AI Bot with Gemini API Integration
"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get API keys from environment
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Validate environment variables
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"👋 Hello {user.mention_html()}!\n\n"
        "I'm an AI bot powered by Google's Gemini AI.\n\n"
        "Simply send me any message and I'll respond with AI-generated answers.\n\n"
        "Commands:\n"
        "/start - Show this welcome message\n"
        "/help - Show help information\n"
        "/new - Start a new conversation"
    )
    await update.message.reply_html(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_message = (
        "🤖 <b>How to use this bot:</b>\n\n"
        "1. Just send me any text message\n"
        "2. I'll process it with Gemini AI\n"
        "3. Get intelligent responses!\n\n"
        "<b>Commands:</b>\n"
        "/start - Welcome message\n"
        "/help - This help message\n"
        "/new - Clear conversation history\n\n"
        "<b>Tips:</b>\n"
        "- You can ask questions\n"
        "- Request explanations\n"
        "- Get creative content\n"
        "- Solve problems\n"
        "- And much more!"
    )
    await update.message.reply_html(help_message)


async def new_conversation_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start a new conversation by clearing chat history."""
    # Clear the chat history
    if 'chat' in context.user_data:
        del context.user_data['chat']
    await update.message.reply_text(
        "🔄 Conversation cleared! Let's start fresh.\n"
        "What would you like to talk about?"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and generate AI responses."""
    user_message = update.message.text
    user = update.effective_user
    
    logger.info(f"User {user.username or user.id} sent: {user_message}")
    
    # Basic input validation
    if not user_message or len(user_message.strip()) == 0:
        await update.message.reply_text("Please send a valid message.")
        return
    
    # Limit message length to prevent excessive API usage
    if len(user_message) > 4000:
        await update.message.reply_text(
            "Your message is too long. Please keep it under 4000 characters."
        )
        return
    
    # Send typing action
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    try:
        # Initialize or get existing chat session for conversation history
        if 'chat' not in context.user_data:
            context.user_data['chat'] = model.start_chat(history=[])
        
        chat = context.user_data['chat']
        
        # Generate response using Gemini with conversation history
        response = chat.send_message(user_message)
        
        # Check if response has text
        if response.text:
            ai_response = response.text
            logger.info(f"AI response generated successfully")
        else:
            ai_response = "I apologize, but I couldn't generate a proper response. Please try rephrasing your message."
            logger.warning("Gemini returned empty response")
        
        # Send the response
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        error_message = (
            "😔 Sorry, I encountered an error while processing your message.\n"
            "Please try again or rephrase your question."
        )
        await update.message.reply_text(error_message)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors caused by updates."""
    logger.error(f"Update {update} caused error {context.error}")


def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("new", new_conversation_command))
    
    # Register message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
