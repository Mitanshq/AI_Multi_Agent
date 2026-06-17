import requests
from urllib.parse import quote

def wiki_search(query):
    try:
        # Search Wikipedia
        search_url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        search_response = requests.get(
            search_url,
            params=params,
            headers=headers,
            timeout=10
        )

        search_response.raise_for_status()

        search_data = search_response.json()

        results = search_data["query"]["search"]

        if not results:
            return "No results found"

        title = results[0]["title"]

        # Get page summary
        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + quote(title)
        )

        summary_response = requests.get(
            summary_url,
            headers=headers,
            timeout=10
        )

        # If summary endpoint fails, return basic info
        if summary_response.status_code != 200:
            return {
                "title": title,
                "summary": "Summary unavailable",
                "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            }

        summary_data = summary_response.json()

        return {
            "title": summary_data.get("title", title),
            "summary": summary_data.get("extract", "No summary available"),
            "url": f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
        }

    except Exception as e:
        print("Error Type:", type(e))
        print("Error:", e)
        return None

