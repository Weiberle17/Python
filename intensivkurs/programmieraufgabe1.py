string = "Python ist sooo eine tolle Programmiersprache!"
myDict = {}
list = []

for char in string:
  if char not in myDict:
    myDict[char] = 1
  else:
    myDict[char] = myDict[char] + 1
myDict.pop(' ')

for key, value in myDict.items():
  list.append((value, key))
list.sort()

print(list)
