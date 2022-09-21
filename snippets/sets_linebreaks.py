the_acm_gang = set()
traitors = set()
afirmative_answers = {'yes', 'y', 'yeah', 'yep', 'si', 's'}

while True:
    user_name = input("¿Como te llamas? ")
    user_wants_in = input("¿Quieres unirte a ACM? ").lower() \
                    in afirmative_answers

    group_to_add = the_acm_gang if user_wants_in else traitors
    group_to_add.add(user_name)

    print("ACM:", the_acm_gang, "\nTraitors:", traitors)
