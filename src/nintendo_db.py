from src import config
from src.database import Database


class NintendoDB(Database):
    def get_product_from_id(self, id: str) -> dict:
        return self.db[config.COLLECTION_DIGITAL_REWARDS].find_one({"id": id})

    def get_product_from_sku(self, sku: int) -> dict:
        return self.db[config.COLLECTION_PHYSICAL_REWARDS].find_one({"sku": sku})

    def remove_product_from_sku(self, sku: int) -> dict:
        return self.db[config.COLLECTION_PHYSICAL_REWARDS].remove({"sku": sku})

    def is_product_restock(self, sku: int) -> bool:
        if self.db[config.COLLECTION_PHYSICAL_SKU].find_one({"sku": sku}):
            return True
        return False
