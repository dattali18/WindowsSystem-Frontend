# this model will get the images from url and at some point will post the image bit to an ai tagging service
import requests

from .config import API_KEY, API_SECRET

IMAGGA_API_ENDPOINT = "https://api.imagga.com"

class ImageModel:
    def get_image(self, url: str) -> bytes:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content

    def post_image(self, image: bytes) -> list[str]:
        url = f"{IMAGGA_API_ENDPOINT}/v2/tags"

        auth = (API_KEY, API_SECRET)
        files = {"image": image}

        response = requests.post(url, files=files, auth=auth)

        # parse the response
        if response.status_code == 200:
            data = response.json()
            tags = data["result"]["tags"]
            return [tag["tag"]["en"] for tag in tags]
        else:
            return None
