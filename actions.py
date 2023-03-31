import random
import dialogue
from player import Player
from utils import slow_print
import menus
from commands import *
from locations import random_pokemon_in_location
import time
from colorama import Fore, Style


player = Player.get_instance()

# ==================== A C T I O N S ====================


def at_location(player_location): # actions at location
    while player.stay_here == "y":
        random_pokemon = random_pokemon_in_location(player_location)
        if player.pokemon_item_rocket_chance == 1:
            rocket_encounter()
        elif player.pokemon_item_rocket_chance <= 3:
            item_encounter()
        else:
            player.pokemon_caught = "n"
            pokemon_encounter(player_location, random_pokemon)
            throw_pokeball_or_berry(random_pokemon)
        if player.pokeballs == 0 or player.quit == True:
            quit_game()
        search = input(
            f"\nDo you steel want to search for a Pokemon in the {player_location}? y/n" +  
            Fore.GREEN+Style.BRIGHT +"\n>>>: " + Style.RESET_ALL)
        if search == "y":
            player.pokemon_item_rocket_chance = random.randint(1, 10)
            player.stay_here == "y"
            print()
        else:
            slow_print(f"\nYou decide to leave the {player_location}.\n")
            break



def pokemon_encounter(player_location, random_pokemon): # pokemon apearing (random by players location)
    print(Fore.YELLOW + f"""
    ==========================================
      A wild {random_pokemon} appeared in {player_location}!
    ==========================================
    """ + Style.RESET_ALL)


def throw_pokeball_or_berry(random_pokemon):
    while player.pokemon_caught == "n":
        menus.catch_menu()
        choice = input(Fore.GREEN+Style.BRIGHT+"\n>>>: " + Style.RESET_ALL)
        if choice in [command.value for command in CATCH_MENU]:
            if choice == CATCH_MENU.THROW_POKEBALL.value:
                throw_pokeball(random_pokemon)
            elif choice == CATCH_MENU.THROW_BERRY.value:
                throw_berry(random_pokemon)
                choice = input(Fore.GREEN+Style.BRIGHT+"\n>>>: " + Style.RESET_ALL)
                if choice == CATCH_MENU.THROW_POKEBALL.value:
                    throw_pokeball(random_pokemon)
            else:
                leave(random_pokemon)
                player.pokemon_caught = "y"
        else:
            print("Invalid input! Please enter a valid command.")
            continue
        

def throw_pokeball(random_pokemon):
    if player.pokeballs > 0:
        slow_print(
            f"\nYou deside to throw a Pokeball at the wild {random_pokemon}.")
        player.pokeballs -= 1
        slow_print("\nThe ball shakes once...")
        time.sleep(1)
        if player.pokemon_catch_chance == 1:
            pokemon_breaks_out(random_pokemon)
        else:
            slow_print("\nTwice...")
            time.sleep(1)
            if player.pokemon_catch_chance <= 3:
                pokemon_breaks_out(random_pokemon)
            else:
                slow_print("\nThree times...\n")
                time.sleep(1)
                if player.pokemon_catch_chance == 4:
                    pokemon_breaks_out(random_pokemon)
                else:
                    slow_print(
                        f"\nGood job! You do it! {random_pokemon} was added to your Pokedex!\n")
                    player.player_pokemon.append(random_pokemon)
                    player.xp += 100
                    player.player_info(player.player_name)
                    player.pokemon_item_rocket_chance = random.randint(1, 10)
                    player.pokemon_catch_chance = random.randint(1, 10)

                    if player.pokeballs == 0:
                        slow_print(
                            "\nOops..It looks like you're out of Pokeballs!")
                        player.pokemon_caught = "y"
                        player.quit = True
                    else:
                        player.pokemon_caught = "y"
    else:
        slow_print("\nOops..It looks like you're out of Pokeballs!")
        player.pokemon_caught = "y"
        player.quit = True


def throw_berry(random_pokemon):
    print()
    if player.berries > 0:
        player.berries -= 1
        slow_print(
            f"\nYou deside to throw a berry at the wild {random_pokemon}.")
        slow_print(
            f"\nYou have {player.berries} berries left.\n")
        player.pokemon_catch_chance += 2
        slow_print(
            f"\nThe wild {random_pokemon} looks a little happier, maybe it will be easier to catch!")
        menus.trhow_pokeball_or_leave()
    else:
        slow_print("\nIt looks like you don't have any berries to throw.")
        menus.trhow_pokeball_or_leave()


def pokemon_breaks_out(random_pokemon):
    slow_print(
        f"\nOh no! The wild {random_pokemon} broke out of the Pokeball!\n")
    if player.pokeballs == 0:
        slow_print("\nIt looks like you're out of Pokeballs!\n")
        player.pokemon_caught = "y"
        player.quit = True
    else:
        slow_print(f"\nYou have {player.pokeballs} Pokeballs left.\n")
        player.pokemon_catch_chance = random.randint(1, 10)


def rocket_encounter(): # Team Rocket apearing(randomly)
    slow_print("""
Wait...did you hear that?")
It's Team Rocket!
""")
    if player.player_pokemon != []:
        dialogue.rocket_stole_pokemon()
        slow_print(f"\nOh no...They've stolen {player.player_pokemon[0]}!\n")
        player.player_pokemon.pop(0)
        player.pokemon_item_rocket_chance = random.randint(1, 10)
        if player.counter == 1:
            dialogue.professor_oak()
        player.counter = 2

    else:
        dialogue.rocket_encounter()
        player.pokemon_item_rocket_chance = random.randint(1, 10)


def item_encounter(): # random item apearing (pokeball or berry)
    item_found = random.randint(1, 2)
    num_items = random.randint(2, 3)
    if item_found == 1:
        slow_print(
            "\nLook there, near the stone! It's something round and red..\nThat must be a Pokeball! Let's collect some!\n")
        slow_print(f"\n{num_items} Pokeballs added to your inventory!")
        player.pokeballs += num_items
        slow_print(f"\nNow you have {player.pokeballs} Pokeballs.\n")
        player.pokemon_item_rocket_chance = random.randint(1, 10)
    else:
        slow_print("\nLook, it's nice berry bush. Let's collect some berries!\n")
        slow_print(f"\n{num_items} berries added to your inventory!")
        player.berries += num_items
        slow_print(f"\nNow you have {player.berries} berries.\n")
        player.pokemon_item_rocket_chance = random.randint(1, 10)


def leave(random_pokemon):
    slow_print(f"You decide not to catch the wild {random_pokemon}. \n")


def quit_game():
    player.quit = True
    player.save_player()
    if player.player_pokemon == []:
        slow_print(
            f"Thank you {player.player_name}, next time you'll catch them all! You have {player.pokeballs} Pokeballs left.\n")
    if player.pokeballs == 0 and player.player_pokemon != []:
        slow_print(
            "It's time to head back to the lab.\n")
        slow_print(
            f"Great job, Trainer {player.player_name}! You have caught {len(player.player_pokemon)} Pokemon!\n")
        slow_print(f"I hope you enjoyed your adventure! You earned {player.xp} XP points!\n")
        slow_print(
            "Thank you for helping me with my research, and I hope to see you again soon!\n\n")
    if player.player_pokemon != [] and player.pokeballs != 0:
        slow_print(
            f"Great job, Trainer {player.player_name}! You have caught {len(player.player_pokemon)} Pokemon!\n")
        slow_print(f"I hope you enjoyed your adventure! You earned {player.xp} XP points!\n")
        slow_print(
            "Thank you for helping me with my research, and I hope to see you again soon!\n\n")

    exit()
