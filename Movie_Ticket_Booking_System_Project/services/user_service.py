class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def register_user(self, username, name, password, email, phone_no):
        return self.user_dao.create_user(username, name, password, email, phone_no)

    def login(self, username, password):
        user = self.user_dao.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def list_users(self):
        return self.user_dao.get_all_users()
