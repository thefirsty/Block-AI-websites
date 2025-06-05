import time
import os
import pygetwindow as gw
from blocker import block_url
from loguru import logger
from ai_detector import contains_ai_keyword

# Keyword to domain mapping
KEYWORD_TO_DOMAIN = {
    "chatgpt": "chatgpt.com",
    "openai": "openai.com",
    "bard": "bard.google.com",
    "gemini": "gemini.google.com",
    "copilot": "copilot.microsoft.com",
    "claude": "claude.ai",
    "perplexity": "perplexity.ai",
    "character.ai": "character.ai"
}

def flush_dns_cache():
    logger.info("Flushing DNS cache to apply host file changes immediately...")
    try:
        # Explicit full path to ipconfig
        result = os.system(r"C:\Windows\System32\ipconfig.exe /flushdns")
        if result == 0:
            logger.info("DNS cache flushed successfully.")
        else:
            logger.warning("Failed to flush DNS cache. You may need to run as administrator.")
    except Exception as e:
        logger.error(f"Error flushing DNS cache: {e}")

def start_monitoring():
    logger.info("Monitoring started. Press Ctrl+C to stop.")
    blocked = set()

    try:
        while True:
            windows = gw.getAllTitles()
            for title in windows:
                lowered = title.lower()
                if contains_ai_keyword(lowered):
                    for keyword, domain in KEYWORD_TO_DOMAIN.items():
                        if keyword in lowered and keyword not in blocked:
                            block_url("https://" + domain)
                            blocked.add(keyword)
                            logger.info(f"Blocked: {domain} (via keyword: {keyword})")
                            flush_dns_cache()
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped.")
