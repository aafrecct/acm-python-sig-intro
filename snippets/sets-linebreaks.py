the_acm_gang = {'Anto', 'Paula', 'Jorge', 'Neku', 'Diego',
                'Carlos', 'Younes', 'Ferrero', 'Gaspar',
                'Roberto', 'Jas', 'Samu', 'Borja'}
traitors = set()
afirmative_answers = {'yes', 'y', 'yeah', 'yep', 'si'}

user_name = input("What's your name? ")
user_wants_in = input("Wanna join ACM? ").lower() \
                in afirmative_answers

group_to_add = the_acm_gang if user_wants_in else traitors
group_to_add.add(user_name)

print("ACM:", the_acm_gang, "\nTraitors:", traitors)
