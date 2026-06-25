people={
    "Jeff":"Is afraid of Dogs.",
    "David":"Plays the piano.",
    "Jason":"Can fly an airplane."
}

for name,fact in people.items():
    print(name+":",fact)

people["Jeff"]="Is afraid of heights."
people["Jill"]="Can hula dance."

for name,fact in people.items():
    print(name+":",fact)