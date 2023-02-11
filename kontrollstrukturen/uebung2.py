personen = 5
putzliste = []

for x in range(personen):
  putzliste.append([])

for x in range(1, 366):
  if x%5 == 1:
    putzliste[0].append(x)
  elif x%5 == 2:
    putzliste[1].append(x)
  elif x%5 == 3:
    putzliste[2].append(x)
  elif x%5 == 4:
    putzliste[3].append(x)
  elif x%5 == 0:
    putzliste[4].append(x)

for x in range(personen):
  print(putzliste[x])
