import os
telbuch = []
if os.path.isfile("telbuch.txt"):
  with open("telbuch.txt", "r", encoding="utf-8") as tb:
    for zeile in tb:
      telbuch.append(zeile.rstrip().split(":"))

while True:
  print("------------------------------------------------------------------")
  print("Was möchten Sie machen? Geben Sie eine der folgenden Ziffern ein:")
  print("1: Telefonbuch ausgeben")
  print("2: Neuen Telefonbucheintrag erstellen")
  print("3: Telefonnummer suchen")
  print("4: Programm beenden")

  ziffer = int(input("Ziffer: "))

  if ziffer == 1:
    print("Telefonbuch:")
    for eintrag in telbuch:
      print("{}: {}".format(eintrag[0], eintrag[1]))

  if ziffer == 2:
    name = input("Name: ")
    telnum = input("Telefonnummer: ")
    telbuch.append([name ,telnum])
    with open("telbuch.txt", "a", encoding="utf-8") as tb:
      tb.write("{}: {}".format(name, telnum))
    print("Eintrag hinzugefügt")

  if ziffer == 3:
    such = input("Suchtext: ")
    treffer = [e for e in telbuch if such.lower() in e[0].lower()]
    if len(treffer) == 0:
      print("Keine Einträge mit Suchtext {} gefunden".format(such))
    else:
      for eintrag in treffer:
        print("{}: {}".format(eintrag[0], eintrag[1]))
    
  if ziffer == 4:
    print("Ciao")
    break
