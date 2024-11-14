import pypokedex


pokemon = pypokedex.get(dex="722")  

sprite_url = "https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_0722_000_mf_n_00000000_f_n.webp"
sprite_s_url = "https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_0722_000_mf_n_00000000_f_r.webp"


type_images = {
    "normal": "https://i.imgur.com/SBXyc7J.png"
    "fire": "https://i.imgur.com/XIfMybU.png"
    "water": "https://i.imgur.com/r0zYJzB.png"
    "grass": "https://i.imgur.com/IlC2EX9.png"
    "flying": "https://i.imgur.com/mLcARq4.png"
    "fighting": "https://i.imgur.com/GWhxJ41.png"
    "poison": "https://i.imgur.com/RDr8eRt.png"
    "electric": "https://i.imgur.com/kW49TD7.png"
    "ground": "https://i.imgur.com/ABV5Dmy.png"
    "rock": "https://i.imgur.com/frGoZNG.png"
    "psychic": "https://i.imgur.com/HzKcFZ8.png"
    "ice": "https://i.imgur.com/SzeQiYY.png"
    "bug": "https://i.imgur.com/To38YCR.png"
    "ghost": "https://i.imgur.com/yJadCBL.png"
    "steel": "https://i.imgur.com/sJGQUg7.png"
    "dragon": "https://i.imgur.com/Igw2QFg.png"
    "dark": "https://i.imgur.com/y64bnBU.png"
    "fairy": "https://i.imgur.com/UGxdMsG.png"
}

with open({pokemon.name.capitalize()}, "w") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Pokémon - {pokemon.name.capitalize()}</title>
        <link href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' rel='stylesheet'>
    </head>
    <body class='bg-light'>
        <div class='container text-center'>
            <h1 class='mt-5'>{pokemon.name.capitalize()}</h1>
            <p><strong>Types:</strong>
    """)

    for poke_type in pokemon.types:
        if poke_type in type_images:
            f.write(f"<img src='{type_images[poke_type]}' alt='{poke_type} type' class='img-fluid' style='width: 50px; margin: 5px;' />")

    f.write("</p>\n<h3>Base Stats</h3>\n<div class='row'>")

  
    base_stats = pokemon.base_stats  
    stat_names = ["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]

    for stat_name, stat_value in zip(stat_names, base_stats):
        f.write(f"""
                <div class='col-md-4'>
                    <h5>{stat_name}</h5>
                    <div class='progress' style='height: 30px;'>
                        <div class='progress-bar bg-info' style='width: {stat_value}%' aria-valuenow='{stat_value}' aria-valuemin='0' aria-valuemax='100'>
                            {stat_value}
                        </div>
                    </div>
                </div>
        """)

    f.write(f"""
            </div>
            <h3 class='mt-4'>Sprite</h3>
            <img src='{sprite_url}' alt='{pokemon.name} sprite' class='img-fluid mb-4' />
            <img src='{sprite_s_url}' alt='{pokemon.name} Shiny sprite' class='img-fluid mb-4' />
        </div>
    </body>
    </html>
    """)

    for dex in range(722, 809):
            try:
                pokemon = pypokedex.get(dex=dex)
                
                alola_pokemon_list.append(pokemon)
                

                create_pokemon_php(pokemon)
                
    
                update_type_catalog(pokemon)
            
            except Exception as e:
                print(f"Erro ao processar o Pokémon de dex {dex}: {str(e)}")
                continue

            process_alola_pokemons()