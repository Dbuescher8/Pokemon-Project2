import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/Pokemon_Gen1"
engine = create_engine(f'postgresql://{rds_connection_string}')

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# print(Base.classes.keys())

# # Save reference to the table
# Pokemon = Base.classes.gen1_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/pokemon"
    )


@app.route("/api/v1.0/pokemon")
def pokemon():
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    # Query all pokemon
    # results = session.query(Pokemon.name, Pokemon.pokeType, Pokemon.hp, Pokemon.attack, Pokemon.defense, Pokemon.specialAttack, Pokemon.specialDefense, Pokemon.speed).all()

    # session.close()
    results = engine.execute("SELECT * FROM gen1_data")

    # Create a dictionary from the row data and append to a list of all_pokemon
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
