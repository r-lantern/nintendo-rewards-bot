from src import config
from src.database import Database


class NintendoDB(Database):
    def get_product_from_id(self, id: str) -> dict:
        return self.db[config.COLLECTION_REWARDS].find_one({"id": id})
