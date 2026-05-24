import uuid


class OfflineAuth:

    @staticmethod
    def login(username: str):
        return {
            "username": username,
            "uuid": str(uuid.uuid4()),
            "token": ""
        }