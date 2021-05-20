import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify,render_template


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/Pokemon_Gen1"
engine = create_engine(f'postgresql://{rds_connection_string}')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/types<br/>"
        f"/api/v1.0/dragon<br/>"
        f"/api/v1.0/ghost<br/>"
        f"/api/v1.0/normal<br/>"
        f"/api/v1.0/poison<br/>"
        f"/api/v1.0/grass<br/>"
        f"/api/v1.0/psychic<br/>"
        f"/api/v1.0/fighting<br/>"
        f"/api/v1.0/electric<br/>"
        f"/api/v1.0/ice<br/>"
        f"/api/v1.0/fire<br/>"
        f"/api/v1.0/bug<br/>"
        f"/api/v1.0/ground<br/>"
        f"/api/v1.0/rock<br/>"
        f"/api/v1.0/water<br/>"
        f"/api/v1.0/fairy<br/>"

    )


@app.route("/api/v1.0/types")
def types():
    
    results = engine.execute('SELECT DISTINCT "pokeType" FROM gen1_data')

    all_pokemon = []
    for pokeType in results:
        print(pokeType)
        pokemon_dict = {}
        pokemon_dict["pokeType"] = pokeType[0]
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/dragon")
def dragon():
    
    results = engine.execute('SELECT * FROM gen1_data WHERE "pokeType" = \'dragon\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ghost")
def ghost():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'ghost\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/normal")
def normal():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'normal\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/poison")
def poison():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'poison\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/grass")
def grass():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'grass\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/psychic")
def psychic():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'psychic\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/fighting")
def fighting():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'fighting\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/electric")
def electric():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'electric\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ice")
def ice():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'ice\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/fire")
def fire():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'fire\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/bug")
def bug():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'bug\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/ground")
def ground():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'ground\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/rock")
def rock():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'rock\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/water")
def water():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'water\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)

@app.route("/api/v1.0/fairy")
def fairy():
    
    results = engine.execute('SELECT * from gen1_data WHERE "pokeType" = \'fairy\'')

    all_pokemon = []
    for name, pokeType, hp, attack, defense, specialAttack, specialDefense, speed in results:
        pokemon_dict = {}
        pokemon_dict["name"] = name
        pokemon_dict["pokeType"] = pokeType
        pokemon_dict["hp"] = hp
        pokemon_dict["attack"] = attack
        pokemon_dict["defense"] = defense
        pokemon_dict["specialAttack"] = specialAttack
        pokemon_dict["specialDefense"] = specialDefense
        pokemon_dict["speed"] = speed
        all_pokemon.append(pokemon_dict)

    return jsonify(all_pokemon)


if __name__ == '__main__':
    app.run(debug=True)
