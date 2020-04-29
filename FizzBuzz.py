UPPER_COUNT_LIMIT = int(input("Select a number between 1 and 100!:  "))
number = 0

while number != UPPER_COUNT_LIMIT:
    number = number + 1
    if (number % 15) == 0:
        print("fizzbuzz")
    elif (number % 3) == 0:
        print("fizz")
    elif (number % 5) == 0:
        print("buzz")
    else:
        print(str(number))



