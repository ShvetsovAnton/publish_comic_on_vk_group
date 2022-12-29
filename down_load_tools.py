import os
import urllib.parse
from pathlib import Path
from urllib.parse import urlparse

import requests


def take_file_name_from_url(comic_url):
    url_path = urlparse(comic_url).path
    unquote_url_path = urllib.parse.unquote(url_path)
    file_name = os.path.split(unquote_url_path)[-1]
    return file_name


def download_image_in_folder(comic_url, file_name):
    response = requests.get(comic_url)
    response.raise_for_status()
    with open(file_name, "wb") as image:
        image.write(response.content)


def delete_published_comic(file_name):
    remove_image_path = Path.cwd() / file_name
    os.remove(path=remove_image_path)
