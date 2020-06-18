lottozahl = 43 # integer, Ganzzahl
temperature = 36.9 # float, Dezimalzahl (immer nur mit "." statt "," in Python)
ein_wort = "Känguru" # string, Zeichenkette
es_regnet = False # boolean vgl. True (in Python immer mit großen Anfangsbuchstaben)

cities = ["Vienna", "Paris", "Rome", "New York"] # eine variable mit 4 versch. Werten = "list (of strings)" ACHTUNG: man beginnt bei 0 zu zählen
print(cities)
print(cities[3])
cities[2] = "London"
print(cities)

print("Some cities are:")
for city in cities: # für jede Stadt in der Liste "Cities" gib mir:
    print(city)

for x in cities[3]: # eigener Gehversuch
    print(cities[1])

print(len(cities))
for x in range(0,len(cities)):
    print(cities[x])

for x in range(0,len(cities)):
    print(str(x+1) + ": " + cities[x])
    # ==>
    # counter = x + 1
    # counter_string = str(counter)
    # print(counter_string + ": " + cities[x])

person = { "name": "Gerda", "age": 29, "email": 'gerda@smartninja.at'}
print(person["name"]) # 'name' [en. 'key'] ]fungiert hier als Schlüssel für gekoppelten Wert [en. 'value']
