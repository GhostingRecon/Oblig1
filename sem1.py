#Oblig_1



#1

tall_1 = int(input("Tall nr 1: "))
tall_2 = int(input("Tall nr 2: "))
tall_3 = int(input("Tall nr 3: "))
print()

print("Tall nr 1: " + str(tall_1))
print("Tall nr 2: " + str(tall_2))
print("Tall nr 2: " + str(tall_3))


if tall_1 < tall_2 < tall_3:
    print("Strengt stigende")
elif tall_1 > tall_2 > tall_3:
    print("Strengt synkende")
else:
    print("Verken strengt stigende eller synkende")

#2

print()
#2.a



kort = input("Skriv inn \"kort tegn\" for konvertering (D, H, S, C): ").upper()

if kort == "D":
    print("Ruter")
elif kort == "H":
    print("Hjerter")
elif kort == "S":
    print("Spar")
elif kort == "C":
    print("Kløver")
else:
    print("ikke et tegn i kortstokken")

print()

#2.b
"""lager en array med alle tall og tegn"""

tegnDict = {
    "A": "Ess",
    "2": "To",
    "3": "Tre",
    "4": "Fire",
    "5": "Fem",
    "6": "Seks",
    "7": "Syv",
    "8": "Åtte",
    "9": "Ni",
    "10": "Ti",
    "J": "Knekt",
    "Q": "Dame",
    "K": "Konge"

}

"""Legger til upper her siden alle ord er med stor bokstav"""

bruker = input("tast inn tegn eller tall for konvertering: ").upper()

"""Printer så verdien"""

print(tegnDict[bruker])


print()

#2.a og 2.b

kort_konvertering = input("Skriv inn nummer og korttegn for konvertering: ").upper()

liste = list(kort_konvertering)



def kort(type):


    kortNummer = {
     "A": "Ess",
     "2": "To",
     "3": "Tre",
     "4": "Fire",
     "5": "Fem",
     "6": "Seks",
     "7": "Syv",
     "8": "Åtte",
     "9": "Ni",
     "10": "Ti",
     "J": "Knekt",
     "Q": "Dame",
     "K": "Konge"
}

    kortTegn = {
    "D": "Ruter",
    "H": "Hjerter",
    "S": "Spar",
    "C": "Kløver"
}
    return kortNummer[type[0]] + " " + kortTegn[type[1]]


print(kort(liste))

#3

print()

#3.a



valuta = {
    "EUR": 9.68551,
    "USD": 8.50373,
    "GBP": 11.0134,
    "SEK": 0.92950,
    "AUD": 6.06501,
    "NOK": 1.00000
}
print("valuttakalkulator til NOK")
verdiInput = float(input("Verdi for konvertering: "))
valutaInput = input("Fra hvilke valutta: ").upper()

print(verdiInput * valuta[valutaInput], "NOK")

print()
#3.b
"""skal bare gå andre veien her så da kan jeg bruke samme dictionary som i a"""

print("valutakalkulator fra NOK")
verdiInputFra = float(input("Verdi for konvertering: "))
valutaInputFra = input("Til hvilke valutta: ").upper()

print(verdiInputFra / valuta[valutaInputFra], valutaInputFra)

print()
#4
"""Printe ut alle heltall fra 0-9 i potens 3"""

for x in range(0, 10+1):
    print(str(x) + "**" + str(3),  "=", str(x**3))

#5.a
print()

inputStart = int(input("Start: "))
inputStop = int(input("Stop: "))
inputN = int(input("n: "))

print("Verdier mellom", str(inputStart), "og", str(inputStop),
          "som er delelige på", str(inputN) + ":")

for n in range(inputStart, inputStop+1):

    if n % inputN == 0:
        print(n)

print()
#6

#6.a

def tilFahrenheit(celsius):
    return int(celsius * 1.800)+32
print("Celsius    Fahrenheit")
for n in range(0, 100+1, 10):
    print("%7d %12d" % (n, tilFahrenheit(n)))


print()
#6.b

"""def tilFahrenheit(celsius):
    return int(celsius * 1.800)+32
print("Celsius    Fahrenheit    Status")
for n in range(0, 100+1, 10):

    if n >= 60:
        print("%7d %12d %s" % (n, tilFahrenheit(n), str("Jeg svetter ihjel! ")))
    else:
        print("7d %12d %s" % (n, tilFahrenheit(n) ,str("Jeg har det bra")))"""



def tilFahrenheit(celsius):
    return int(celsius * 1.800) + 32
print("Celsius    Fahrenheit    Stratus")
for n in range(0, 100+1, 10):
    if n >= 60:
        print("%7d %12d %23s" % (n, tilFahrenheit(n), str("jeg svetter ihjel! ")))
    else:
        print("%7d %12d %21s" % (n, tilFahrenheit(n), str("jeg har det bra. ")))

#7

print()

verdi = float(input("Hvor mye har du?: "))
fra = float(input("Fra år: "))
til = float(input("Til år: "))

def renteOkning(verdi, fra, til):

    tid = til - fra
    endring = verdiInputFra * (1.02 ** tid)
    return endring
print(round(renteOkning(verdi, fra, til), 2),
      "Kroner med 2% inflasjonsøkning")


