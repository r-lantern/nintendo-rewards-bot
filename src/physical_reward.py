from src import consts as consts
from src import utils as utils
from src.reward import Reward


def get_name(product: dict) -> str:
    return product["name"]


def get_url(product: dict) -> str:
    return consts.URI_STORE_PRODUCTS + product["urlKey"]


def get_cost(product: dict) -> str:
    return product["platinumPoints"]


def build_tweet(reward: Reward) -> str:
    data = reward.data
    msg = consts.TWEET_REWARDS_TEMPLATE.format(
        status=reward.status,
        title=get_name(data),
        start_time=utils.format_time(utils.get_date()),
        end_time="Undefined",
        category="My Nintendo Store",
        points_value=get_cost(data),
        points_type="Platinum",
        url=get_url(data),
    )
    return msg
