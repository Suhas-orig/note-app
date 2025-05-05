#scraper/views.py
from django.http import JsonResponse
from .scraper import scrape_news

def scraper_view(request):
    news = scrape_news()  # Call the scraper function
    return JsonResponse(news, safe=False)  # Return the news as JSON response

import json
from django.views.decorators.csrf import csrf_exempt
from newspaper import Article
from transformers import pipeline

# Load HuggingFace summarizer model (loads once)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@csrf_exempt
def summarize_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            url = data.get("url")

            if not url:
                return JsonResponse({"error": "No URL provided."}, status=400)

            # Extract full article text
            article = Article(url)
            article.download()
            article.parse()

            full_text = article.text

            if not full_text:
                return JsonResponse({"error": "Couldn't extract article text."}, status=500)

            # Summarize the first 1024 characters (for performance)
            summary_chunks = summarizer(full_text[:1024], max_length=150, min_length=40, do_sample=False)

            summary = summary_chunks[0]['summary_text']
            return JsonResponse({"summary": summary})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)