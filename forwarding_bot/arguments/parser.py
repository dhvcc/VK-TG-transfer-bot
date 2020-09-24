import argparse
from forwarding_bot.__version__ import __version__


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="VK TG message forwarding bot",
            add_help=True)
        self.parser.add_argument("--version", help="print version info",
                                 action="version",
                                 version=f"rss-reader {__version__}")
        self.parser.add_argument("-b", "--bot-token", help="TG bot token",
                                 type=str)
        self.parser.add_argument("-g", "--group-token", help="VK group token",
                                 type=str)
        self.parser.add_argument("-s", "--source-id", help="VK source conversation id",
                                 type=int)
        self.parser.add_argument("-d", "--destination-id", help="TG destination conversation id",
                                 type=int)

    def get_args(self):
        return self.parser.parse_args()
