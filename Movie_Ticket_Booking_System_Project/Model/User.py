class User:
    def __init__(self,user_id,username,name,password,email,phone_no):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.password = password
        self.email = email
        self.phone_no = phone_no
        
    def __repr__(self):
        return (f"User(user_id={self.user_id}, username='{self.username}', "
                f"name='{self.name}', email='{self.email}', phone_no='{self.phone_no}')")