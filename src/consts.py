PAGE_REWARDS_STORE = "https://my.nintendo.com/reward_categories/nintendo_store"

STATUS_NEW = "new"
STATUS_STOCK_IN = "stock_in"
STATUS_STOCK_OUT = "stock_out"

TAGS = {
    STATUS_NEW: "NEW",
    STATUS_STOCK_IN: "BACK IN STOCK",
    STATUS_STOCK_OUT: "OUT OF STOCK",
}

TWEET_TEMPLATE = """
[ {tag} ] {title}
Available: {start_time} - {end_time}
Category: {category}
Cost: {points_value} {points_type} Coins
{url}
"""
