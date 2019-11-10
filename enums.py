from enum import Enum
from models.reporters import CatanReporter
from models.reporters import WingspanReporter


class BoardGameEnum(Enum):
    """
    ボードゲームの列挙型
    """
    # BOARD_GAME_NAME = (
    #     bg_id: int,                   # ボードゲームID
    #     bg_name: str,                 # ボードゲーム名
    #     spreadsheet_key: str,         # スプレッドシートキー
    #     reporter: {bg_name}Reporter,  # レポータークラス
    # )
    CATAN = (
        0,
        "CATAN",
        "TODO: Google Spread Sheetのキー",
        CatanReporter,
    )
    WINGSPAN = (
        1,
        "WINGSPAN",
        "TODO: Google Spread Sheetのキー",
        WingspanReporter,
    )

    def __init__(self,
        bg_id: int,
        bg_name: str,
        spreadsheet_key: str,
        reporter: "{bg_name}Reporter"
    ) -> None:
        """
        初期化関数
        """
        self.bg_id = bg_id
        self.bg_name = bg_name
        self.spreadsheet_key = spreadsheet_key
        self.reporter = reporter
