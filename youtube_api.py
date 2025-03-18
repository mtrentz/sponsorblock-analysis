import requests
import requests_cache
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YT_API_KEY")

# Cache responses indefinitely
# Can I make this print for every cache miss?!
requests_cache.install_cache("youtube_cache", expire_after=None)


def get_channel_name(channel_id: str) -> str:
    url = (
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet&id={channel_id}&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    try:
        return data.get("items", [])[0].get("snippet", {}).get("title", "")
    except (IndexError, AttributeError):
        return ""


def get_channel_country(channel_id: str) -> str:
    url = (
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet&id={channel_id}&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    try:
        return data.get("items", [])[0].get("snippet", {}).get("country", "")
    except (IndexError, AttributeError):
        return ""


def get_channel_small_thumbnail(channel_id: str) -> str:
    url = (
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet&id={channel_id}&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    try:
        return (
            data.get("items", [])[0]
            .get("snippet", {})
            .get("thumbnails", {})
            .get("default", {})
            .get("url", "")
        )
    except (IndexError, AttributeError):
        return ""


if __name__ == "__main__":
    id = "UCfk5MMR4k6ulPmvvzkGe5kg"

    # get thumbnail
    print(get_channel_small_thumbnail(id))
