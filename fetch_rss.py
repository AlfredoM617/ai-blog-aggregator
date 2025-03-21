import feedparser
import json
from datetime import datetime

# List of RSS feeds
RSS_FEEDS = {
    "Google AI": "https://ai.googleblog.com/feeds/posts/default?alt=rss",
    "AWS ML Blog": "https://aws.amazon.com/blogs/machine-learning/feed/",
    "Hugging Face": "https://huggingface.co/blog/rss",
    "Microsoft AI": "https://techcommunity.microsoft.com/rss/ai-cognitive-services-bg-p/AzureAICognitiveServicesBlog",
}

def fetch_rss():
    posts = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:  # Get the latest 5 posts per source
            posts.append({
                "title": entry.title,
                "source": source,
                "url": entry.link,
                "published": entry.published if "published" in entry else datetime.now().isoformat(),
                "summary": entry.summary if "summary" in entry else "No summary available.",
                "tags": [source.replace(" ", "_")],  # Tag it with the source name
            })

    # Save to posts.json
    with open("public/data/posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    fetch_rss()
    print("✅ RSS feed fetched and posts.json updated!")
