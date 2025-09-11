import logging
import colorlog
from logging import Logger, Handler, Formatter

# ---------------- コンソール出力用（色付き） ----------------
console_handler: Handler = colorlog.StreamHandler()
console_formatter: Formatter = colorlog.ColoredFormatter(
    "%(log_color)s[%(levelname)s] %(asctime)s - %(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    }
)
console_handler.setFormatter(console_formatter)

# ---------------- ファイル出力用 ----------------
file_handler: Handler = logging.FileHandler("app.log", encoding="utf-8")
file_formatter: Formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
file_handler.setFormatter(file_formatter)

# ---------------- ロガーを作成 ----------------
logger: Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# どちらのハンドラーも追加
logger.addHandler(console_handler)
logger.addHandler(file_handler)