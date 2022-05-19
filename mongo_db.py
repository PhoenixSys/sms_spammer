from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.sms_spammer
sms_spammer_db = db.users


class DataBaseManagerUser:

    @classmethod
    def insert_user_data(cls, user_id: str, phone: str, status=False):
        if DataBaseManagerUser.check_exists(user_id):
            data = {"phone": phone, "user_id": user_id, "status": status}
            sms_spammer_db.insert_one(data)
            return True
        else:
            return False

    @classmethod
    def check_exists(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        if data is None:
            return True
        else:
            return False

    @classmethod
    def check_login(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        if data is not None:
            if data["status"] is True:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def activator(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        sms_spammer_db.update_one({"_id": data["_id"]}, {"$set": {"status": True}})
        return True

    @classmethod
    def deactivator(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        sms_spammer_db.update_one({"_id": data["_id"]}, {"$set": {"status": False}})
        return True



    @classmethod
    def users_list(cls):
        users_list = []
        users = sms_spammer_db.find({})
        for user in users:
            users_list.append(user)
        return users_list
