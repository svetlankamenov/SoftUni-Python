from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name:str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon:Pokemon):
        pokemon_name = pokemon.name
        pokemon_health = pokemon.health
        if any(captured_pokemon[0] == pokemon_name for captured_pokemon in self.pokemons):
            return "This pokemon is already caught"
        else:
            self.pokemons.append((pokemon_name, pokemon_health))
            return f"Caught {pokemon_name} with health {pokemon_health}"

    def release_pokemon(self, pokemon_name:str):
        for captured_pokemon in self.pokemons:
            if captured_pokemon[0] == pokemon_name:
                self.pokemons.remove(captured_pokemon)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon_name, pokemon_health in self.pokemons:
            result += f"- {pokemon_name} with health {pokemon_health}\n"

        result = result.rstrip()

        return result