import feedparser
import json
from datetime import datetime

# RSS feed sources and their URLs
RSS_FEEDS = {
    "Google AI": "https://ai.googleblog.com/feeds/posts/default?alt=rss",
    "AWS ML Blog": "https://aws.amazon.com/blogs/machine-learning/feed/",
    "Hugging Face": "https://huggingface.co/blog/rss",
    "Microsoft AI": "https://techcommunity.microsoft.com/rss/ai-cognitive-services-bg-p/AzureAICognitiveServicesBlog",
}

# Map source names to clean, human-readable tags
TAG_MAP = {
    "Google AI": "Google",
    "AWS ML Blog": "AWS",
    "Hugging Face": "HuggingFace",
    "Microsoft AI": "Microsoft",
}

def fetch_rss():
    posts = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:  # Limit to latest 5 posts per source
            tag = TAG_MAP.get(source, source.replace(" ", "_"))

            posts.append({
                "title": entry.title,
                "source": source,
                "url": entry.link,
                "published": entry.published if "published" in entry else datetime.now().isoformat(),
                "summary": entry.summary if "summary" in entry else "No summary available.",
                "tags": [tag],  # Clean tag
            })

    # Write results to posts.json
    with open("public/data/posts.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)

    print("✅ RSS feed fetched and posts.json updated!")

if __name__ == "__main__":
    fetch_rss()
