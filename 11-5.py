class User:
    def say_my_name(some_user):
        print("My name is "+ some_user.name)

user1=User()
user2=User()

user1.name="Young"
user1.email="young@codeit.kr"
user1.password="123456"

print(user1.name,user1.email,user1.password)

User.say_my_name(user1)

user1.say_my_name()