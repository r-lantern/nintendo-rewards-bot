from src import config as config
from src import consts as consts
from src import mynintendo as mynintendo
from src import reward as reward
from src.twitter import Twitter
from src.nintendo_db import NintendoDB


def main():
    req = mynintendo.get_store_request()
    new_products = mynintendo.get_rewards(req)

    nintendoDB = NintendoDB(config.DB_URI, config.DB_NINTENDO)

    product_deltas = {
        consts.STATUS_NEW: [],
        consts.STATUS_STOCK_IN: [],
        consts.STATUS_STOCK_OUT: [],
    }

    for new_product in new_products:
        old_product = nintendoDB.get_product_from_id(new_product["id"])
        old_stock = reward.get_stock(old_product)
        new_stock = reward.get_stock(new_product)

        if not old_product:
            product_deltas[consts.STATUS_NEW].append(new_product)
        elif old_stock is not None:
            if new_stock != old_stock:
                if new_stock:
                    product_deltas[consts.STATUS_STOCK_IN].append(new_product)
                else:
                    product_deltas[consts.STATUS_STOCK_OUT].append(new_product)

    nintendoDB.drop_and_insert(config.COLLECTION_REWARDS, new_products)

    twitter = Twitter()
    for key in product_deltas:
        for product in product_deltas[key]:
            metadata = reward.get_metadata(product)
            message = consts.TWEET_TEMPLATE.format(
                tag=consts.TAGS[key],
                title=metadata["title"],
                start_time=metadata["start_time"],
                end_time=metadata["end_time"],
                points_value=metadata["points_value"],
                points_type=metadata["points_type"],
                url=metadata["url"],
            )

            twitter.tweet(message)


if __name__ == "__main__":
    main()
