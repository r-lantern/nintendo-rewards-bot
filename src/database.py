from typing import List
import pymongo


class Database:
    def __init__(self, uri: str, db_name: str) -> None:
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    def __exit__(self) -> None:
        self.client.close()

    def drop_and_insert(self, collection: str, entries: List) -> None:
        self.db[collection].drop()
        self.db[collection].insert_many(entries)

    def insert_one(self, collection: str, entry: set) -> None:
        self.db[collection].insert_one(entry)
