import logging
import colorlog

# ハンドラーを作成
handler = colorlog.StreamHandler()

# フォーマッターを作成（色の指定もここで）
formatter = colorlog.ColoredFormatter(
    "%(log_color)s[%(levelname)s] %(asctime)s - %(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    }
)

# ハンドラーにフォーマッターを設定
handler.setFormatter(formatter)

# ロガーを作成
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  # 出力するログのレベルを指定
