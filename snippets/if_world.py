my_name = "borja"
my_enemys_name = "carlos"
user_name = input("What's your name? ")

if (un := user_name.lower()) == my_name:
    print("Hola {}!".format(user_name))
elif un == my_enemys_name:
    print("Ewww {}!!!".format(user_name))
else:
    print("¿Quien eres?")
