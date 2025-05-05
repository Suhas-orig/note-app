# scraper/scraper.py
import requests
from bs4 import BeautifulSoup
from .models import NewsArticle  # Import your model to save the data

def scrape_news():
    URL = "https://timesofindia.indiatimes.com/"
    HEADERS = {"User-Agent": "Mozilla/5.0"}
    news_items = []

    response = requests.get(URL, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("figure")
        for item in items:
            title_tag = item.find("figcaption")
            link_tag = item.find("a")
            
            if title_tag and link_tag:
                title = title_tag.text.strip()
                link = link_tag.get("href")

                # Ensure the link is complete
                if link and not link.startswith("http"):
                    link = "https://timesofindia.indiatimes.com" + link

                # Save the scraped news to the database
                news_article = NewsArticle.objects.create(
                    title=title,
                    link=link,
                )
                
                # Append to news_items for JSON response
                news_items.append({"title": title, "link": link})

    return news_items
