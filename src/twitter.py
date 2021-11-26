from src import config as config
import tweepy


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
        self.auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

        self.api = tweepy.API(self.auth)
        self.api.verify_credentials()

    def tweet(self, msg: str) -> None:
        self.api.update_status(msg)
