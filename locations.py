import json
import random
from pokemons import all_pokemon


# ================== L O C A T I O N S ===================

class Cave():
    def __init__(self, location_name, cave_pokemon=[]):
        self.location_name = location_name
        self.cave_pokemon = cave_pokemon

    def set_cave_pokemon(self):
        for pokemon_name, pokemon_data in all_pokemon.items():
            pokemon_type = pokemon_data["type1"]
            if pokemon_type in ["rock", "ground", "dark", "poison", "ghost", "psychic"]:
                self.cave_pokemon.append(pokemon_name)

class Forest():
    def __init__(self, location_name="Forest", forest_pokemon=[]):
        self.location_name = location_name
        self.forest_pokemon = forest_pokemon

    def set_forest_pokemon(self):
        for pokemon_name, pokemon_data in all_pokemon.items():
            pokemon_type = pokemon_data["type1"]
            if pokemon_type in ["grass", "bug", "normal", "electric"]:
                self.forest_pokemon.append(pokemon_name)

class Lake():
    def __init__(self, location_name="Lake", lake_pokemon=[]):
        self.location_name = location_name
        self.lake_pokemon = lake_pokemon

    def set_lake_pokemon(self):
        for pokemon_name, pokemon_data in all_pokemon.items():
            pokemon_type = pokemon_data["type1"]
            if pokemon_type in ["water"]:
                self.lake_pokemon.append(pokemon_name)

class Mountain():
    def __init__(self, location_name="Mountains", mountain_pokemon=[]):
        self.location_name = location_name
        self.mountain_pokemon = mountain_pokemon

    def set_mountain_pokemon(self):
        for pokemon_name, pokemon_data in all_pokemon.items():
            pokemon_type = pokemon_data["type1"]
            if pokemon_type in ["fire", "dragon", "steel"]:
                self.mountain_pokemon.append(pokemon_name)

def export_locations(): # export locations to json file
    cave = Cave("Cave")
    cave.set_cave_pokemon()
    forest = Forest("Forest")
    forest.set_forest_pokemon()
    lake = Lake("Lake")
    lake.set_lake_pokemon()
    mountain = Mountain("Mountains")
    mountain.set_mountain_pokemon()
    locations = {"Locations": {
        "Cave": cave.cave_pokemon,
        "Forest": forest.forest_pokemon,
        "Lake": lake.lake_pokemon,
        "Mountains": mountain.mountain_pokemon
    }
    }

    with open("locations.json", "w") as file:
        json.dump(locations, file)

export_locations()

def random_pokemon_in_location(location): # generate random pokemon in location
    with open("locations.json", "r") as file:
        locations = json.load(file)
    random_pokemon = random.choice(locations["Locations"][location])
    return random_pokemon
