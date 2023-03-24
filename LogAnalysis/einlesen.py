# Columns:
# 'Timestamp',
# 'H100i ELITE CAPELLIX Fan #1',
# 'H100i ELITE CAPELLIX Fan #2',
# 'H100i ELITE CAPELLIX Fan #3',
# 'H100i ELITE CAPELLIX Fan #4',
# 'H100i ELITE CAPELLIX Fan #5',
# 'H100i ELITE CAPELLIX Pump',
# 'H100i ELITE CAPELLIX Coolant Temp'

import pandas as pd, glob, argparse

parser = argparse.ArgumentParser()
parser.add_argument("filedir", help="Name of Directory of Logfiles")
args = parser.parse_args()

logs = pd.concat(map(pd.read_csv, glob.glob(args.filedir + '*.csv')))

columns = []

for column in logs:
  columns.append(column)

logs['H100i ELITE CAPELLIX Coolant Temp Int'] = logs[columns[7]].str[0:5]
logs['H100i ELITE CAPELLIX Coolant Temp Int'] = logs['H100i ELITE CAPELLIX Coolant Temp Int'].astype('float')

logsMax = logs.loc[logs[columns[7]] == logs[columns[7]].max()]

print(logsMax)
print("Die maximale Temperatur betrug {}".format(logs[columns[7]].max()))
print("Die Durchschnittstemperatur beträgt: {:.2f}°C".format(logs['H100i ELITE CAPELLIX Coolant Temp Int'].mean()))
