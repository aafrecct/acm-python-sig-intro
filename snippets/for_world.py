the_acm_gang = ["Ferrero", "Carlos", "Jennifer", "Henny",
                "Kalili", "Anche", "Nerea"]
user_name = input("¿Cómo te llamas? ")

user_in_gang = False
for member in the_acm_gang:
    user_in_gang |= user_name.lower() == member.lower()

print("Uno de los nuestros" if user_in_gang else "Unete a ACM")
