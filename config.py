# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("27972068"))
    API_HASH = os.environ.get("6e7e2f5cdddba536b8e603b3155223c1")
    BOT_TOKEN = os.environ.get("6993994399:AAEAZGdENHw9ileTSskRq4Xb78FedHjzGL4")
    LOGS_CHANNEL = int(os.environ.get("-1002041484396"))
    MONGODB_URL = os.environ.get("mongodb+srv://subhadeepsamui79:v3REnnLOfITn2p8t@cluster0.4z3invg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    BOT_OWNER = int(os.environ.get("6075512585"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
