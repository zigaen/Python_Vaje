with open("text.csv", "r") as name_surname:
    people = name_surname.readlines()
    for line in people[1:]:
        #possible option of solution, if you don't mind the brackets
        #case = [line.split(",")[0],"is", line.split(",")[2],"and", line.split(",")[1], "years old."]
        #print(case)
        name = line.split(",")[0]
        gender = line.split(",") [2]
        gender = gender.replace("\n","")
        age = line.split(",")[1]
        #an example of code writing that is not recomended
        #print(line.split(",")[2],"is", line.split(",")[0],"and", line.split(",")[1], "years old.")
        print(f"{name} is {gender} and {age} years old")
    name_surname.close()

