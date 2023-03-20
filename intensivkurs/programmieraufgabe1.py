# Eingabe des Strings
s = "Python ist sooo eine tolle Programmiersprache!"

# Declaration des verwendeten Dictionarys
myDict = {}

# Declaration des verwendeten Liste
myList = []

# Declaration 
sortedList = []

# For loop zum Erstellen des Dictionarys
for char in s:
  # If-Schleife kontrolliert, ob Zeichen bereits in Dictionary ist
  # Wenn nein wird es also Key mit dem Value 1 gespeichert
  if char not in myDict:
    myDict[char] = 1
  # Wenn ja wird das Value des Zeichens um eins erhöht
  else:
    myDict[char] = myDict[char] + 1
# Whitespaces sollen nicht beachtet werden, also entfernen wir Sie hier aus dem Dictionary
myDict.pop(' ')

# For-Loop zum Erstellen einer Liste, die wir sortieren können
for key, value in myDict.items():
  myList.append([value, key])

for i in range(3):
  maximum = myList[0]
  for x in myList:
    if x > maximum:
      maximum = x
  sortedList.append(maximum)
  myList.remove(maximum)

print("Die drei häufigsten Zeichen sind {}, {} und {}.".format(sortedList[0][1], sortedList[1][1], sortedList[2][1]))
