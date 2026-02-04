#!/usr/bin/env python3
"""
ZHEERA (ژییرە) - Intelligent Kurdish Sorani Telegram Bot
A Telegram bot powered by Google's Gemini 2.0 Flash model,
specialized for Kurdish Sorani language interactions.
"""

import os
import logging
from typing import Dict
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import google.generativeai as genai
from config import Config

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# User conversation history storage
user_conversations: Dict[int, list] = {}

# System prompt defining ZHEERA's personality
SYSTEM_PROMPT = """Your name is ZHEERA (ژییرە), which means intelligent person in Kurdish Sorani.
You are an AI assistant specialized in helping Kurdish Sorani speakers.
Respond primarily in Kurdish Sorani when possible, but can understand and respond in other languages if needed.
Be helpful, friendly, and culturally aware when interacting with users.
Always maintain a professional yet warm tone in your responses."""


def initialize_gemini():
    """Initialize and configure the Gemini AI model."""
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel(
            model_name='gemini-2.0-flash-exp',
            system_instruction=SYSTEM_PROMPT
        )
        logger.info("Gemini AI model initialized successfully")
        return model
    except Exception as e:
        logger.error(f"Failed to initialize Gemini AI: {e}")
        raise


# Initialize Gemini model
gemini_model = initialize_gemini()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command with bilingual welcome message."""
    user = update.effective_user
    user_id = user.id
    
    # Initialize conversation history for new user
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    welcome_message = (
        "سڵاو! من ژییرە (ZHEERA) م، یاریدەدەری زیرەکی دەستکردی تۆم. 🤖\n"
        "من لێرەم بۆ یارمەتیدانت بە زمانی کوردی سۆرانی.\n"
        "چۆن دەتوانم یارمەتیت بدەم؟\n\n"
        "Hello! I'm ZHEERA (ژییرە), your intelligent AI assistant. 🤖\n"
        "I'm here to help you in Kurdish Sorani language.\n"
        "How can I assist you today?"
    )
    
    await update.message.reply_text(welcome_message)
    logger.info(f"User {user_id} ({user.username}) started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command with instructions in Kurdish Sorani."""
    help_message = (
        "📚 **یارمەتی - Help**\n\n"
        "**بە کوردی:**\n"
        "من ژییرە (ZHEERA) م، یاریدەدەری زیرەکی دەستکردیت.\n"
        "تەنها پەیامێکم بۆ بنێرە و من وەڵامت دەدەمەوە!\n\n"
        "**فەرمانەکان:**\n"
        "/start - دەستپێکردن\n"
        "/help - یارمەتی\n"
        "/clear - سڕینەوەی مێژووی گفتوگۆ\n\n"
        "**In English:**\n"
        "I'm ZHEERA (ژییرە), your intelligent AI assistant.\n"
        "Just send me a message and I'll respond!\n\n"
        "**Commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/clear - Clear conversation history\n\n"
        "💡 **تێبینی / Note:** "
        "من باشترین کارکردنم بە زمانی کوردی سۆرانییە، بەڵام زمانە تریش تێدەگەم.\n"
        "I work best in Kurdish Sorani, but I understand other languages too."
    )
    
    await update.message.reply_text(help_message, parse_mode='Markdown')
    logger.info(f"Help command used by user {update.effective_user.id}")


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /clear command to reset conversation history."""
    user_id = update.effective_user.id
    
    if user_id in user_conversations:
        user_conversations[user_id] = []
    
    clear_message = (
        "✅ مێژووی گفتوگۆکەت سڕایەوە!\n"
        "Conversation history cleared!\n\n"
        "دەتوانیت گفتوگۆیەکی نوێ دەست پێ بکەیت.\n"
        "You can start a fresh conversation now."
    )
    
    await update.message.reply_text(clear_message)
    logger.info(f"Conversation cleared for user {user_id}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming text messages and generate responses using Gemini."""
    user = update.effective_user
    user_id = user.id
    user_message = update.message.text
    
    # Initialize conversation history if needed
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    logger.info(f"Message from user {user_id}: {user_message[:50]}...")
    
    try:
        # Send typing action
        await update.message.chat.send_action(action="typing")
        
        # Add user message to conversation history
        user_conversations[user_id].append({
            'role': 'user',
            'parts': [user_message]
        })
        
        # Keep only last 20 messages to avoid token limits
        if len(user_conversations[user_id]) > 20:
            user_conversations[user_id] = user_conversations[user_id][-20:]
        
        # Start chat with history
        chat = gemini_model.start_chat(history=user_conversations[user_id][:-1])
        
        # Generate response
        response = chat.send_message(user_message)
        bot_response = response.text
        
        # Add bot response to conversation history
        user_conversations[user_id].append({
            'role': 'model',
            'parts': [bot_response]
        })
        
        # Send response to user
        await update.message.reply_text(bot_response)
        logger.info(f"Response sent to user {user_id}")
        
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        error_message = (
            "ببوورە، هەڵەیەک ڕوویدا. تکایە دواتر هەوڵ بدەرەوە.\n"
            "Sorry, an error occurred. Please try again later."
        )
        await update.message.reply_text(error_message)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors in the bot."""
    logger.error(f"Exception while handling an update: {context.error}")
    
    # If we have an update with a message, inform the user
    if isinstance(update, Update) and update.message:
        error_message = (
            "ببوورە، کێشەیەک ڕوویدا. تکایە دواتر هەوڵ بدەرەوە.\n"
            "Sorry, something went wrong. Please try again later."
        )
        try:
            await update.message.reply_text(error_message)
        except Exception:
            pass


def main() -> None:
    """Start the bot."""
    try:
        # Validate configuration
        Config.validate()
        
        # Create the Application
        application = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
        
        # Register command handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("clear", clear_command))
        
        # Register message handler for text messages
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Register error handler
        application.add_error_handler(error_handler)
        
        # Start the bot
        logger.info("Starting ZHEERA (ژییرە) bot...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise


if __name__ == '__main__':
    main()
