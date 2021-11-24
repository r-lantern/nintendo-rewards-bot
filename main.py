from src import config as config
from src import consts as consts
from src import utils as utils
from src import mynintendo as mynintendo
from src.twitter import Twitter
from src.database import Database


def main():
    req = mynintendo.get_store_request()
    new_products = mynintendo.get_rewards(req)

    nintendoDB = Database(config.DB_URI, config.DB_NINTENDO)

    product_deltas = {
        consts.STATUS_NEW: [],
        consts.STATUS_STOCK_IN: [],
        consts.STATUS_STOCK_OUT: [],
    }

    for product in new_products:
        old_product = nintendoDB.db[config.COLLECTION_REWARDS].find_one(
            {"id": product["id"]}
        )

        if not old_product:
            product_deltas[consts.STATUS_NEW].append(product)

        elif "stock" in old_product:
            if product["stock"]["available"] != old_product["stock"]["available"]:
                if product["stock"]["available"] is True:
                    product_deltas[consts.STATUS_STOCK_IN].append(product)
                else:
                    product_deltas[consts.STATUS_STOCK_OUT].append(product)

    nintendoDB.override_collection(config.COLLECTION_REWARDS, new_products)

    twitter = Twitter()
    for key in product_deltas:
        for product in product_deltas[key]:

            # endsAt is an optional key
            end_time = ""
            if product["endsAt"]:
                end_time = utils.convert_time(product["endsAt"])

            # points type in one of two locations
            if "key" not in product["points"][0]:
                points_type = product["points"][0]["category"]
            else:
                points_type = product["points"][0]["key"]

            message = consts.TWEET_TEMPLATE.format(
                tag=consts.TAGS[key],
                title=product["title"],
                start_time=utils.convert_time(product["beginsAt"]),
                end_time=end_time,
                points_value=product["points"][0]["amount"],
                points_type=points_type.replace("_", " ").title(),
                url=product["links"]["myNintendo"]["href"],
            )

            twitter.tweet(message)


if __name__ == "__main__":
    main()
