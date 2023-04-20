# (©)Codexbotz
# Recife By Zaen #Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6118968145:AAGvfCyKbgHJyDfWKEBQsuiApLh485BAsDA")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11662467"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "325e13dfb76973f4bca9bdae2678bbbe")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001612655312"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5178772086"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "xyzuzux")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://txxsmyof:b99F5n0mIL1ND8-uGHSTMwq73_mRSkgd@john.db.elephantsql.com/txxsmyof")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Tolak_Ange")
GROUP = os.environ.get("GROUP", "Tolak_Ange")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5178772086").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)
ADMINS.append(2010825200)
ADMINS.append(1750080384)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
