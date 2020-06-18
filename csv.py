"""
CSV:
Name,Alter,Geschlecht
Susanne, 42, w
Kurt, 27, m

Susanne ist 42 Jahre alt und weiblich
Kurt ist 27 Jahre alt und männlich
...

<file>.readlines()
<string>.split()
"""

with open("mitglieder.csv", "r") as member_file:
    members = member_file.readlines()

for x in range(1, len(members)): # anstelle von member in members: (Hier dann erst ab 1. Spalte weil grds Beginn mit 0)
    member = members[x].strip() # entfernt str Zeichen und Leerzeichen (Schönheitskorrektur zB für /n)
    parts = member.split(',') # Angabe an welcher Stelle der Datensatz geteilt werden soll (Zeichenkette --> Liste)
    print("{0} ist {1} Jahre alt und {2}".format(*parts))  # {} --> statt print(parts[0] + ' ist' + parts[1] + ' Jahre alt und' + parts[2])

