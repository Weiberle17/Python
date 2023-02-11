def collatz_function(number):
  while number != 1:
    if number%2 == 0:
        number = int(number/2)
    else:
        number = int(number*3+1)
    print(number)

collatz_function(15)
