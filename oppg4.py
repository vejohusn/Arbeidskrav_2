"""
Arbeidskrav 2 - OPPGAVE 4
USN - Python høst 2025
Dictionary og antall innbyggere i hovedsteder
av Vegard H. Johansen
Versjon 1
"""
# DICTIONARY

data = {
     "Norge": ["Oslo", 0.634],
     "England": ["London", 8.982],
     "Frankrike": ["Paris", 2.161],
     "Italia": ["Roma", 2.873]
}


# OPPSTARTS INFORMASJON
print("*******************************************************************")
print("Program som finner antall inbyggere i en hovedstad basert på land")
print("Skriv 'avslutt' istedet for land eller ")
print("Trykk Ctrl+C for å avslutte program")
print("*******************************************************************")

# FUNKSJON FOR Å MOTTA INNDATA (land) FRA BRUKEREN AV PROGRAMMET OG PRINTE INBYGGERE EVT, KALLE FUNKSJON FOR Å LEGGE TIL
def inndata(): 
        
    land = input('Skriv inn land: ') # Input som gir landet

    land = land.lower() #Konverterer input til småbokstaver for å sikre hvis bruker skriver med store bokstaver eller en blading
    
    if(land == "avslutt"): #Legger inn en betingelse hvis bruker skriver avslutt istedet for verdi så avsluttes programmet
        exit()    

    land = land.capitalize() #Setter stor forbokstav for å sikre at alle skrivemåter inn blir konvertert slik dict er bygget opp. 


    try: # Gjør sjekk på input data fra brukerern
        if land in data:
            print(f"{data[land][0]} er hovedstaden i {land} og det er {data[land][1]} innbyggerer i {data[land][0]}")
        else:
            svar = input(f"Landet {land} finnes ikke i dataene, fil du legge det til? svar: J for ja eller N for nei: ")
            if svar.lower() == "j":
                ny_data(land) #Siden landet ikke finnes og bruker ønsker å legge det til kalles funksjon for å gjøre dette.
        
    except ValueError:
        print("---FEIL---") # Skriver to linjer med tilbakemelding til brukeren om at han har skrevet inn feil format eller verdi.
        print("Du må skrive inn et land")


# FUNKSJON SOM LEGGER ITL ET NYTT LAND
def ny_data(inn_land):
    hoved = input(f"Skriv inn hovedstadet i {inn_land} : ")
    innbygger = input(f"Skriv inn innbyggertallet i {inn_land} antall millioner (f.eks 0.550 for 550 000 innbyggere) : ")

    data[inn_land] = [hoved, innbygger]

    print(f"{data[inn_land][0]} er hovedstaden i {inn_land} og det er {data[inn_land][1]} innbyggerer i {data[inn_land][0]}")




# EN WHILE LØKKE SOM KALLER UTREGNINGSFUNKSJONEN HELT TIL MAN AVSLUTTER PROGRAMMET MED Å AVSLUTTE DET MED CTRL+C ELLER SKRIVE AVSLUTT
while True:
    inndata()


