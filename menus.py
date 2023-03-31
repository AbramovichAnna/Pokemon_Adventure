from utils import slow_print
from colorama import Fore, Style


# ==================== M E N U S ====================


def main_menu():
    slow_print("\nWhat would you like to do?\n")
    print(Fore.GREEN + """
    =========== M A I N   M E N U  ===========
    |                                        |
    |         1) Look for a pokemon          |
    |         2) Check your Pokedex          |
    |         3) Quit                        |
    |                                        |
    ==========================================
    """ + Style.RESET_ALL)


def map_menu():
    slow_print("\nWhere would you like to go?\n")
    print(Fore.GREEN + """
    ============ L O C A T I O N  ============
    |                                        |
    |          1) Cave                       |
    |          2) Forest                     |
    |          3) Lake                       |
    |          4) Mountains                  |
    |          5) Back to main menu          |
    |                                        |
    ==========================================
    """ + Style.RESET_ALL)


def catch_menu():
    slow_print("\nWhat would you like to do?\n")
    print(Fore.GREEN + """
    ========== C A T C H   M E N U ===========
    |                                        |
    |          1) Throw a Pokeball.          |
    |          2) Throw a berry              |
    |          3) Leave                      |
    |                                        |
    ==========================================
    """ + Style.RESET_ALL)


def pokedex_menu():
    slow_print("\nWaht would you like to do?\n")
    print(Fore.GREEN + """
    ============= P O K E D E X  =============
    |                                        |
    |      1) Check Player inventory         |
    |      2) Check your Pokemons Data       |
    |      3) Check all Pokemons in area     |
    |      4) Back to main menu              |
    |                                        |
    ==========================================
    """ + Style.RESET_ALL)


def trhow_pokeball_or_leave():
    slow_print("\nWould you like to throw another Pokeball or leave?\n")
    print(Fore.GREEN + """
    ==========================================
    |          1) Throw a Pokeball.          |
    |          2) Leave                      |
    ==========================================
    """ + Style.RESET_ALL)


def choose_player():
    slow_print("\nWhich player would you like to load?\n")
    print(Fore.GREEN + """
    ==========================================
    |            1) New Player               |
    |            2) Load Player              |
    ==========================================
    """ + Style.RESET_ALL)


def player_options():
    slow_print("\nWhat would you like to do?\n")
    print(Fore.GREEN + """
    ==========================================
    |          1) Overwrite Player           |
    |          2) Load existing Player       |
    |          3) Set new Player             |
    ==========================================
    """ + Style.RESET_ALL)
