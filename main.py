import os

from dotenv import load_dotenv

from down_load_tools import download_random_comic
from down_load_tools import delete_comic
from vk_load_tools import get_server_url
from vk_load_tools import post_comic
from vk_load_tools import save_comic_in_album
from vk_load_tools import upload_comic_on_server


def main():
    load_dotenv()
    vk_access_token = os.environ["VK_ACCESS_TOKEN"]
    group_id = int(os.environ["VK_GROUP_ID"])
    vk_api_version = 5.131
    file_name_and_comic_comment = download_random_comic()
    file_name = file_name_and_comic_comment["file_name"]
    comic_comment = file_name_and_comic_comment["comic_comment"]
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
        delete_comic(file_name)


if __name__ == "__main__":
    main()
