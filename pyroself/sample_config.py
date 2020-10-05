import os

class Config():
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 1891006))
    API_HASH = os.environ.get("API_HASH", "544212aa9f34df3883da6cc0fdc9aed1")
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", None)
    MAX_MESSAGE_LENGTH = 4096
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads")
    OFFICIAL_UPSTREAM_REPO = os.environ.get("OFFICIAL_UPSTREAM_REPO","https://github.com/PiniGerteam/PyroSelf.git")
    DB_URI = os.environ.get("DATABASE_URL", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", "281795085"))
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "281795085").split())
    TG_MAX_SELECT_LEN = int(os.environ.get("TG_MAX_SELECT_LEN", "100"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    OWNER_NAME = os.environ.get("OWNER_NAME", "Sigaris xD")
    GBAN_GROUP = int(os.environ.get("GBAN_GROUP", -100))
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID", -100))
    PM_PERMIT = bool(os.environ.get("PM_PERMIT", False))
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/opt/google/chrome/chrome")
    REMBG_API_KEY = os.environ.get("REMBG_API_KEY", None)

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
