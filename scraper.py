import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_website_contents(url):
    normalized_url = str(url).strip()
    if not normalized_url:
        return "Please enter a valid URL."
    if not normalized_url.startswith(("http://", "https://")):
        normalized_url = "https://" + normalized_url

    try:
        response = requests.get(normalized_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Could not fetch the website. Error: {e}"

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"
    for tag in soup(["script", "style", "nav", "footer", "header", "img", "input"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    return f"Title: {title}\n\nPage contents:\n{text}"


def scrape_website_contents(url):
    return fetch_website_contents(url)
