from os import environ

# 🔧 Bot Configuration Settings
# ⚙️ Get values from environment variables or use defaults

API_ID = int(environ.get("29481626", ""))
API_HASH = environ.get("4892185769903521077c4cea97808b8c", "")
BOT_TOKEN = environ.get("8619959255:AAFM9xBgLouwUMizDlTASIFbcHoCqD6gmkU", "")

# 👥 Authorized Users - Bot will work only with these users
AUTH_USERS = list(map(int, environ.get("AUTH_USERS", "5856009289 7456492367").split()))

# 👑 Owner/Admin ID - Multiple owners supported
OWNER_ID = list(map(int, environ.get("5856009289", "").split()))

# 📁 Download Directory - Where temporary files are stored
DOWNLOAD_DIRECTORY = environ.get("DOWNLOAD_DIRECTORY", "./downloads")

# 🏷️ Default Metadata - Video file metadata title
DEFAULT_METADATA = environ.get("DEFAULT_METADATA", "")

# 📄 Default Filename - Used when no filename is provided
DEFAULT_FILENAME = environ.get("DEFAULT_FILENAME", "Ls")

# 🌍 Timezone Configuration
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
