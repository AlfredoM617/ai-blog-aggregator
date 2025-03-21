import feedparser
import json
from datetime import datetime

RSS_FEEDS = {
    "AWS ML Blog": "https://aws.amazon.com/blogs/machine-learning/feed/",
    "Hacker News AI": "https://hnrss.org/newest?q=ai",
    "Towards Data Science": "https://towardsdatascience.com/feed",
    "MIT Tech Review AI": "https://www.technologyreview.com/feed/",
    "DeepMind": "https://deepmind.google/blog/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "LangChain": "https://blog.langchain.dev/rss/",
    "LlamaIndex": "https://www.llamaindex.ai/blog/feed",
    "Microsoft AI": "https://www.microsoft.com/en-us/ai/blog/feed/"
}

TAG_MAP = {
    "AWS ML Blog": "AWS",
    "Hacker News AI": "HackerNews",
    "Towards Data Science": "TDS",
    "MIT Tech Review AI": "MIT",
    "DeepMind": "DeepMind",
    "Hugging Face": "HuggingFace",
    "LangChain": "LangChain",
    "LlamaIndex": "LlamaIndex",
    "Microsoft AI": "Microsoft"
}

def fetch_rss():
    posts = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        entries = feed.entries
        print(f"📡 {source}: {len(entries)} entries fetched")

        for entry in entries[:5]:
            tag = TAG_MAP.get(source, source.replace(" ", "_"))
            posts.append({
                "title": entry.title,
                "source": source,
                "url": entry.link,
                "published": entry.published if "published" in entry else datetime.now().isoformat(),
                "summary": entry.summary if "summary" in entry else "No summary available.",
                "tags": [tag],
            })

    output = {
        "last_updated": datetime.now().isoformat(),
        "posts": sorted(posts, key=lambda p: p["published"], reverse=True)
    }

    with open("public/data/posts.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print("✅ RSS feed fetched and posts.json updated!")

if __name__ == "__main__":
    fetch_rss()
