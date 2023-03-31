import art
import dialogue
import menus
import commands
from player import Player
from pokemons import Pokemon, all_pokemon
import actions
from utils import slow_print
from colorama import Fore, Style

player = Player.get_instance()

# ==================== G A M E ====================

def game_loop():
    menus.choose_player()
    while True:
        choose_player = input(Fore.GREEN+Style.BRIGHT +"\n>>>: " + Style.RESET_ALL) # New player or load player
        if choose_player in [command.value for command in commands.CHOOSE_PLAYER]:
            if choose_player == commands.CHOOSE_PLAYER.NEW_PLAYER.value:  # New player
                print(art.logo)
                dialogue.intro()
                while True:
                    new_name = input(Fore.GREEN+Style.BRIGHT +"\n>>>: " + Style.RESET_ALL) # New player name
                    if new_name == "":
                        print("Invalid input! Please enter a valid name.")
                        continue
                    elif player.check_existing_player(new_name) == True: # If player name doesn't exist
                        player.update_name(new_name)
                        dialogue.hello(player.player_name)
                        player.if_continue()
                        dialogue.explanation()
                        break
                    else:                                       # If player name exists
                        menus.player_options()
                        player_option = input(Fore.GREEN+Style.BRIGHT + "\n>>>: " + Style.RESET_ALL)
                        if player_option in [command.value for command in commands.PLAYER_OPTIONS_MENU]: 
                            if player_option == commands.PLAYER_OPTIONS_MENU.OVERWRITE.value:  # Overwrite player
                                player.update_name(new_name)
                                dialogue.hello(player.player_name)
                                player.if_continue()
                                dialogue.explanation()
                                break
                            elif player_option == commands.PLAYER_OPTIONS_MENU.LOAD.value:  # Load player from existing name
                                load_name = new_name
                                player.load_player(load_name)
                                dialogue.player_load(player.player_name)
                                break
                            else:                                                     # Set new player name
                                slow_print("\nOk! Let's try again then.\n")
                                slow_print("What is your name?")
                                continue
                        else:
                            print("Invalid input! Please enter a valid command.")
                            continue

            elif choose_player == commands.CHOOSE_PLAYER.LOAD_PLAYER.value:  # Load player
                player.display_all_players()
                load_name = input(
                    "\nWhat is the name of the player you want to load?" + Fore.GREEN+Style.BRIGHT + "\n>>>: " + Style.RESET_ALL)
                if load_name == "":
                    print("Invalid input! Please enter a valid name.")
                player.load_player(load_name)
                dialogue.player_load(player.player_name)

            player.player_info(player.player_name)
            slow_print("\nLooks good! Now, let's start our adventure!\n")
            main_menu()

        else:
            print("Invalid input! Please enter a valid command.")
            continue

def main_menu():
    while True:
        menus.main_menu()
        player_choice = input(Fore.GREEN+Style.BRIGHT +"\n>>>: " + Style.RESET_ALL)
        if player_choice in [command.value for command in commands.MAIN_MENU]:
            if player_choice == commands.MAIN_MENU.LOOK_FOR_POKEMON.value:  # Look for pokemon
                location_menu(player)
            if player_choice == commands.MAIN_MENU.CHECK_POKEDEX.value:  # Check pokedex
                pokedex_check()
            if player_choice == commands.MAIN_MENU.QUIT.value:  # Quit game
                player.save_player()
                actions.quit_game()
        else:
            print("Invalid input! Please enter a valid command.")
            continue


def pokedex_check():
    while True:
        menus.pokedex_menu()
        player_choice = input(Fore.GREEN+Style.BRIGHT +
                              "\n>>>: " + Style.RESET_ALL)
        if player_choice in [command.value for command in commands.POKEDEX_MENU]:
            if player_choice == commands.POKEDEX_MENU.CHECK_PLAYER_INV.value: # Check player inventory
                player.check_inventory(player.player_name)
            if player_choice == commands.POKEDEX_MENU.CHECK_POKEMONS_DATA.value: # Check player pokemon data
                Player.check_player_pokemon(player)
            if player_choice == commands.POKEDEX_MENU.CHECK_ALL_POKEMONS_IN_AREA.value: # Check all pokemon in area
                Pokemon.check_all_pokemons(all_pokemon)
            if player_choice == commands.POKEDEX_MENU.BACK.value:   # Back to main menu
                break
        else:
            print("Invalid input! Please enter a valid command.")
            continue


def location_menu(player):
    while True:
        menus.map_menu()
        chosen_location = input(
            Fore.GREEN+Style.BRIGHT+"\n>>>: " + Style.RESET_ALL)
        if chosen_location in [command.value for command in commands.MAP_MENU]:
            if chosen_location == commands.MAP_MENU.CAVE.value:  # Cave
                player.update_location("Cave")
                print(art.cave)
                dialogue.cave_intro()
            if chosen_location == commands.MAP_MENU.FOREST.value:  # Forest
                player.update_location("Forest")
                print(art.forest)
                dialogue.forest_intro()
            if chosen_location == commands.MAP_MENU.LAKE.value:  # Lake
                player.update_location("Lake")
                print(art.lake)
                dialogue.lake_intro()
            if chosen_location == commands.MAP_MENU.MOUNTAINS.value:  # Mountains
                player.update_location("Mountains")
                print(art.mountains)
                dialogue.mountain_intro()
            elif chosen_location == commands.MAP_MENU.BACK.value:  # Back to main menu
                print("Let's go back to the main menu.")
                break
            actions.at_location(player.player_location)
        else:
            print("Invalid input! Please enter a valid command.")
            continue


if __name__ == "__main__":
    game_loop()
