import random
from commands import *
import json
from colorama import Fore, Style
from utils import slow_print
from pokemons import all_pokemon


# ==================== P L A Y E R ====================


class Player():
    __instance = None  # class-level variable to store the instance of the class

    def __init__(self, player_name="Ash", player_location="Cave", player_pokemon=[], pokeballs=5, berries=5, xp=0):
        if Player.__instance is not None:  # check if instance already exists
            raise Exception("Singleton classes can only have one instance.")
        else:
            Player.__instance = self  # set instance variable to this instance of the class

        self.player_name = player_name
        self.player_pokemon = player_pokemon
        self.pokeballs = pokeballs
        self.berries = berries
        self.pokemon_item_rocket_chance = random.randint(1, 10)
        self.pokemon_catch_chance = random.randint(1, 10)
        self.pokemon_caught = "n"
        self.stay_here = "y"
        self.counter = 1
        self.try_again = "y"
        self.quit = False
        self.xp = 0
        self.player_location = player_location

    @staticmethod
    def get_instance():
        if Player.__instance is None:  # check if instance already exists
            Player()  # create instance if it does not exist
        return Player.__instance

    def __str__(self):
        return self.player_name

    def player_info(self, player_name): # display player information
        print(Fore.BLUE + f"""
                P O K E D E X
    Player name     : {player_name}
    Player pokemon  : {self.player_pokemon}
    Player items    : {self.pokeballs} Pokeballs 
                      {self.berries} Berries
    Player location : {self.player_location}
    Player XP       : {self.xp}
""" + Style.RESET_ALL)

    def update_name(self, new_name):  # update player name
        self.player_name = new_name

    def update_location(self, chosen_location):  # update player location
        self.player_location = chosen_location

    def check_inventory(self, player_name):  # check player inventory
        print()
        slow_print(f"\nHere is your inventory, {player_name}.\n")
        print()
        print(f"Pokeballs : {self.pokeballs}")
        print(f"Berries   : {self.berries}")

    
    def check_player_pokemon(self): # check if player has caught any pokemon if yes display them
        if self.player_pokemon == []:
            print(
                "\nIt looks like you haven't caught any Pokemon yet! Get out there and catch 'em all!")
        else:
            print("\nThese are the Pokemon you have caught so far :")
            for pokemon_name in self.player_pokemon:
                if pokemon_name in all_pokemon:
                    print(
                        f"\n{pokemon_name} is a {all_pokemon[pokemon_name]['type1']} type Pokemon. Pokedex number: {all_pokemon[pokemon_name]['pokedex_number']}. Weight: {all_pokemon[pokemon_name]['weight']}kg. Hight: {all_pokemon[pokemon_name]['height']}m.")

    def save_player(self):  # save  player information to all players dict json file
        with open("players.json", "r") as file:
            all_players = json.load(file)
        all_players[self.player_name] = {
            "Player pokemon": self.player_pokemon,
            "Pokeballs": self.pokeballs,
            "Berries": self.berries,
            "Last player location": self.player_location,
            "Xp": self.xp
        }
        with open("players.json", "w") as file:
            json.dump(all_players, file, indent=4)

    def display_all_players(all_players): # display all players that have saved their progress
        slow_print(
            "\nHere are all the players that have saved their progress so far : \n")
        print()
        with open("players.json", "r") as file:
            all_players = json.load(file)
        for player in all_players:
            print(player)
        print()

    def load_player(self, load_name): # load player from all_players dict json file
        with open("players.json", "r") as file:
            all_players = json.load(file)
        if load_name in all_players:
            player = Player.get_instance()
            player.player_name = load_name
            player.player_pokemon = all_players[load_name]["Player pokemon"]
            player.pokeballs = all_players[load_name]["Pokeballs"]
            player.berries = all_players[load_name]["Berries"]
            player.player_location = all_players[load_name]["Last player location"]
            player.xp = all_players[load_name]["Xp"]
            slow_print("\nPlayer loaded successfully!\n")

    def check_existing_player(self, new_name): # check if player already exists
        with open("players.json", "r") as file:
            all_players = json.load(file)
        if new_name not in all_players:  
            return True # player does not exist
        else:  
            print("\nThis player already exists!\n")
            return False # player  exist


    def if_continue(self):
        while True:
            choice = input(Fore.GREEN+Style.BRIGHT +"\n>>>: " + Style.RESET_ALL).lower()
            if choice == "n": # if player does not want to continue
                slow_print("\nOk! Maybe next time then.")
                exit()
            if choice == "y": # if player wants to continue
                break
            else:
                print("Invalid input! Please enter y or n.")
                continue