# bot.py（サンプル）

import os
import tweepy

def main():
    auth = tweepy.OAuth1UserHandler(
        os.environ["API_KEY"],
        os.environ["API_SECRET"],
        os.environ["ACCESS_TOKEN"],
        os.environ["ACCESS_TOKEN_SECRET"]
    )
    api = tweepy.API(auth)
    api.update_status("こんにちは、ひらがなボットです。")

if __name__ == "__main__":
    main()
