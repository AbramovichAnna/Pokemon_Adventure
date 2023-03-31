from enum import Enum

# ==================== C O M M A N D S ====================


class CHOOSE_PLAYER(Enum):
    NEW_PLAYER = "1"
    LOAD_PLAYER = "2"
    QUIT = "3"


class MAIN_MENU(Enum):
    LOOK_FOR_POKEMON = "1"
    CHECK_POKEDEX = "2"
    QUIT = "3"


class MAP_MENU(Enum):
    CAVE = "1"
    FOREST = "2"
    LAKE = "3"
    MOUNTAINS = "4"
    BACK = "5"


class CATCH_MENU(Enum):
    THROW_POKEBALL = "1"
    THROW_BERRY = "2"
    BACK = "3"


class POKEDEX_MENU(Enum):
    CHECK_PLAYER_INV = "1"
    CHECK_POKEMONS_DATA = "2"
    CHECK_ALL_POKEMONS_IN_AREA = "3"
    BACK = "4"


class PLAYER_OPTIONS_MENU(Enum):
    OVERWRITE = "1"
    LOAD = "2"
    SET_NEW = "3"