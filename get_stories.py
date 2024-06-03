import requests


TOP_STORIES_API_ENDPOINT = "https://hn.algolia.com/api/v1/search?query=front_page"


def get_stories():
    r = requests.get(TOP_STORIES_API_ENDPOINT)
    if (r.status_code != 200):
        return

    result = r.json()
    print(len(result["hits"]))
    for article in result["hits"]:
        print(article["title"])
