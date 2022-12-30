import os
import random
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import unquote

import requests


def download_random_comic():
    first_comic = 1
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comics_total_number = response.json()["num"]
    comic_number = random.randint(first_comic, comics_total_number)
    random_comic_url = f"https://xkcd.com/{comic_number}/info.0.json"
    random_comic_response = requests.get(random_comic_url)
    random_comic_response.raise_for_status()
    random_comic_description = random_comic_response.json()
    comic_comment = random_comic_description["alt"]
    downloading_comic_url = random_comic_description["img"]
    comic_response = requests.get(downloading_comic_url)
    url_path = urlparse(downloading_comic_url).path
    unquote_url_path = unquote(url_path)
    file_name = os.path.split(unquote_url_path)[-1]
    with open(file_name, "wb") as image:
        image.write(comic_response.content)
    return {
        "file_name": file_name,
        "comic_comment": comic_comment
    }


def delete_comic(file_name):
    remove_image_path = Path.cwd() / file_name
    os.remove(path=remove_image_path)



