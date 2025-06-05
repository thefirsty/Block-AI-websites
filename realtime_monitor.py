import time
import pygetwindow as gw
from ai_detector import is_ai_site
from blocker import block_url
from loguru import logger

def start_monitoring():
    logger.info("Monitoring AI-related websites... Press Ctrl+C to stop.")
    blocked = set()

    try:
        while True:
            windows = gw.getAllTitles()
            for title in windows:
                if " - Google Chrome" in title:
                    domain_guess = title.split(" - ")[0].strip()
                    if domain_guess and domain_guess not in blocked and is_ai_site(domain_guess):
                        block_url("https://" + domain_guess)
                        blocked.add(domain_guess)
                        logger.info(f"Blocked: {domain_guess}")
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Monitoring stopped.")
