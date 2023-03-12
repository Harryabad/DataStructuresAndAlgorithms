import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = [
    "Turner Rodriguez",
    "Mekhi Morgan",
    "Maximillian Bowers",
    "Kailee Bauer",
    "Emelia Tran",
    "Paige Hooper",
    "Dalton Powers",
    "Barrett Dunlap",
    "Mara Walls",
    "Kennedi Soto",
    "Jake Ewing",
    "Finn Dawson",
    "Seamus Jenkins",
    "Yesenia Simmons",
    "Ean Browning",
    "Giselle Castro",
    "Konner Thomas",
    "Mattie Mcneil",
    "Cameron Olson",
    "Jerome Travis",
    "Graham Benson",
    "Aryanna Chen",
    "Karsyn Lowe",
    "Cailyn Barber",
    "Johan Hanson",
    "Juliet Joseph",
    "Julio Lee",
    "Maddox Hill",
    "Damaris Mcconnell",
    "Araceli Sutton",
    "Kathleen Hunt",
    "Jessica Parrish",
    "Gaven Stuart",
    "Rosemary Hawkins",
    "Ethan Dunn",
    "Janae George",
    "Sandra Hayden",
    "Eliezer Stokes",
    "Katherine Donovan",
    "Katrina Gallagher",
    "Jasmine Tapia",
    "Ayaan Reese",
    "Grady Townsend",
    "Francis Odonnell",
    "Ashanti Avila",
    "Triston Hurley",
    "Yoselin Baxter",
    "Adrien Chan",
    "Genesis Ayala",
    "Mohamed Vasquez",
    "Gunner Stephens",
    "Kinsley Lowery",
    "Lizeth Duarte",
    "Jaden Maddox",
    "Zaid Goodman",
    "Jaylan Pineda",
    "Aedan Aguirre",
    "Alina Manning",
    "Tess Golden",
    "Reed Stone",
    "Cameron Neal",
    "Anastasia Brandt",
    "Rubi Whitney",
    "Arturo Stafford",
    "Gianna Sheppard",
    "Carlee Mcgee",
    "Quinn Coffey",
    "Kaylin Pace",
    "Lillianna Harding",
    "Rhianna Booth",
    "Brooklyn Leach",
    "Michael Wang",
    "Dominic Bradley",
    "Yareli Contreras",
    "Erick Jimenez",
    "Nathan Stephenson",
    "Ashanti Sandoval",
    "Martin Tran",
    "Jorge Weber",
    "Zayne Friedman",
    "Danny Woods",
    "Sophia Woodard",
    "Cruz Weiss",
    "Nayeli Mcconnell",
    "Kathleen Berry",
    "Kiana Moreno",
    "Carter Sloan",
    "Veronica Frey",
    "Jalen Castro",
    "Nico Cain",
    "Jessie Holt",
    "Trace Graves",
    "Jenna Hurst",
    "Alannah Conner",
    "Jefferson Combs",
    "Rocco Paul",
    "Demetrius Case",
    "Mallory Olsen",
    "Aaden Austin",
    "Zoie Woodward",
]


def binary_search(collection, target):

    first = 0
    last = len(collection) -1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

for n in search_names:
    index = binary_search(names, n)
    print(index)