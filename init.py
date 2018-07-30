class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

user1=User("Young","young@codeit","123456")

print(user1.name)