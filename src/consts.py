PAGE_DIGITAL_REWARDS = "https://my.nintendo.com/reward_categories/media"
PAGE_PHYSICAL_REWARDS = "https://www.nintendo.com/en-ca/store/exclusives/rewards/"
URI_STORE_PRODUCTS = "https://www.nintendo.com/en-ca/store/products/"

STATUS_NEW = "NEW"
STATUS_RESTOCKED = "RESTOCK"

TWEET_DIGITAL_REWARDS_TEMPLATE = """
[ {status} ] {title}
Available: {start_time} - {end_time}
Category: {category}
Cost: {points_value} {points_type} Points
{url}"""

TWEET_PHYSICAL_REWARDS_TEMPLATE = """
[ {status} ] {name}
Category: My Nintendo Store
Cost: {cost}
{url}"""

TWEET_MAX_LENGTH = 280
