import requests
from bs4 import BeautifulSoup

AI_KEYWORDS = ["artificial intelligence", "chatbot", "gpt", "llm", "openai", "copilot", "generative"]
AI_DOMAINS = ["chatgpt.com", "openai.com", "bard.google.com", "gemini.google.com", "copilot.microsoft.com", "character.ai", "claude.ai", "perplexity.ai"]

def is_ai_site(url):
    url = url.lower()
    if any(domain in url for domain in AI_DOMAINS):
        return True

    try:
        response = requests.get("https://" + url, timeout=5)
        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()
        meta = ' '.join([m.get('content', '') for m in soup.find_all('meta')]).lower()
        combined = text + meta

        return any(keyword in combined for keyword in AI_KEYWORDS)

    except Exception:
        return False
