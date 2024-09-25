import json
from resources.stat_tools import rand_uncertainty, average

def load_json_data(filename: str = "data.json"):
    with open("./" + filename) as file:
        return json.load(file)


if __name__ == "__main__":
    data = load_json_data()

    distances = data["ruler-distances"]
    masses = data["scale-masses"]
    diameters = data["caliper-diameters"]

    ruler_ru = round(rand_uncertainty(distances), 3)
    masses_ru = round(rand_uncertainty(masses, 3))
    diameters_ru = round(rand_uncertainty(diameters), 3)
