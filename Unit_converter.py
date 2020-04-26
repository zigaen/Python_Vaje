
compliance = input("Hi, i am converting km in to miles, would you like to continue? y/n  __ ")
while True:
    if compliance == "y":
        km = (input("Enter the number of kilometers:  "))
        km = float(km.replace(",", "."))
        miles = km * 1.60944
        print("That makes:  " + str(round(miles, 2)) + "   miles.")
        compliance = input("Would you like to make another conversion? y/n  __ ")
    elif compliance == "n":
        print("Ok Bye")
        break
    else:
        compliance = input("Please enter y or n !   ")



