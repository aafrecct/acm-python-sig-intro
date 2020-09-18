my_name = "borja"
my_enemys_name = "anto"
user_name = input("What's your name? ")

if (un := user_name.lower()) == my_name:
    print("Hello {}!".format(user_name))
elif un == my_enemys_name:
    print("Get the fuck out of here {}!!!".format(user_name))
else:
    print("I don't really know who you are...")
