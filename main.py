from typing import List
from src import config as config
from src import mynintendo as mynintendo
from src.twitter import Twitter
from src.database import Database


def main():
    req = mynintendo.get_store_request()
    new_products = mynintendo.get_rewards(req)

    nintendoDB = Database(config.DB_URI, config.DB_NINTENDO)

    twitter = Twitter()


if __name__ == "__main__":
    main()
