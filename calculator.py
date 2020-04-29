cifra1 = int(input("Vnesi prvo številko!:"))
cifra2 = int(input("Vnesi drugo številko!:"))
racun = (input("Vnesi željeno računsko operacijo, izbiraš lahko med seštevanjem +, odštevanjem - , množenjem * in deljenjem / ! "))


if racun == "+":
    print("Rezultat je:", cifra1 + cifra2)
elif racun == "-":
    print("Rezultat je:", cifra1 - cifra2)
elif racun == "*":
    print("Rezultat je:", cifra1 * cifra2)
elif racun == "/":
    rezultat = float(cifra1 / cifra2)
    rezultat = round(rezultat, 3)
    print("Rezultat je:", rezultat)
else:
    print("Vnesel nisi pravilne operacije, poizkusi znova!")