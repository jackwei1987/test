import json

filename = "user3.json"
user_name = input("What's your name?")
user_name = user_name.title()

try:
    with open(filename,'r') as obj1, open(filename,'a') as obj2:
        user_data = json.load(obj1)
        user_data = user_data.title()
        if user_data == user_name:
            print("Welcome back, obj1" + user_name + "!")
        else:
            json.dump(user_name, obj2)
            print("We'll remember you when you come back, obj2" + user_name + "!")

except FileNotFoundError:
    with open(filename, "x") as obj3:
        json.dump(user_name, obj3)
        print("We'll remember you when you come back, obj3" + user_name + "!")