import pypokedex

# Get Pokémon data
pokemon = pypokedex.get(dex=727)

# Open the file in append mode and write Pokémon details to it
with open("demofile1.html", "a") as f:
    f.write(f"Name: {pokemon.name}\n")
    f.write(f"Types: {', '.join(pokemon.types)}\n")
    f.write(f"Base Stats: {pokemon.base_stats}\n")
    f.write(f"Sprites: {pokemon.sprites}\n")
    f.write("\n")
    f.write("<img src= 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/727.png' alt= 'Incineroar sprite' />")  # Add a newline for better readability

# Open the file in read mode and print its content
with open("demofile1.html", "r") as f:
    print(f.read())