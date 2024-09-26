import pypokedex

# Obter os dados do Pokémon
pokemon = pypokedex.get(dex=722)

# URL do sprite de Rowlet
sprite_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/722.png"

# Criar ou abrir o arquivo HTML em modo de escrita
with open("pokemon_rowlet.html", "w") as f:
    f.write("""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Pokémon - Rowlet</title>
        <link href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' rel='stylesheet'>
    </head>
    <body class='bg-light'>
        <div class='container text-center'>
            <h1 class='mt-5'>{name}</h1>
            <p><strong>Types:</strong> {types}</p>
            <h3>Base Stats</h3>
            <div class='row'>
    """.format(name=pokemon.name.capitalize(), types=', '.join(pokemon.types).capitalize()))

    # Mostrar as estatísticas base
    base_stats = pokemon.base_stats  # Aqui usamos o atributo corretamente como tupla ou lista
    stat_names = ["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]

    for stat_name, stat_value in zip(stat_names, base_stats):
        f.write("""
                <div class='col-md-4'>
                    <h5>{stat_name}</h5>
                    <div class='progress' style='height: 30px;'>
                        <div class='progress-bar bg-info' style='width: {stat_value}%' aria-valuenow='{stat_value}' aria-valuemin='0' aria-valuemax='100'>
                            {stat_value}
                        </div>
                    </div>
                </div>
        """.format(stat_name=stat_name, stat_value=stat_value))

    # Mostrar o sprite
    f.write("""
            </div>
            <h3 class='mt-4'>Sprite</h3>
            <img src='{sprite_url}' alt='Rowlet sprite' class='img-fluid mb-4' />
        </div>
    </body>
    </html>
    """.format(sprite_url=sprite_url))

# Exibir o arquivo gerado
with open("pokemon_rowlet.html", "r") as f:
    print(f.read())
