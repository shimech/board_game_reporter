import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSpreadSheetInformation:
    SCOPE = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    BOARD_GAME_REPORTER_PATH = "TODO: このアプリケーションのルートパス"
    JSON_PATH = os.path.join(BOARD_GAME_REPORTER_PATH, "models/TODO: Google APIのJSONファイル名")
    CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, SCOPE)
    GC = gspread.authorize(CREDENTIALS)


class CatanSheetInformation(GoogleSpreadSheetInformation):
    SPREADSHEET_KEY = "TODO: Google Spread Sheetのキー"
    WORKBOOK = GoogleSpreadSheetInformation.GC.open_by_key(SPREADSHEET_KEY)


class WingspanSheetInformation(GoogleSpreadSheetInformation):
    SPREADSHEET_KEY = "TODO: Google Spread Sheetのキー"
    WORKBOOK = GoogleSpreadSheetInformation.GC.open_by_key(SPREADSHEET_KEY)
