import platform
import os
from loguru import logger

BLOCK_MARKER_START = "#ai_blocker_start"
BLOCK_MARKER_END = "#ai_blocker_end"

def get_hosts_path():
    return r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"

def flush_dns():
    logger.info("Flushing DNS cache...")
    result = os.system(r"C:\Windows\System32\ipconfig.exe /flushdns")
    if result == 0:
        logger.info("DNS cache flushed.")
    else:
        logger.warning("DNS flush failed. Run as admin.")

def unblock_ai_domains():
    hosts_path = get_hosts_path()
    try:
        with open(hosts_path, "r", encoding="utf-8") as f:
            content = f.read()

        if BLOCK_MARKER_START in content and BLOCK_MARKER_END in content:
            before = content.split(BLOCK_MARKER_START)[0]
            after = content.split(BLOCK_MARKER_END)[-1]
            new_content = before.strip() + "\n\n" + after.strip()

            with open(hosts_path, "w", encoding="utf-8") as f:
                f.write(new_content.strip() + "\n")

            logger.info("AI domain block removed from hosts file.")
            flush_dns()
        else:
            logger.info("No AI block section found in hosts file.")

    except PermissionError:
        logger.error("Run as administrator to modify hosts file.")

if __name__ == "__main__":
    unblock_ai_domains()
