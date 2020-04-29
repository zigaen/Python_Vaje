string = ""
response = ""
while True:
    string = input("Input a random sentence, use lower and uppercase: ")
    response = input("Would you like to see lowercase transition of your sentence? (Y/N):  ")
    response = response.lower()
    if response == "y":
        print(string.lower())
        continue
    elif response == "n":
        print("Goobye!")
        break
    elif response == "":
        continue
    else:
        print("Enter Y or N !")

