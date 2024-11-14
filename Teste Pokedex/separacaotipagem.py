import pypokedex
import time
import random

# Dicionário de imagens dos tipos de Pokémon
type_images = {
    "normal": "https://i.imgur.com/SBXyc7J.png",
    "fire": "https://i.imgur.com/XIfMybU.png",
    "water": "https://i.imgur.com/r0zYJzB.png",
    "grass": "https://i.imgur.com/IlC2EX9.png",
    "flying": "https://i.imgur.com/mLcARq4.png",
    "fighting": "https://i.imgur.com/GWhxJ41.png",
    "poison": "https://i.imgur.com/RDr8eRt.png",
    "electric": "https://i.imgur.com/kW49TD7.png",
    "ground": "https://i.imgur.com/ABV5Dmy.png",
    "rock": "https://i.imgur.com/frGoZNG.png",
    "psychic": "https://i.imgur.com/HzKcFZ8.png",
    "ice": "https://i.imgur.com/SzeQiYY.png",
    "bug": "https://i.imgur.com/To38YCR.png",
    "ghost": "https://i.imgur.com/yJadCBL.png",
    "steel": "https://i.imgur.com/sJGQUg7.png",
    "dragon": "https://i.imgur.com/Igw2QFg.png",
    "dark": "https://i.imgur.com/y64bnBU.png",
    "fairy": "https://i.imgur.com/UGxdMsG.png"
}

# Função para criar a página HTML de um Pokémon
def create_pokemon_html(pokemon):
    dex = pokemon.dex  # Número da Pokédex (ex: 722, 723, etc.)

    # Construir as URLs dos sprites com base no número da Pokédex
    sprite_url = f"https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_{dex:04d}_000_uk_n_00000000_f_n.webp"
    sprite_s_url = f"https://remiscan.fr/shinydex/images/pokemon-sprites/webp/512/poke_capture_{dex:04d}_000_uk_n_00000000_f_r.webp"

    # Abrir o arquivo com o nome do Pokémon
    with open(f"{pokemon.name.capitalize()}.html", "w") as f:
        # Escrever a estrutura do HTML
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

        # Inserir as imagens dos tipos
        for poke_type in pokemon.types:
            if poke_type in type_images:
                f.write(f"<img src='{type_images[poke_type]}' alt='{poke_type} type' class='img-fluid' style='width: 50px; margin: 5px;' />")

        f.write("</p>\n<h3>Base Stats</h3>\n<div class='row'>")

        # Acessar as estatísticas corretamente
        try:
            base_stats = pokemon.base_stats  
            stat_names = ["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"]
            
            for stat_name, stat_value in zip(stat_names, base_stats.__dict__.values()):  # Usando `__dict__` para acessar atributos
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

        except AttributeError:
            # Caso base_stats seja uma lista ou não tenha atributos com esses nomes, usamos um fallback
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

# Função para fazer tentativas de buscar o Pokémon
def fetch_pokemon_with_retries(dex, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            pokemon = pypokedex.get(dex=dex)
            return pokemon
        except Exception as e:
            attempt += 1
            print(f"Tentativa {attempt}/{retries} falhou ao obter o Pokémon de dex {dex}: {e}")
            time.sleep(random.uniform(1, 3))  # Espera aleatória de 1 a 3 segundos entre tentativas
            if attempt == retries:
                print(f"Erro: não foi possível obter o Pokémon de dex {dex} após {retries} tentativas.")
                return None

# Função para filtrar e processar Pokémon por tipo
def process_pokemon_by_type(pokemon_type):
    try:
        # Considerando a Pokédex completa de 1 a 898 (ajuste conforme necessário)
        for dex in range(1, 899):
            pokemon = fetch_pokemon_with_retries(dex)

            if pokemon and pokemon_type in pokemon.types:
                create_pokemon_html(pokemon)
                print(f"Processado Pokémon: {pokemon.name.capitalize()} (Dex {dex})")

            # Adiciona um pequeno atraso entre as requisições para evitar sobrecarga do servidor
            time.sleep(random.uniform(0.5, 1.5))  # Atraso aleatório de 0.5 a 1.5 segundos entre requisições

    except Exception as e:
        print(f"Erro ao processar os Pokémon do tipo {pokemon_type}: {str(e)}")

# Escolha o tipo de Pokémon que deseja filtrar (por exemplo, 'fire')
pokemon_type = 'fire'  # Aqui você pode alterar para qualquer tipo, como 'water', 'grass', 'electric', etc.
process_pokemon_by_type(pokemon_type)
