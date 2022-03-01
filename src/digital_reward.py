from src import consts as consts
from src import utils
from src.reward import Reward


def get_title(product: dict) -> str:
    return product["title"]


def get_start_time(product: dict) -> str:
    return utils.convert_time(product["beginsAt"])


def get_end_time(product: dict) -> str:
    end_time = "Undefined"
    if product["endsAt"]:
        end_time = utils.convert_time(product["endsAt"])
    return end_time


def get_category(product: dict) -> str:
    return product["category"].replace("_", " ").title()


def get_points_value(product: dict) -> str:
    return product["points"][0]["amount"]


def get_points_type(product: dict) -> str:
    # points type in one of two locations
    if "key" not in product["points"][0]:
        points_type = product["points"][0]["category"]
    else:
        points_type = product["points"][0]["key"]
    return points_type.replace("_", " ").title()


def get_url(product: dict) -> str:
    return product["links"]["myNintendo"]["href"]


def get_stock(product: dict) -> bool:
    if "stock" in product:
        return product["stock"]["available"]
    return None


def build_tweet(tag: str, reward: Reward) -> str:
    data = reward.data
    msg = consts.TWEET_DIGITAL_REWARDS_TEMPLATE.format(
        tag=consts.STATUS_NEW,
        title=get_title(data),
        start_time=get_start_time(data),
        end_time=get_end_time(data),
        category=get_category(data),
        points_value=get_points_value(data),
        points_type=get_points_type(data),
        url=get_url(data),
    )
    return msg
