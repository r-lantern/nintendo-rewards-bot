from src import consts as consts
from src.reward import Reward


def get_name(product: dict) -> str:
    return product["name"]


def get_url(product: dict) -> str:
    return consts.URI_STORE_PRODUCTS + product["urlKey"]


def get_cost(product: dict) -> str:
    return product["platinumPoints"] + " Platinum Points"


def build_tweet(reward: Reward) -> str:
    data = reward.data
    msg = consts.TWEET_PHYSICAL_REWARDS_TEMPLATE.format(
        status=reward.status,
        name=get_name(data),
        cost=get_cost(data),
        url=get_url(data),
    )
    return msg
