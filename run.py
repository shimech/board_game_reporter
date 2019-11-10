import sys
from datetime import datetime
from slacker import Slacker
from slackbot_settings import SlackbotSettings
from utils import Utils
from enums import BoardGameEnum
from models.googlespreadsheet_manager import GoogleSpreadSheetManager
from models.reporters import CatanReporter
from models.reporters import WingspanReporter


def main() -> None:
    """
    チャンネルにメッセージをポスト
    """
    print("Run Time: {}".format(datetime.today()))

    # CyberLabワークスペースのチャンネル設定
    cyberlab_channel = SlackbotSettings.CHANNEL
    argument = None  # オプション
    # オプションが付加されていた場合、その内容によってポストするチャンネルを切り替える
    if len(sys.argv) >= 2:
        argument = sys.argv[1]
        if argument in ["-t", "--test", "-d", "--debug"]:
            cyberlab_channel = SlackbotSettings.DEBUG_CHANNEL
    # オプションがなく、本番チャンネルにポストしようとする場合の確認
    if cyberlab_channel == SlackbotSettings.CHANNEL and argument not in ["-y", "--yes"]:
        is_continue = input("Post to Channel: {}. Is it OK? [y/n] >> ".format(SlackbotSettings.CHANNEL))
        if is_continue in ["y", "yes"]:
            pass
        else:
            cyberlab_channel = SlackbotSettings.DEBUG_CHANNEL
            print("Changed Channel to {}".format(SlackbotSettings.DEBUG_CHANNEL))

    # ワークスペースの設定
    cyberlab_slacker = Slacker(SlackbotSettings.API_TOKEN)
    my_slacker = Slacker(SlackbotSettings.MY_API_TOKEN)

    for board_game in BoardGameEnum:
        # ワークブックにアクセス
        workbook = GoogleSpreadSheetManager.get_workbook(board_game.spreadsheet_key)
        # レポートを取得
        report = board_game.reporter.make_report(workbook)
        print("Made {} report successfully.".format(board_game.name))

        # レポートをCyberLabと個人ワークスペースにポスト
        post_message(cyberlab_slacker, cyberlab_channel, report)
        post_message(my_slacker, SlackbotSettings.MY_CHANNEL, report)

        # 標準出力
        print("----- {} -----".format(board_game.name))
        print(report)
        print("\n")


def post_message(slacker: Slacker, channel: str, message: str) -> None:
    """
    メッセージをチャンネルにポスト
    @param slacker: ポストするワークスペース
    @param channel: ポストするチャンネル
    @param message: ポストするメッセージ
    """
    slacker.chat.post_message(
        channel,
        message
    )


if __name__ == "__main__":
    main()
