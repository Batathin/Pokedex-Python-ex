import pypokedex


f = open("demofile2.html", "a")
f.read(pokemon = pypokedex.get(dex= 727) print(pokemon.name, pokemon.types, pokemon.base_stats, pokemon.sprites))
f.close()

#open and read the file after the appending:
f = open("demofile2.html", "r")
print(f.read())
