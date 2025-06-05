import time
import pygetwindow as gw
from blocker import block_url
from loguru import logger
from ai_detector import contains_ai_keyword

#mapping keywords
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
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped.")
