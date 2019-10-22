

import matplotlib.pyplot as plt
import random


def oppgave1():
    """ Printer ut store tall i kort og lang form,
        ofte kalt amerikansk og britisk form.
    """
    store_tall = [
        ["Million",    "10^6 ", "10^6 "],
        ["Milliard",   "     ", "10^9 "],
        ["Billion",    "10^9 ", "10^12"],
        ["Billiard",   "     ", "10^15"],
        ["Trillion",   "10^12", "10^18"],
        ["Quadrillion","10^15", "10^24"],
        ["Quintillion","10^18", "10^30"],
        ["Sextillion", "10^21", "10^36"]
    ]  # Hentet fra https://en.wikipedia.org/wiki/Names_of_large_numbers

    print("%-15s %9s %9s" % ("Navn", "lang", "Kort"))
    for i in store_tall:
        print("%-15s %9s %9s" % tuple(i))



# I billion USD (kort form)

microsoft_inntekt_dollar = [
    [2002, 28.37],
    [2003, 32.19],
    [2004, 36.84],
    [2005, 39.79],
    [2006, 44.28],
    [2007, 51.12],
    [2008, 60.42],
    [2009, 58.44],
    [2010, 62.48],
    [2011, 69.94],
    [2012, 73.12],
    [2013, 77.85],
    [2014, 86.83],
    [2015, 93.58],
    [2016, 85.32],
    [2017, 89.95],
    [2018, 110.36],
    [2019, 125.84]
]  # Hentet fra https://www.statista.com/statistics/267805/microsofts-global-revenue-since-2002/

#legger inn kursen
valuta = float(8.6862)


def oppgave2a():
    """ Henter en rekke tall fra brukeren og ut hva som
        var medianen i listen
    """

    tall_liste = []
    while True:
        bruker_input = input("Skriv inn tall (avslutt med ferdig): ")
        if bruker_input == "ferdig":
            break
        tall_liste.append(int(bruker_input))
    print("Dine tall:", tall_liste)

    tall_liste.sort()
    if len(tall_liste) % 2 == 0:
        ny_1 = int(len(tall_liste) /2)
        ny_2 = ny_1 - 1
        median = (tall_liste[ny_1] + tall_liste[ny_2]) /2
        print("Medianen til tallene: ", median)
    else:
        print("Medianen til tallene: ", tall_liste[int(len(tall_liste)/2)])

    pass
#kopierer listen
microsoft_inntekt_kroner_ny = microsoft_inntekt_dollar.copy()
def oppgave3a():
    """ Konverterer inntektene fra dollar til kroner
    uten å gjøre endringer på originallisten.
    """
    #multipliserer index i ny liste med valuta
    microsoft_inntekt_kroner = [valuta * i[-1] for i in microsoft_inntekt_kroner_ny]
    print("I NOK:", [float(round(n, 2)) for n in microsoft_inntekt_kroner])
    print("Orginal:", microsoft_inntekt_dollar)

    """ berge sin kommentar: for n in microsoft_inntekt_dollar:
            print("%-15s %-15s %10s" %(n[0], n[1], n[1]*usdtilNOK))"""



def oppgave3b():
    """ Tegner et histogram over inntektene til Microsoft
    """
    year = []
    inntekt = []
    for i in range(0, len(microsoft_inntekt_dollar)):
        year.append(microsoft_inntekt_dollar[i][0])
        inntekt.append(microsoft_inntekt_dollar[i][1])
    plt.bar(year, inntekt)
    plt.show()



def oppgave3c():
    """ Summerer opp inntektene til Microsoft
    """
    inntekt = []
    for i in range(0, len(microsoft_inntekt_dollar)):
        inntekt.append(microsoft_inntekt_dollar[i][1])
    total_milliard = sum(inntekt)
    total_billion = int(total_milliard * 100)
    print("Microsoft tjente", total_billion, "billioner dollar i perioden 2002-2019")


def print_kart(spiller, monster):
    x = 0
    while x <= 10:
        y = 0
        kart_liste = []
        while y <= 10:
            if x == spiller[1] and y == spiller[0]:
                kart_liste.append("S")
            elif x == monster[1] and y == monster[0]:
                kart_liste.append("M")
            else: kart_liste.append("* ")

            y = y + 1

        samlet = " ".join(kart_liste)

        print(samlet)

        x = x + 1

spiller = [2, 6]
monster = [4, 5]

def spiller_bevegelse():
    flytt = input()

    if flytt == "W":
        spiller[1] = spiller[1] - 1
    if flytt == "a":
        spiller[0] = spiller[0] - 1
    if flytt == "s":
        spiller[1] = spiller[1] + 1
    if flytt == "d":
        spiller[0] = spiller[0] + 1

    monster[0] = monster[0] + random.randint(-1, 1)
    monster[1] = monster[1] + random.randint(-1, 1)

def spill():

    print("wasd + enter for å bevege seg")
    print_kart(spiller, monster)

    try:
        while True:
                spiller_bevegelse()
                print_kart(spiller, monster)
    except KeyboardInterrupt:
        exit()





def main():
    """ Dette er filens main-funksjon, det er denne funksjonen som kjører
    når hele filen blir kjørt. 
    Hvis du vil kjøre en av oppgave-funksjonene nedenfor fjerner du #-tegnet 
    foran oppgave-funksjonen slik at den blir "skrudd på".
    Før du leverer kan det være lurt å sjekke alle funksjonene. Dette gjør 
    du ved å fjerne alle #-tegnene nedenfor.
    """
    oppgave1()
    print()
    oppgave2a()
    print()
    print()
    oppgave3a()
    print()
    oppgave3b()
    print()
    oppgave3c()
    print()
    spill()
    print()

main()
