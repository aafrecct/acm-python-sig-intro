the_acm_gang = ['Anto', 'Paula', 'Jorge', 'Neku', 'Diego', 'Carlos', 'Younes',
                'Ferrero', 'Gaspar', 'Roberto', 'Jas', 'Samu', 'Borja']
user_name = input("What's your name? ")

user_in_gang = False
for member in the_acm_gang:
    user_in_gang |= user_name.lower() == member.lower()

print("Have a good day" if user_in_gang else "Join ACM or die.")
