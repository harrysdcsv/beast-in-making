#!/usr/bin/env python3
"""
Render Environment Diagnostics Script
Run this to check if your environment variables are properly configured on Render
"""

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_environment():
    """Check all required environment variables"""
    
    # Required environment variables
    required_vars = {
        'API_ID': 'Telegram API ID',
        'API_HASH': 'Telegram API Hash', 
        'BOT_TOKEN': 'Telegram Bot Token',
        'OWNER': 'Bot Owner User ID',
        'AUTH_USERS': 'Authorized User IDs (comma-separated)',
        'TOTAL_USERS': 'Total User IDs (comma-separated)'
    }
    
    logging.info("🔍 Checking environment variables...")
    
    missing_vars = []
    
    for var_name, description in required_vars.items():
        value = os.environ.get(var_name)
        if value:
            # Don't log sensitive values, just confirm they exist
            if 'TOKEN' in var_name or 'HASH' in var_name:
                logging.info(f"✅ {var_name}: [HIDDEN] - {description}")
            else:
                logging.info(f"✅ {var_name}: {value} - {description}")
        else:
            logging.error(f"❌ {var_name}: NOT SET - {description}")
            missing_vars.append(var_name)
    
    if missing_vars:
        logging.error(f"🚨 Missing {len(missing_vars)} required environment variables!")
        logging.error("Please set these in your Render service environment:")
        for var in missing_vars:
            logging.error(f"   - {var}")
        return False
    else:
        logging.info("🎉 All required environment variables are set!")
        return True

def test_imports():
    """Test importing required modules"""
    
    logging.info("📦 Testing module imports...")
    
    try:
        logging.info("   Testing basic imports...")
        import pyrogram
        import tgcrypto
        import aiohttp
        import requests
        logging.info("✅ Core modules imported successfully")
        
        logging.info("   Testing vars module...")
        from modules.vars import API_ID, API_HASH, BOT_TOKEN, OWNER
        logging.info("✅ vars module imported successfully")
        
        logging.info("   Testing main module imports...")
        # Import main without running it
        import main
        logging.info("✅ main module imported successfully")
        
        return True
        
    except ImportError as e:
        logging.error(f"❌ Import error: {e}")
        return False
    except Exception as e:
        logging.error(f"❌ Unexpected error during import: {e}")
        return False

def main():
    """Run all diagnostics"""
    
    logging.info("🚀 Starting Render Environment Diagnostics...")
    logging.info("=" * 50)
    
    env_ok = check_environment()
    logging.info("-" * 30)
    
    imports_ok = test_imports() 
    logging.info("-" * 30)
    
    if env_ok and imports_ok:
        logging.info("🎉 All checks passed! Your bot should start successfully on Render.")
    else:
        logging.error("🚨 Some checks failed. Fix the issues above before deploying.")
        
    logging.info("=" * 50)

if __name__ == "__main__":
    main()