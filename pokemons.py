import json

# ==================== P O K E M O N ====================

class Pokemon():
    def __init__(self, pokemon_name, pokedex_number, weight, height, type1):
        self.pokemon_name = pokemon_name
        self.pokedex_number = pokedex_number
        self.weight = weight
        self.height = height
        self.type1 = type1

    def __str__(self):
        return f"{self.pokemon_name} is a {self.type1} type pokemon. Pokedex number: {self.pokedex_number}. Weight : {self.weight}kg. Hight: {self.height}m."
 
    def load_data(cls):  # load data from json file
        with open("pokedex_data.json") as json_file:
            data = json.load(json_file)
            return data

    def check_all_pokemons(all_pokemon): # display all pokemon in the game
        print()
        print("\nHere is a list of all the Pokemon in the game.\n")
        for pokemon in all_pokemon:
            print(pokemon)


all_pokemon = Pokemon.load_data(Pokemon)