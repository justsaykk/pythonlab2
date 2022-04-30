# In python, a Javascript "object" is called a "dictionary"
car: dict[str, str | int] = {"type": "Fiat", "model": 500, "color": "white"}
print(car)
print("=" * 10)

# To read the value from a specific key
print(car["model"])
print("=" * 10)

# Getting the length of the dictionary
print(len(car))
print("=" * 10)

# Reading different things from the dictionary
print(car.keys())  # accessing keys
print(car.values())  # accessing values
print(car.items())  # accessing both
print("=" * 10)

# Looping through the dictionary
for element in car:  # get the keys
    print(element)

print("=" * 10)

for key, value in car.items():  # get both key and values
    print(key, value)
