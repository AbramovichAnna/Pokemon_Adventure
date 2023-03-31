from utils import slow_print
from player import Player
from colorama import Fore, Style


player = Player.get_instance()

# ==================== D I A L O G U E S ====================

def player_load(player_name):
    slow_print(f"""
Welcome back, trainer {player_name}! Are you ready to continue your adventure?
Let's check your pokedex.\n
    """)
 
def intro():
    slow_print("""
Hello there! Welcome to the world of pokemon! My name is OAK, Professor OAK!
This world is inhabited by creatures called pokemon! For some people, pokemon are pets.
Others use them for fights. Myself...I study pokemon as a profession.
First, let me ask you a few questions.
What is your name?""")


def hello(player_name):
    slow_print(f"\nHello {player_name}!")
    slow_print("""
Are you a Pokemon trainer? Because you've caught my attention! Haha!
If serious, i looking for a Pokemon trainer to help me with my research.
Are you interested? y/n""")


def explanation():
    slow_print(f"""
Great!!!
I'll give you {player.pokeballs} pokeballs and {player.berries} berries. Use them to catch pokemon.
Also you can find more items in different locations. Try to find as many as you can.
Each pokemon you catch will give you some XP points. The more pokemon you catch, the more XP you get.
And be warned Team Rocket has been seen in the area! They might steal your pokemon!

Almost forgot, there is your pokedex.
All the pokemon you catch will be added to it, so you can see them later.
It can display your inventory too. Let's check it!\n""")


def cave_intro():
    slow_print("""
You are now in the cave. I hope you are not afraid of the dark!
Let's see what you can find in this cave. Good luck!\n""")


def forest_intro():
    slow_print("""
Look at all the trees! Nice and green! I guess there are many pokemon here.
Let's see what you can find in this forest. Good luck!\n""")


def lake_intro():
    slow_print("""
You approach the lake. What a sunny day! Don't forget your hat!
Let's see what you can find in this lake. Good luck!\n""")


def mountain_intro():
    slow_print("""
You are now in the mountain. Look at the view! It's amazing!
Let's see what you can find in this mountain. Good luck!\n""")


def rocket_stole_pokemon():
    slow_print(Fore.RED + """
TEAM ROCKET
James : Well, well, well, what do we have here? A little trainer wandering around in our territory?
Meowth : Looks like there are some Pokemon to steal. We can take one from them and add it to our collection!
Jessie : That's right! Prepare for trouble, and make it double! 
""" + Style.RESET_ALL)


def rocket_encounter():
    slow_print(Fore.RED + """
TEAM ROCKET
Jessie: Hey, you! Give us your Pokemon!
James: What? No Pokemon? How pathetic!
Meowth: I told you guys, this was a waste of time.
James: Oh..let's go, there's nothing to steal here.
""" + Style.RESET_ALL)


def professor_oak():
    slow_print(f"""
Are you ok, {player.player_name}?
I see you've just had an encounter with that terrible Team Rocket.
Don't worry! If they steal a Pokemon from you, you can still catch it again.
Good luck!\n""")