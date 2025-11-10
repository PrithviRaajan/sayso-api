import logging
from logging.handlers import RotatingFileHandler
import sys
from datetime import datetime


LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
LOG_FILE = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"

# Create logger
logger = logging.getLogger("MiniTweet")
logger.setLevel(logging.INFO)

# Console Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# File Handler (rotating)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Attach handlers (avoid duplication)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


