with open("text.csv", "r") as name_surname:
    people = name_surname.readlines()
    for line in people[1:]:
        print(line.split(",")[0],"is", line.split(",")[2],"and", line.split(",")[1], "years old.")
    name_surname.close()

