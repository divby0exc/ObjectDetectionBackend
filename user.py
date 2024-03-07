
class User():
    def __init__(self,t_user, t_pwd, t_created_at=None, t_updated_at=None) -> None:
        self.username=t_user
        self.password=t_pwd
        self.created_at=t_created_at
        self.updated_at=t_updated_at

    def get_username(self):
        return self.username
    
    def get_pwd(self):
        return self.password
    
    def get_created(self):
        return self.created_at
    
    def get_updated(self):
        return self.updated_at
    