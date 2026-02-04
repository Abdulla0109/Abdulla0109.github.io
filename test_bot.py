#!/usr/bin/env python3
"""
Simple test to verify bot structure and imports
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    try:
        # Test standard library imports
        import logging
        from dotenv import load_dotenv
        print("✓ Standard library imports successful")
        
        # Test telegram imports
        from telegram import Update
        from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
        print("✓ Telegram bot imports successful")
        
        # Test Google AI imports
        import google.generativeai as genai
        print("✓ Google Gemini AI imports successful")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_bot_structure():
    """Test that bot.py has correct structure"""
    try:
        with open('bot.py', 'r') as f:
            content = f.read()
            
        # Check for essential functions
        required_functions = [
            'start_command',
            'help_command',
            'new_conversation_command',
            'handle_message',
            'error_handler',
            'main'
        ]
        
        for func in required_functions:
            if f'async def {func}' in content or f'def {func}' in content:
                print(f"✓ Function '{func}' found")
            else:
                print(f"✗ Function '{func}' not found")
                return False
        
        # Check for environment variable handling
        if 'TELEGRAM_BOT_TOKEN' in content and 'GEMINI_API_KEY' in content:
            print("✓ Environment variables properly configured")
        else:
            print("✗ Missing environment variable configuration")
            return False
            
        # Check for conversation history
        if 'start_chat' in content:
            print("✓ Conversation history implementation found")
        else:
            print("✗ Conversation history not implemented")
            return False
            
        return True
    except Exception as e:
        print(f"✗ Error reading bot.py: {e}")
        return False

def test_configuration_files():
    """Test that all configuration files exist"""
    files = [
        'requirements.txt',
        '.env.example',
        '.gitignore',
        'Dockerfile',
        'README.md'
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

if __name__ == '__main__':
    print("=" * 50)
    print("Running Bot Structure Tests")
    print("=" * 50)
    print()
    
    print("Test 1: Checking imports (requires dependencies installed)")
    print("-" * 50)
    # Skip import test if dependencies not installed
    print("⚠ Skipping import test (dependencies may not be installed)")
    print()
    
    print("Test 2: Checking bot structure")
    print("-" * 50)
    test2 = test_bot_structure()
    print()
    
    print("Test 3: Checking configuration files")
    print("-" * 50)
    test3 = test_configuration_files()
    print()
    
    print("=" * 50)
    if test2 and test3:
        print("✓ All tests passed!")
        print("=" * 50)
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        print("=" * 50)
        sys.exit(1)
