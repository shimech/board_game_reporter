import os
import sys
sys.path.append(os.getcwd())

from utils import Utils
from models.catan.catan_report_manager import CatanReportManager
from models.wingspan.wingspan_report_manager import WingspanReportManager


class CatanReporter:
    @staticmethod
    def make_report() -> str:
        """
        CATANのレポートを生成
        @return report: CATANの戦績レポート
        """
        players = CatanReportManager().catan_players()
        if len(players) == 0:
            report = "あれっ、先月は開拓しなかったみたいですね..."
        else:
            year, month = Utils.target_year_and_month()
            report = "{}年{:02}月のCATANの戦績です。".format(year, month) + "\n"
            report += "```" + "\n"
            for player in players:
                report += player.message + "\n"
            report += "```" + "\n"
            report += "{}さん強すぎバロタ".format(players[0].name)
        return report


class WingspanReporter:
    @staticmethod
    def make_report():
        """
        WINGSPANのレポートを作成
        @return report: WINGSPANの戦績レポート
        """
        players = WingspanReportManager().wingspan_players()
        if len(players) == 0:
            report = "あれっ、先月は鳥と遊ばなかったんですね..."
        else:
            year, month = Utils.target_year_and_month()
            report = "{}年{:02}月のWINGSPANの戦績です。".format(year, month) + "\n"
            report += "```" + "\n"
            for player in players:
                report += player.message + "\n"
            report += "```" + "\n"
            report += "{}さんが最強の鳥使い！".format(players[0].name)
        return report
