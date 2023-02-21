import requests
import sys
import os

APP_KEY = "li9hYwSQhOg_b5q7gV8HkHJZSwZCCzlZsks71IrGif0"
BASE_URL = "https://api.unsplash.com"


def get_wallpaper(target_path):
    session = requests.session()
    params = {"client_id": APP_KEY, "orientation": "landscape"}
    resp = session.get(BASE_URL + "/photos/random/", params=params)
    full_url = resp.json()["urls"]["full"]
    image_resp = session.get(full_url)
    with open(target_path, "wb") as f:
        f.write(image_resp.content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    target_path = os.path.abspath(sys.argv[1])
    get_wallpaper(target_path)
