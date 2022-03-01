from src import config as config
from src import consts as consts
import sys
import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

        self.api = tweepy.API(self.auth)
        self.api.verify_credentials()

    def post_long_tweet(self, msg: str) -> None:
        tweet_id = None
        for index in range(0, len(msg) - 1, consts.TWEET_MAX_LENGTH):
            tweet = self.api.update_status(
                status=msg[index : index + consts.TWEET_MAX_LENGTH],
                in_reply_to_status_id=tweet_id,
            )
            tweet_id = tweet.id

    def post_tweet(self, msg: str) -> None:
        try:
            if len(msg) - 1 > consts.TWEET_MAX_LENGTH:
                split_msg = msg.split("\n")
                url = split_msg[-1]
                new_msg = msg[: -1 * (len(url) - 1)]
                if len(new_msg) - 1 <= consts.TWEET_MAX_LENGTH:
                    tweet = self.api.update_status(new_msg)
                    if len(url) - 1 <= consts.TWEET_MAX_LENGTH:
                        self.api.update_status(url, in_reply_to_status_id=tweet.id)
                else:
                    self.post_long_tweet(msg)
            else:
                self.api.update_status(msg)

        except tweepy.errors.Forbidden as e:
            sys.stderr.write(e.args[0] + "\n")
            sys.stderr.write(msg + "\n")
