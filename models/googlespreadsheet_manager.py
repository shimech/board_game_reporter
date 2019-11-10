import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheetManager:
    SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    BOARD_GAME_REPORTER_PATH = "TODO: このアプリケーションのルートパス"
    JSON_PATH = os.path.join(BOARD_GAME_REPORTER_PATH, "models/Google APIのJSONファイル")
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, SCOPE)
    GC = gspread.authorize(CREDENTIALS)

    @classmethod
    def get_workbook(cls, spreadsheet_key: str) -> gspread.models.Spreadsheet:
        """
        ワークブックを取得
        @param spreadsheet_key: スプレッドシートキー
        @return workbook: ワークブックインスタンス
        """
        workbook = cls.GC.open_by_key(spreadsheet_key)
        return workbook
