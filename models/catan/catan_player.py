import gspread


class CatanPlayer:
    """
    CATANのプレイヤ情報を保持するクラス
    """
    def __init__(self, column: int) -> None:
        """
        インスタンスの初期化関数
        @param column: カラム番号
        """
        self.column = column      # カラム番号
        self.name = None          # プレイヤ名
        self.num_game = None      # 試合数
        self.num_win = None       # 勝利数
        self.winning_rate = None  # 勝率
        self.message = None       # メッセージ

    def get_name(self, worksheet: gspread.models.Worksheet) -> str:
        """
        プレイヤ名を取得
        @param worksheet: ワークシートオブジェクト
        @return name: プレイヤ名
        """
        name = worksheet.cell(1, self.column).value
        self.name = name
        return name

    def get_results(self, worksheet: gspread.models.Worksheet) -> (int, int, float):
        """
        プレイヤの戦績を取得
        @param worksheet: ワークシートオブジェクト
        @return num_game: 試合数
        @return num_win: 勝利数
        @return winning_rate: 勝率
        """
        num_game = int(worksheet.cell(2, self.column).value)
        num_win = int(worksheet.cell(6, self.column).value)
        winning_rate = None

        if num_game > 0:
            winning_rate = num_win / num_game

        self.num_game = num_game
        self.num_win = num_win
        self.winning_rate = winning_rate

        return num_game, num_win, winning_rate

    def make_message(self) -> str:
        """
        メッセージの作成
        @return message: メッセージ
        """
        if self.winning_rate is None:
            message = "{}: No Data".format(self.name)
        else:
            message = "{}: {:.1%} ({}戦{}勝)".format(self.name, self.winning_rate, self.num_game, self.num_win)
        self.message = message
        return message
