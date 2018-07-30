class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def introduce(self):
        print("My name is %s"%self.name)
        print("My email address is %s"%self.email)

    def introduce_twice(self):

        for i in range(2):
            self.introduce()

user1=User("Young","young@codeit.kr","123456")
user1.introduce()
user1.introduce_twice()