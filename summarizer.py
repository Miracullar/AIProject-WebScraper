import os

from dotenv import load_dotenv
from openai import OpenAI

from scraper import fetch_website_contents

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

system_prompt = """You analyze the contents of a website and
give a short, friendly summary. Ignore navigation menus.
Respond in markdown."""


def summarize(url):
    if not url or not str(url).strip():
        return "Please enter a website URL."

    website = fetch_website_contents(url)
    if website.startswith("Please enter") or website.startswith("Could not fetch"):
        return website

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": website},
        ],
    )

    return response.choices[0].message.content