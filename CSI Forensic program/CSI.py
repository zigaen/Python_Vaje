import json
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

with open("dna.txt", "r") as dna:
    dna_string = dna.read()
    print("DNA sequence is: " + dna_string)


#hair_black = "CCAGCAATCGC"
#hair_brown = "GCCAGTGCCG"  #! 182
#hair_blonde = "TTAGCTATCGC"
Hair_color = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]

#shape_square = "GCCACGG" #! 47
#shape_round = "ACCACAA"
#shape_oval = "AGGCCTCA"
Facial_shape = ["GCCACGG", "ACCACAA", "AGGCCTCA"]

#eye_blue = "TTGTGGTGGC"
#eye_green = "GGGAGGTGGC" #! 216
#eye_brown = "AAGTAGTGAC"
Eye_color = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]

Gender = ["TGAAGGACCTTC", "TGCAGGAACTTC" ]
#female = "TGAAGGACCTTC"
#male = "TGCAGGAACTTC" #! 281

Race = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]
#white = "AAAACCTCA" #! 321
#black = "CGACTACAG"
#asian = "CGCGGGCCG"


print("Scanning dna.txt for instances of dna: ")

i = 0
j = 0
k = 0
h = 0
g = 0

while i <= 2:
    a = dna_string.find(str(Hair_color[i]))
    if  a > 0:
        print("Collor of hair is :" + str(Hair_color[i]))
        hair = Hair_color[i]
        break
    else:
        i = i + 1

while j <= 2:
    a = dna_string.find((Facial_shape[j]))
    if  a > 0:
        print("Face shape is: " + str(Facial_shape[j]))
        shape = Facial_shape[j]
        break
    else:
        j = j + 1

while k <= 2:
    a = dna_string.find((Eye_color[k]))
    if  a > 0:
        print("Eye color is:" + str(Eye_color[k]))
        eye = Eye_color[k]
        break
    else:
        k = k + 1

while h <= 2:
    a = dna_string.find((Gender[h]))
    if  a > 0:
        print("Gender:" + str(Gender[h]))
        gender = Gender[h]
        break
    else:
        h = h + 1

while g <= 2:
    a = dna_string.find((Race[g]))
    if  a > 0:
        print("Rasa :" + str(Race[g]))
        rasa = Race[g]
        break
    else:
        g = g + 1

with open("suspect_list.txt", "r") as suspects:
    suspects_list = json.loads(suspects.read())

#check for all DNA characteristics

response = input("Would you really like to find out, who the suspect is? (y/n) : ")
response = response.lower()
if response == "y":
    w = 0
    while w < 4:
        if suspects_list[w]["Gender"] == gender and suspects_list[w]["Race"] == rasa and suspects_list[w]["Hair_color"] == hair and suspects_list[w]["eye_color"] == eye and suspects_list[w]["face_shape"] == shape:
           print("Our suspect is : " + suspects_list[w]["Name"])
        w = w + 1
else:
    print("Yeah, truth hurts. better not to know! ")



