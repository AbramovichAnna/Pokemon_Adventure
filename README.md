# Pokémon Adventure Console Game
```
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
```

## Introduction

Welcome to the Pokemon Adventure Game! This console-based game is designed for practicing Object-Oriented Programming (OOP) skills. The goal of the game is simple: catch as many Pokemon as you can and earn XP points for each captured Pokemon. You'll start the game with 5 Poke Balls, but if luck is on your side, you might find more during your adventure. Be cautious, though, as Team Rocket may appear and attempt to steal your hard-earned Pokemon.

## Files Description

- **PLAYER – Class Player:** Defines the player's attributes. The player starts with an empty Pokémon list, 5 Poké Balls, 5 Forest Berries, and 0 points. The player's data and the list of captured Pokémon are saved in separate JSON files at the end of the game.

- **POKEMONS – Class Pokemon:** Contains attributes of different Pokémon, such as their name, Pokédex number, type, weight, and height. This data is loaded from a JSON file.

- **LOCATIONS - Class Cave, Class Forest, Class Lake, Class Mountain:** Represents different areas where Pokémon can be found. Each class contains the Pokémon native to that area. The data is stored in separate JSON files, and Pokémon are randomly distributed within each area.

- **MENUS:** Contains game menus and user prompts.

- **ACTIONS:** Contains various game functions.

- **COMMANDS:** Defines commands and their functionality.

- **DIALOGUE:** Contains introductory and in-game dialogues.

- **ART:** Stores game illustrations.

- **UTILS:** Contains text formatting settings.

- **MAIN:** The main game file.

## Gameplay

1. Start a new game, create new player or load an existing player from a JSON file, or overwrite an existing player's data.
2. Choose an area to search for Pokémon (Cave, Forest, Lake, or Mountain).
3. View player information, a list of captured Pokémon, or a list of all Pokémon in the game.
4. Capture a Pokémon or pick up items (Poké Balls, Forest Berries) during your adventure.
5. Save player data, area information, and the list of captured Pokémon to separate JSON files.
6. Encounter random events, such as finding items or facing Team Rocket.

Have fun capturing Pokémon with the Pokémon Adventure Console Game!
