from src.reward import Reward
from src import config as config
from src import consts as consts
from src import mynintendo as mynintendo
from src import digital_reward as digital_reward
from src import physical_reward as physical_reward
from src.twitter import Twitter
from src.nintendo_db import NintendoDB


def main():
    new_digital_rewards = mynintendo.get_digital_rewards()
    new_physical_rewards = mynintendo.get_physical_rewards()

    nintendoDB = NintendoDB(config.DB_URI, config.DB_NINTENDO)

    digital_reward_deltas = set()
    physical_reward_deltas = set()

    for new_digital_reward in new_digital_rewards:
        old_digital_reward = nintendoDB.get_product_from_id(new_digital_reward["id"])
        if not old_digital_reward:
            reward = Reward(new_digital_reward)
            digital_reward_deltas.add(reward)

    for new_physical_reward in new_physical_rewards:
        sku = new_physical_reward["sku"]
        old_physical_reward = nintendoDB.get_product_from_sku(sku)
        if not old_physical_reward:
            reward = Reward(new_physical_reward)
            if nintendoDB.is_product_restock(sku):
                reward.status = consts.STATUS_RESTOCKED
            else:
                nintendoDB.insert_one(config.COLLECTION_PHYSICAL_SKU, {"sku": sku})
            physical_reward_deltas.add(reward)

    twitter = Twitter()
    for reward in digital_reward_deltas:
        msg = digital_reward.build_tweet(reward)
        twitter.post_tweet(msg)
    nintendoDB.drop_and_insert(config.COLLECTION_DIGITAL_REWARDS, new_digital_rewards)

    for reward in physical_reward_deltas:
        msg = physical_reward.build_tweet(reward)
        twitter.post_tweet(msg)
    nintendoDB.drop_and_insert(config.COLLECTION_PHYSICAL_REWARDS, new_physical_rewards)


if __name__ == "__main__":
    main()
