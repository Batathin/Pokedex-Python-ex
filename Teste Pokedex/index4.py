import pypokedex

# Obter os dados do Pokémon Rowlet
pokemon = pypokedex.get(name="Kartana")  # "rowlet" entre aspas

# URL do sprite de Rowlet
sprite_url = "https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_0798_000_uk_n_00000000_f_n.webp"
sprite_s_url = "https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_0798_000_uk_n_00000000_f_r.webp"

# Criar ou abrir o arquivo HTML em modo de escrita
type_images = {
    "normal": "https://i.imgur.com/SBXyc7J.png",
    "fire": "https://i.imgur.com/XIfMybU.png",
    "water": "https://i.imgur.com/r0zYJzB.png",  # URL da imagem de água
    "grass": "https://i.imgur.com/IlC2EX9.png",  # URL da imagem de grama
    "flying": "https://i.imgur.com/mLcARq4.png",  # URL da imagem de voador
    "fighting": "https://i.imgur.com/GWhxJ41.png",  # URL da imagem de lutador
    "poison": "https://i.imgur.com/RDr8eRt.png",  # URL da imagem de veneno
    "electric": "https://i.imgur.com/kW49TD7.png",  # URL da imagem de elétrico
    "ground": "https://i.imgur.com/ABV5Dmy.png",  # URL da imagem de solo
    "rock": "https://i.imgur.com/frGoZNG.png",  # URL da imagem de rocha
    "psychic": "https://i.imgur.com/HzKcFZ8.png",  # URL da imagem de psíquico
    "ice": "https://i.imgur.com/SzeQiYY.png",  # URL da imagem de gelo
    "bug": "https://i.imgur.com/To38YCR.png",  # URL da imagem de inseto
    "ghost": "https://i.imgur.com/yJadCBL.png",  # URL da imagem de fantasma
    "steel": "https://i.imgur.com/sJGQUg7.png",  # URL da imagem de aço
    "dragon": "https://i.imgur.com/Igw2QFg.png",  # URL da imagem de dragão
    "dark": "https://i.imgur.com/y64bnBU.png",  # URL da imagem de obscuro
    "fairy": "https://i.imgur.com/UGxdMsG.png",  # URL da imagem de fada
}

# Criar o arquivo HTML
with open("Kartana.html", "w") as f:
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

    # Escrever os tipos do Pokémon e as imagens correspondentes
    for poke_type in pokemon.types:
        if poke_type in type_images:
            f.write(f"<img src='{type_images[poke_type]}' alt='{poke_type} type' class='img-fluid' style='width: 50px; margin: 5px;' />")

    f.write("</p>\n<h3>Base Stats</h3>\n<div class='row'>")

    # Mostrar as estatísticas base
    base_stats = pokemon.base_stats  # Aqui usamos o atributo corretamente como tupla ou lista
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

    # Mostrar o sprite
    f.write(f"""
            </div>
            <h3 class='mt-4'>Sprite</h3>
            <img src='{sprite_url}' alt='{pokemon.name} sprite' class='img-fluid mb-4' />
            <img src='{sprite_s_url}' alt='{pokemon.name} Shiny sprite' class='img-fluid mb-4' />
        </div>
    </body>
    </html>
    """)

# Exibir o arquivo gerado
with open("Kartana.html", "r") as f:
    print(f.read())