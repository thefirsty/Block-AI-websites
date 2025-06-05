import platform
from loguru import logger


def extract_domain(url):
    """
    Extracts the domain name from a full URL.
    Example: https://www.example.com/path -> www.example.com
    """
    return url.split("//")[-1].split("/")[0]

def block_url(url):
    """
    Adds an entry to the system's hosts file to redirect the given URL's domain to 127.0.0.1.
    This effectively blocks access to that site on the machine.

    Requires administrative privileges to modify the hosts file.
    """
    domain = extract_domain(url)
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
    redirect_ip = "127.0.0.1"

    try:
        with open(hosts_path, "r+", encoding="utf-8") as f:
            content = f.read()
            if domain not in content:
                f.write(f"\n{redirect_ip} {domain}\n")
                logger.info(f"{domain} has been blocked")
            else:
                logger.info(f"{domain} is already blocked")
    except PermissionError:
        logger.error("Must run this script as Administrator to edit the hosts file.")
