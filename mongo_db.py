from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.sms_spammer
sms_spammer_db = db.users


class DataBaseManagerUser:

    @classmethod
    def insert_user_data(cls, user_id: str, phone: str, status=True, vip=False):
        if DataBaseManagerUser.check_exists(user_id):
            data = {"phone": phone, "user_id": user_id, "status": status, "vip": vip, "spam_count": 0}
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
        try:
            sms_spammer_db.update_one({"user_id": user_id}, {"$set": {"status": True}})
            return True
        except:
            return False

    @classmethod
    def deactivator(cls, user_id):
        try:
            sms_spammer_db.update_one({"user_id": user_id}, {"$set": {"status": False}})
            return True
        except:
            return False

    @classmethod
    def check_vip(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        if data is not None:
            if data["vip"] is True:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def set_vip(cls, user_id):
        try:
            sms_spammer_db.update_one({"user_id": user_id}, {"$set": {"vip": True}})
            return True
        except:
            return False

    @classmethod
    def unset_vip(cls, user_id):
        try:
            sms_spammer_db.update_one({"user_id": user_id}, {"$set": {"vip": False}})
            return True
        except:
            return False

    @classmethod
    def users_list(cls):
        users_list = []
        users = sms_spammer_db.find({})
        for user in users:
            users_list.append(user)
        return users_list

    @classmethod
    def spam_count(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        if data is not None:
            return data["spam_count"]
        else:
            return False

    @classmethod
    def spam_count_up(cls, user_id):
        data = sms_spammer_db.find_one({"user_id": user_id})
        if data is not None:
            sms_spammer_db.update_one({"user_id": user_id}, {"$set": {"spam_count": data["spam_count"] + 1}})
            return True
        else:
            return False
