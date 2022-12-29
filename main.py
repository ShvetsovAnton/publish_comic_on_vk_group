import os
import random

import requests
from dotenv import load_dotenv

from down_load_tools import delete_published_comic
from down_load_tools import download_image_in_folder
from down_load_tools import take_file_name_from_url
from vk_load_tools import get_server_url
from vk_load_tools import post_comic
from vk_load_tools import save_comic_in_album
from vk_load_tools import upload_comic_on_server


def get_total_number_comics():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    return response.json()["num"]


def get_comic_description(comic_number):
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    vk_access_token = os.environ["VK_ACCESS_TOKEN"]
    group_id = int(os.environ["VK_GROUP_ID"])
    vk_api_version = 5.131
    comics_total_number = get_total_number_comics()
    first_comic = 1
    comic_number = random.randint(first_comic, comics_total_number)
    comic_description = get_comic_description(comic_number)
    comic_url = comic_description["img"]
    comic_comment = comic_description["alt"]
    file_name = take_file_name_from_url(comic_url)
    download_image_in_folder(comic_url, file_name)
    try:
        upload_url = get_server_url(
            vk_access_token,
            group_id,
            vk_api_version
        )
        uploaded_comic_description = upload_comic_on_server(
            file_name,
            vk_access_token,
            group_id,
            upload_url,
            vk_api_version
        )
        server_id = uploaded_comic_description["server"]
        photo_parameters = uploaded_comic_description["photo"]
        photo_hash = uploaded_comic_description["hash"]
        saved_comic_description = save_comic_in_album(
            vk_access_token,
            group_id,
            photo_parameters,
            server_id,
            photo_hash,
            vk_api_version
        )
        saved_comic_owner_id = \
            saved_comic_description["response"][0]["owner_id"]
        saved_comic_media_id = saved_comic_description["response"][0]["id"]
        post_comic(
            vk_access_token,
            group_id,
            comic_comment,
            saved_comic_owner_id,
            saved_comic_media_id,
            vk_api_version
        )
    finally:
        delete_published_comic(file_name)


if __name__ == "__main__":
    main()
