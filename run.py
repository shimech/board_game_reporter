import sys
from datetime import datetime
from time import sleep
from slacker import Slacker
from slackbot_settings import SlackbotSettings
from utils import Utils
from models.reporters import CatanReporter
from models.reporters import WingspanReporter


SLEEP_TIME_SEC = 60


def main() -> None:
    """
    チャンネルにメッセージをポスト
    """
    print("Run Time: {}".format(datetime.today()))

    # CyberLabワークスペースのチャンネル設定
    cyberlab_channel = SlackbotSettings.CHANNEL
    argument = None  # オプション
    if len(sys.argv) >= 2:
        argument = sys.argv[1]
        if argument in ["-t", "--test", "-d", "--debug"]:
            cyberlab_channel = SlackbotSettings.DEBUG_CHANNEL
    if cyberlab_channel == SlackbotSettings.CHANNEL and argument not in ["-y", "--yes"]:
        is_continue = input("Post to Channel: {}. Is it OK? [y/n] >> ".format(SlackbotSettings.CHANNEL))
        if is_continue in ["y", "yes"]:
            pass
        else:
            cyberlab_channel = SlackbotSettings.DEBUG_CHANNEL
            print("Changed Channel to {}".format(SlackbotSettings.DEBUG_CHANNEL))

    # CATANレポートの取得
    catan_report = CatanReporter.make_report()
    print("Made CATAN report successfully.")

    sleep(SLEEP_TIME_SEC)

    # WINGSPANレポートの取得
    wingspan_report = WingspanReporter.make_report()
    print("Made WINGSPAN report successfully.")

    # CyberLabにメッセージを投稿
    cyberlab_slacker = Slacker(SlackbotSettings.API_TOKEN)
    # CATANのレポート
    cyberlab_slacker.chat.post_message(
        cyberlab_channel,
        catan_report,
    )
    # WINGSPANのレポート
    cyberlab_slacker.chat.post_message(
        cyberlab_channel,
        wingspan_report,
    )


    # 個人ワークスペースにメッセージを投稿
    my_slacker = Slacker(SlackbotSettings.MY_API_TOKEN)
    # CATANのレポート
    my_slacker.chat.post_message(
        SlackbotSettings.MY_CHANNEL,
        catan_report,
    )
    # WINGSPANのレポート
    my_slacker.chat.post_message(
        SlackbotSettings.MY_CHANNEL,
        wingspan_report,
    )

    # 標準出力
    print("---- CATAN -----")
    print(catan_report)
    print("----------------")

    print("--- WINGSPAN ---")
    print(wingspan_report)
    print("----------------")
    print("\n")


if __name__ == "__main__":
    main()
