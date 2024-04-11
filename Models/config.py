PORT: int = 5062
BASE_URL: str = f"http://localhost:{PORT}/api"

API_KEY: str = ""
API_SECRET: str = ""

# import the api_key and secret_key from .config.json file
import json
from os import path

# path to .config.json file
# the file is in the root of the project
config_path = path.join(path.dirname(__name__), ".config.json")


with open(config_path) as f:
    config = json.load(f)
    # reading the api_key and secret_key from the config file
    API_KEY = config["api_key"]
    API_SECRET = config["api_secret"]


