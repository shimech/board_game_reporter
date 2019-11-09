import os
import sys
sys.path.append(os.getcwd())

import gspread
from utils import Utils
from models.googlespreadsheet_information import WingspanSheetInformation
from models.wingspan.wingspan_player import WingspanPlayer


class WingspanReportManager:
    """
    WINGSPANのレポートを管理するクラス
    """
    MAX_NUM_PLAYER = 30

    def wingspan_players(self) -> list:
        """
        すべてのプレイヤの情報を取得
        @return players: すべてのプレイヤリスト
        """
        year, month = Utils.target_year_and_month()
        sheet_name = "{}/{:02}".format(year, month)
        try:
            worksheet = Utils.get_worksheet(WingspanSheetInformation.WORKBOOK, sheet_name)
            players = self.init_players(worksheet)
            players = self.get_result_of_players(players, worksheet)
            players = self.make_messages(players)
            players = sorted(players, key=lambda x: (-x.winning_rate, -float(x.average), -x.num_game))
        except gspread.exceptions.WorksheetNotFound:
            print("gspread.exceptions.WorksheetNotFound: {}".format(sheet_name))
            players = list()
        return players

    def init_players(self, worksheet: gspread.models.Worksheet) -> list:
        """
        すべての初期化されたプレイヤリストを取得
        @param worksheet: ワークシートオブジェクト
        @return players: すべてのプレイヤリスト
        """
        players = list()
        start = 3
        for i in range(self.MAX_NUM_PLAYER):
            row = start + i
            player = WingspanPlayer(row)
            name = player.get_name(worksheet)
            if name != "":
                players.append(player)
            else:
                break
        return players

    def get_result_of_players(self, players: list, worksheet: gspread.models.Worksheet) -> list:
        """
        すべてのプレイヤの戦績を取得
        対戦のないプレイヤは削除する。
        @param players: プレイヤリスト
        @param worksheet: ワークシートオブジェクト
        @return players_new: 更新後プレイヤリスト
        """
        players_new = list()
        for player in players:
            _, _, winning_rate, _ = player.get_results(worksheet)
            if winning_rate is not None:
                players_new.append(player)
        return players_new

    def make_messages(self, players: list) -> list:
        """
        全プレイヤのメッセージを生成
        @param @return players: 全プレイヤリスト
        """
        for player in players:
            _ = player.make_message()
        return players


if __name__ == "__main__":
    players = WingspanReportManager().wingspan_players()
    for player in players:
        print(player.message)
