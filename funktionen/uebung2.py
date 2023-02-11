def add_multiply(*multiplicators, calculation="multiply"):
  if calculation == "add":
    return add(multiplicators)
  elif calculation == "multiply":
    return multiply(multiplicators)
  else:
    print("The only viable options for the second parameter are 'add' and 'multiply'")

def add(multiplicators):
  result = sum(multiplicators)
  return result

def multiply(multiplicators):
  result = 1
  for value in multiplicators:
    result *= value
  return result

print(add_multiply(1,2,3,4,5,6))
