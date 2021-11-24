from src import config as config
from src import consts as consts
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


if __name__ == "__main__":
    main()
