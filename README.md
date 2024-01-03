# Pokemon Adventure

Welcome to Pokemon Adventure, an exciting console game where your mission is simple - capture as many Pokemon as you can! In this game, you play as a trainer who starts with just 5 Poke Balls, but if luck is on your side, you can find more while embarking on your adventure. You have the freedom to choose different search areas like caves, forests, lakes, or mountains, each inhabited by local Pokemon.

But beware, Team Rocket has been spotted in the area! They might try to steal your hard-earned Pokemon.

## Table of Contents

- [Description](#description)
- [Files](#files)
- [Gameplay Actions](#gameplay-actions)

## Description

In Pokemon Adventure, your goal is to capture as many Pokemon as possible and earn 100 XP points for each Pokemon caught. You begin the game with 5 Poke Balls, 5 Forest Berries, and 0 points. At the end of the game, your player data and the list of caught Pokemon are saved in separate JSON files.

## Files

### PLAYER – Class Player

- Defines player attributes, including an empty list of caught Pokemon, 5 Poke Balls, 5 Forest Berries, and 0 points.
- Player data and the list of caught Pokemon are saved in a separate JSON file at the end of the game.

### POKEMONS – Class Pokemon

- Contains attributes of different Pokemon, such as name, Pokedex number, type, weight, and height.
- Pokemon data is retrieved from a JSON file.

### LOCATIONS - Classes Cave, Forest, Lake, Mountain

- Define different search areas where players can find Pokemon.
- Pokemon are randomly distributed within each area based on their type.
- Information about encountered Pokemon in each area is saved in separate JSON files.

### MENUS

- Contains in-game menus and options.

### ACTIONS

- Contains game functions and actions.

### COMMANDS

- Defines game commands.

### DIALOGUE

- Contains introductory dialogues and in-game dialogues.

### ART

- Contains game illustrations.

### UTILS

- Defines text formatting and utility functions.

### MAIN

- Main game file.

## Gameplay Actions

During the game, you can perform various actions:

- Choosing a new player or selecting an existing player from a JSON file.
- Selecting search areas.
- Viewing player data, a list of caught Pokemon, or a list of all Pokemon in the game.
- Adding caught Pokemon to your list and adding items found during the game to your inventory.
- Saving player data, area information, and the list of caught Pokemon to separate JSON files.
- Random appearances of Poke Balls, Forest Berries, wild Pokemon, and Team Rocket encounters.

Enjoy your adventure in the world of Pokemon! Good luck, trainer!
