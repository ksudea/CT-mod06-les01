import requests
import sys
# Task 2
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

#Task 3 
def fetch_planet_data_enhanced():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planets_formatted_list = []
    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass_value = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass_value:.2f} * 10^{mass_exponent} kg, Orbit Period: {orbit_period} days")
            planets_formatted_list.append({"name": name, "mass_value": mass_value, "mass_exponent": mass_exponent, "orbit_period": orbit_period})
    return planets_formatted_list

def find_heaviest_planet(planets):
    heaviest_exponent = 0
    heaviest_mass = 0
    heaviest_name = ""
    for planet in planets:
        planet_exponent = planet['mass_exponent']
        planet_mass = planet['mass_value']
        if planet_exponent > heaviest_exponent:
            heaviest_exponent = planet_exponent
            heaviest_mass = planet_mass
            heaviest_name = planet['name']
        elif planet_exponent == heaviest_exponent:
            if planet_mass > heaviest_mass:
                heaviest_mass = planet_mass
                heaviest_name = planet['name']
    return heaviest_name, heaviest_mass, heaviest_exponent

planets = fetch_planet_data_enhanced()
name, heaviest_mass, heaviest_exponent = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {heaviest_mass} * 10^{heaviest_exponent} kg.")
