import os
import sys
from datetime import datetime

from loguru import logger

from config.config import Config


_run_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
_log_file = os.path.join(Config.LOG_DIR, f"log_{_run_stamp}_{os.getpid()}.log")
os.makedirs(Config.LOG_DIR, exist_ok=True)

logger.remove()

logger.add(
    sys.stderr,
    level=Config.LOG_LEVEL,
    format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <level>{message}</level>",
    colorize=True,
)

logger.add(
    _log_file,
    level=Config.LOG_LEVEL,
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {message}",
    encoding="utf-8",
    enqueue=True,
    backtrace=True,
    diagnose=False,
)


__all__ = ["logger"]
