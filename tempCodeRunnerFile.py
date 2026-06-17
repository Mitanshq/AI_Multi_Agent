import requests

def wiki_search(query):
    # Search
    search_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }

    search_data = requests.get(search_url, params=params).json()

    results = search_data["query"]["search"]

    if not results:
        return "No results found"

    title = results[0]["title"]

    # Get summary
    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

    headers = {
        "User-Agent": "ResearchAgent/1.0"
    }

    summary_data = requests.get(
        summary_url,
        headers=headers
    ).json()

    return {
        "title": summary_data.get("title"),
        "summary": summary_data.get("extract"),
        "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    }

print(wiki_search("healthcare"))