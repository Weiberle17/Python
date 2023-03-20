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

