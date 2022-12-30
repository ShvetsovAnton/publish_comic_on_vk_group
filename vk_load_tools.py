import requests

from exception import VKError


def get_server_url(vk_api_key, group_id, vk_api_version):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    params = {
        "access_token": vk_api_key,
        "group_id": group_id,
        "v": vk_api_version
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    catching_error_from_vk_api(response.json())
    return response.json()["response"]["upload_url"]


def upload_comic_on_server(
        file_name, vk_access_token,
        group_id, upload_url, vk_api_version
):
    url = upload_url
    params = {
        "access_token": vk_access_token,
        "v": vk_api_version,
        "group_id": group_id,
    }
    with open(file_name, "rb") as file:
        files = {
            "photo": file,
        }
        response = requests.post(url, files=files, params=params)
    response.raise_for_status()
    catching_error_from_vk_api(response.json())
    return response.json()


def save_comic_in_album(
        vk_access_token, group_id, photo_parameters,
        server_id, photo_hash, vk_api_version
):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    params = {
        "access_token": vk_access_token,
        "v": vk_api_version,
        "group_id": group_id,
        "photo": photo_parameters,
        "server": server_id,
        "hash": photo_hash
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    catching_error_from_vk_api(response.json())
    return response.json()


def post_comic(
        vk_access_token, group_id, comic_comment,
        saved_comics_owner_id, saved_comics_media_id, vk_api_version
):
    url = "https://api.vk.com/method/wall.post"
    params = {
        "owner_id": -group_id,
        "access_token": vk_access_token,
        "v": vk_api_version,
        "message": comic_comment,
        "from_group": 1,
        "attachments": f"photo{saved_comics_owner_id}_{saved_comics_media_id}"
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    catching_error_from_vk_api(response.json())
    return response.json()


def catching_error_from_vk_api(vk_response):
    if "error" in vk_response:
        raise VKError(
            f'Error code - {vk_response["error"]["error_code"]}',
            f'Error descript - {vk_response["error"]["error_msg"]}',
        )
