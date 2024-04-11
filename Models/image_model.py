# this model will get the images from url and at some point will post the image bit to an ai tagging service
import requests

class ImageModel:
    def get_image(self, url: str) -> bytes:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content

    # def post_image(self, image: bytes):
    #     pass

