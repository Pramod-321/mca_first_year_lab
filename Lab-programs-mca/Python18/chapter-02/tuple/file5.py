cities = ("Delhi", "Mumbai", "Chennai", "Kolkata")
city = input("Enter a city name: ")

if city in cities:
    print(city, "is in the tuple")
else:
    print(city, "is not in the tuple")
