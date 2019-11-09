from datetime import datetime
from dateutil.relativedelta import relativedelta
import gspread


class Utils:
    @staticmethod
    def target_year_and_month() -> (int, int):
        """
        現在から1ヶ月前の年月を取得
        @return year: 年
        @return month: 月
        """
        one_month_ago = datetime.today() - relativedelta(months=1)
        return one_month_ago.year, one_month_ago.month

    @staticmethod
    def get_worksheet(workbook: gspread.models.Spreadsheet, sheet_name: str) -> gspread.models.Worksheet:
        """
        指定した名前のワークシートを取得
        @param workbook: ワークブック
        @param sheet_name: ワークシート名
        @return worksheet: ワークシートオブジェクト
        """
        worksheet = workbook.worksheet(sheet_name)
        return worksheet
