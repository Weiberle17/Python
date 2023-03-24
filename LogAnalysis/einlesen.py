# Columns:
# 'Timestamp',
# 'H100i ELITE CAPELLIX Fan #1',
# 'H100i ELITE CAPELLIX Fan #2',
# 'H100i ELITE CAPELLIX Fan #3',
# 'H100i ELITE CAPELLIX Fan #4',
# 'H100i ELITE CAPELLIX Fan #5',
# 'H100i ELITE CAPELLIX Pump',
# 'H100i ELITE CAPELLIX Coolant Temp'

import pandas as pd, glob

columns = []
logs = pd.concat(map(pd.read_csv, glob.glob('/home/weiberle/Logs/*.csv')))

for column in logs:
  columns.append(column)

logsMax = logs.loc[logs[columns[7]] == logs[columns[7]].max()]

print(logsMax)
