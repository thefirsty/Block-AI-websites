import time
import pygetwindow as gw
from blocker import block_url
from loguru import logger

# Known AI-related domains
AI_DOMAINS = [
    "chatgpt.com", "openai.com", "bard.google.com", "gemini.google.com",
    "copilot.microsoft.com", "character.ai", "claude.ai", "perplexity.ai"
]

def start_monitoring():
    logger.info("Monitoring started. Press Ctrl+C to stop.")
    blocked = set()

    try:
        while True:
            windows = gw.getAllTitles()
            for title in windows:
                lowered_title = title.lower()
                for domain in AI_DOMAINS:
                    if domain in lowered_title and domain not in blocked:
                        block_url("https://" + domain)
                        blocked.add(domain)
                        logger.info(f"Blocked: {domain}")
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped.")
