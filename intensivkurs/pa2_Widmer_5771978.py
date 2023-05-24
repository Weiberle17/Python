import argparse

# Argumente parsen. Diese Zeilen dürfen keinesfalls verändert werden! | Parsing arguments. You must not modify these lines!
parser = argparse.ArgumentParser()
parser.add_argument("statistic", choices=["avg", "max"], help="Which statistic should be run?")
parser.add_argument("variable", choices=["distance", "delay"], help="What variable should be used for the calculation?")
parser.add_argument("tsvfile", help="Name of data file to be analyzed")
parser.add_argument("--carrier", dest="carrier", help="Airline code of flights to be included")
parser.add_argument("--date", dest="date", help="Departure date for flights to be included")
parser.add_argument("--origin", dest="origin", help="Departure origin for flights to be included")
args = parser.parse_args()

# Ab hier die Lösung programmieren | Solution programming starts here ....

import pandas as pd
import time

#Datensatz importieren
try:
    flights = pd.read_csv (args.tsvfile, sep="\t")
except:
    print ("ERROR_INVALID_FILE")
    exit()
  

#Berechnung der wirklichen Verspätung als neue Spalte
flights["ACTUAL_DELAY"] = flights["DEPARTURE_DELAY"] + (flights["ACTUAL_DURATION"]-flights["PLANNED_DURATION"])

#Nullsetzen der negativen Verspätungen
flights.loc[flights["ACTUAL_DELAY"] < 0, "ACTUAL_DELAY"] = 0

#erlaubte Datumsformate festlegen
date_formats = ["%Y-%m-%d", "%d.%m.%Y"]
date = []

#überprüfen, ob ein erlaubtes Format genutzt wurde, sonst Programm abbrechen
if args.date != None:
    try:
        date = time.strptime(args.date, date_formats[0])
    except:
        try:
            date = time.strptime(args.date, date_formats[1])
        except:
            print ("ERROR_INVALID_DATE")
            exit()


#Filter durch optionale Argumente
#wenn Carrier angegeben, nur diese Zeilen anzeigen
if args.carrier != None:
    flights = flights[flights["CARRIER"] == args.carrier]

#wenn Datum angegeben, nur die Daten anzeigen
if args.date != None:
    flights = flights [(flights["DEPARTURE_YEAR"] == date[0]) & (flights["DEPARTURE_MONTH"] == date[1]) & (flights["DEPARTURE_DAY"] == date[2])]

#wenn Herkunft angegeben, nur diese Zeilen anzeigen
if args.origin != None:
    flights = flights[flights["ORIGIN"] == args.origin]

#wenn keine Flüge mit passenden Argumenten gefunden, Programm abbrechen
if flights.empty:
    print ("NO_MATCHING_FLIGHTS")
    exit()

#Grundfunktion des Programmes, Höchst- bzw. Durchschnittswerte für Distanz und Verspätung ausgeben
if (args.statistic == "max") and (args.variable == "distance"):
    print ("{:.0f}".format(flights["DISTANCE"].max()))
elif (args.statistic == "avg") and (args.variable == "distance"):
    print ("{:.1f}".format(flights["DISTANCE"].mean()))
elif (args.statistic == "max") and (args.variable == "delay"):
    print ("{:.0f}".format(flights["ACTUAL_DELAY"].max()))
elif (args.statistic == "avg") and (args.variable == "delay"):
    print ("{:.1f}".format(flights["ACTUAL_DELAY"].mean()))
