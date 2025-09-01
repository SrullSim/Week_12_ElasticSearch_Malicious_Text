from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).parent.parent
APP_DIR = PROJECT_ROOT / "src"
DATA_DIR = PROJECT_ROOT / "data"
CONFIG_DIR = PROJECT_ROOT / "config"
PATH_TO_DATA = DATA_DIR / "tweets_injected 3.csv"
PATH_TO_WEAPONS_LIST = DATA_DIR / "weapon_list.txt"




SETTINGS_FILE_PATH = CONFIG_DIR / "settings.json"
try:
    with open(SETTINGS_FILE_PATH, 'r') as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {}
    print(f"WARNING: Configuration file not found at {SETTINGS_FILE_PATH}. Using defaults.")


API_TITLE = settings.get("API_TITLE", "Default API")
API_DESCRIPTION = settings.get("API_DESCRIPTION", "A default API description.")
API_VERSION = settings.get("API_VERSION", "1.0.0")
URL_ELASTIC = settings.get("URL_ELASTIC", "http://localhost:9200")