number = int(input("Enter a number"))
if number % 3 == 0 and number % 5 == 0:
    number = True
    if number == True:
        print("FizzBuzz")
if number % 3 == 0:
    number = True
    if number == True:
        print("Fizz")
if number % 5 == 0:
    number = True
    if number == True:
        print("Buzz")