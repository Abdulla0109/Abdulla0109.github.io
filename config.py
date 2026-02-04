"""
Configuration module for ZHEERA (ژییرە) Telegram Bot
Handles environment variables and configuration settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for bot settings."""
    
    # Telegram Bot Configuration
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # Gemini API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    @classmethod
    def validate(cls) -> None:
        """
        Validate that all required configuration variables are set.
        Raises ValueError if any required variable is missing.
        """
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN not found in environment variables. "
                "Please set it in your .env file or environment."
            )
        
        if not cls.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables. "
                "Please set it in your .env file or environment."
            )
        
        print("✅ Configuration validated successfully")
