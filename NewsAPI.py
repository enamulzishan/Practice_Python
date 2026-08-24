import os
import requests

api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    api_key = input("Enter your NewsAPI key: ").strip()

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "bd",
    "apiKey": api_key
}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code == 200 and data.get("status") == "ok":
        print("\nLatest News:\n")

        for news in data.get("articles", []):
            print(news.get("title", "No title"))
    else:
        print("Failed to fetch news.")
        print("Reason:", data.get("message", "Unknown error"))
except requests.exceptions.RequestException as error:
    print("Failed to connect to NewsAPI.")
    print("Reason:", error)
