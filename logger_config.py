import logging
import sys

"""
logger: ログの生成に関するオブジェクト
handler: ログの出力に関するオブジェクト
formatter: ログの整形に関するオブジェクト
"""

# ロガーの生成
logger = logging.getLogger(__name__) # __name__でモジュール名を定義
logger.setLevel(logging.INFO) # ハンドラにログレベルを継承

# フォーマッターを生成
sh_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S")
fh_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S")

# 標準出力にログを出力するハンドラを生成
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO) # 標準出力用のハンドラはINFO以上

# ファイルにログを出力するハンドラを生成
fh = logging.FileHandler('log/sample.log')
fh.setLevel(logging.ERROR) # ファイル用のハンドラはERROR以上

# フォーマッターをハンドラに紐づける
sh.setFormatter(sh_fmt)
fh.setFormatter(fh_fmt)

# ハンドラをロガーに紐づける
logger.addHandler(sh)
logger.addHandler(fh)

class Test:
    def __init__(self):
        logger.info("this is a test")
        logger.error("this is a test")
