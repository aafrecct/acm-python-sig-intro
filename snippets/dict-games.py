fav_games = {'Anto' : 'Pokemon Red',
            'Gaspar' : 'MegaMan 2',
            'Borja' : 'Minecraft'}

your_game = input("What's your favorite game? ")

if your_game in fav_games.values():
    print("Your favorite game is good.")
else:
    print("Your favorite game is bad.")
