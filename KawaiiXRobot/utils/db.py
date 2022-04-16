from pymongo import MongoClient
import os


class DATABASE:

    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.role_db = MongoClient(self.db_url)['Sylviorus']['CUSTOM_ROLES']

    def already_exists(self, user_id):
        return bool(x := self.db.find_one({"user_id": user_id}))

    def add_role(self, user_id, role):
        if self.role_db.find_one({"user_id": user_id}):
            self.role_db.update_one({"user_id": user_id},
                                    {"$set": {
                                        "role": role
                                    }})
        else:
            self.role_db.insert_one({"user_id": user_id, "role": role})

    def get_role(self, user_id):
        if self.role_db.find_one({"user_id": user_id}):
            role = self.role_db.find_one({"user_id": user_id})
            return {
                "user_id": role['user_id'],
                "role": role['role'],
                "status": True,
            }
        else:
            return {"status": False}
