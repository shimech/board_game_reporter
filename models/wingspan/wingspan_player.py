import gspread


class WingspanPlayer:
    """
    WINGSPANのプレイヤ情報を保持するクラス
    """
    def __init__(self, row: int) -> None:
        """
        インスタンスの初期化関数
        @param row: 行番号
        """
        self.row = row            # 行番号
        self.name = None          # プレイヤ名
        self.num_game = None      # 試合数
        self.num_win = None       # 勝利数
        self.winning_rate = None  # 勝率
        self.average = None       # 平均スコア
        self.message = None       # メッセージ

    def get_name(self, worksheet: gspread.models.Worksheet) -> str:
        """
        プレイヤ名を取得
        @param worksheet: ワークシートオブジェクト
        @return name: プレイヤ名
        """
        name = worksheet.cell(self.row, 1).value
        self.name = name
        return name

    def get_results(self, worksheet: gspread.models.Worksheet) -> (int, int, float, str):
        """
        プレイヤの戦績を取得
        @param worksheet: ワークシートオブジェクト
        @return num_game: 試合数
        @return num_win: 勝利数
        @return winning_rate: 勝率
        @return average: 平均スコア
        """
        num_game = int(worksheet.cell(self.row, 2).value)
        num_win = int(worksheet.cell(self.row, 3).value)
        winning_rate = None
        average = worksheet.cell(self.row, 11).value

        if num_game > 0:
            winning_rate = num_win / num_game

        self.num_game = num_game
        self.num_win = num_win
        self.winning_rate = winning_rate
        self.average = average

        return num_game, num_win, winning_rate, average

    def make_message(self) -> str:
        """
        メッセージの作成
        @return message: メッセージ
        """
        if self.winning_rate is None:
            message = "{}: No Data".format(self.name)
        else:
            message = "{}: {:.1%} ({}戦{}勝) | 平均スコア {}".format(self.name, self.winning_rate, self.num_game, self.num_win, self.average)
        self.message = message
        return message
