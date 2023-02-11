blitzer = [
  {"uhrzeit": "12:43:17", "geschwindigkeit": 37, "kennzeichen": "TÜ-TL1234"},
  {"uhrzeit": "12:44:01", "geschwindigkeit": 35, "kennzeichen": "TÜ-FL999"},
  {"uhrzeit": "12:44:57", "geschwindigkeit": 45, "kennzeichen": "RT-ZZ321"},
  {"uhrzeit": "12:47:13", "geschwindigkeit": 51, "kennzeichen": "K-FC48"},
  {"uhrzeit": "12:44:57", "geschwindigkeit": 38, "kennzeichen": "RT-R777"},
  {"uhrzeit": "12:51:17", "geschwindigkeit": 42, "kennzeichen": "TÜ-XY1"},
  {"uhrzeit": "12:51:29", "geschwindigkeit": 40, "kennzeichen": "LEO-Z4"},
  {"uhrzeit": "12:54:00", "geschwindigkeit": 43, "kennzeichen": "TÜ-AB656"},
]

ergebnisDict = {}

for blitz in blitzer:
  i = blitz["kennzeichen"].index("-")
  bezirk = blitz["kennzeichen"][0:i]
  if bezirk in ergebnisDict:
    ergebnisDict[bezirk].append(blitz["geschwindigkeit"])
  else:
    ergebnisDict[bezirk] = [blitz["geschwindigkeit"]]

for bezirk, geschwindigkeiten in ergebnisDict.items():
  ergebnisDict[bezirk] = sum(geschwindigkeiten) / len(geschwindigkeiten)

print(ergebnisDict)
