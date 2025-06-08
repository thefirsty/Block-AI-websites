import platform
import os
from loguru import logger

AI_DOMAINS = [
    "chatgpt.com", "www.chatgpt.com", "openai.com", "chat.openai.com",
    "bard.google.com", "gemini.google.com", "copilot.microsoft.com",
    "claude.ai", "perplexity.ai", "character.ai", "chat.yishreylev.net"
]

BLOCK_MARKER_START = "#ai_blocker_start"
BLOCK_MARKER_END = "#ai_blocker_end"
REDIRECT_IP = "127.0.0.1"

def get_hosts_path():
    return r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"

def flush_dns():
    logger.info("Flushing DNS cache...")
    result = os.system(r"C:\Windows\System32\ipconfig.exe /flushdns")
    if result == 0:
        logger.info("DNS cache flushed.")
    else:
        logger.warning("DNS flush failed. Run as admin.")

def block_ai_domains():
    hosts_path = get_hosts_path()
    try:
        with open(hosts_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove old block if exists
        if BLOCK_MARKER_START in content and BLOCK_MARKER_END in content:
            before = content.split(BLOCK_MARKER_START)[0]
            after = content.split(BLOCK_MARKER_END)[-1]
            content = before.strip() + "\n\n" + after.strip()

        # Add new block
        lines = [BLOCK_MARKER_START]
        for domain in AI_DOMAINS:
            lines.append(f"{REDIRECT_IP} {domain}")
        lines.append(BLOCK_MARKER_END)

        new_content = content.strip() + "\n\n" + "\n".join(lines) + "\n"

        with open(hosts_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info("AI domains have been blocked.")
        flush_dns()

    except PermissionError:
        logger.error("Run as administrator to modify hosts file.")

if __name__ == "__main__":
    block_ai_domains()
