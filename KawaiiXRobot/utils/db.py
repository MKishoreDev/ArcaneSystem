from pymongo import MongoClient
import os


class DATABASE:

    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.role_db = MongoClient(self.db_url)['Sylviorus']['CUSTOM_ROLES']
        self.proof_db = MongoClient(self.db_url)['data']['proof']

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

    def add_proof(self, user_id, proof):
        if self.proof_db.find_one({"user_id": user_id}):
            self.proof_db.update_one({"user_id": user_id},
                                    {"$set": {
                                        "proof": proof
                                    }})
        else:
            self.proof_db.insert_one({"user_id": user_id, "proof": proof})

    def get_proof(self, user_id):
        if self.proof_db.find_one({"user_id": user_id}):
            role = self.proof_db.find_one({"user_id": user_id})
            return {
                "user_id": proof['user_id'],
                "proof": role['role'],
                "proof": True,
            }
        else:
            return {"proof": False}
