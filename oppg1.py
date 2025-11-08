"""
Arbeidskrav 2 - OPPGAVE 1
USN - Python høst 2025
Beregninger alder fra input i 2024
av Vegard H. Johansen
Versjon 1
"""


# OPPSTARTS INFORMASJON
print("************************************************************")
print("Program som regner ut din alder basert på fødselsår")
print("Skriv 'avslutt' istedet for fødselsår eller Trykk Ctrl+C for å avslutte program")
print("************************************************************")

# FUNKSJON FOR Å MOTTA INNDATA (Fødselsår) FRA BRUKEREN AV PROGRAMMET OG REGNE UT ALDER I 2024
def utregning(): 
    while True: #Kjøres til den brytes av exit()
        
        f_aar = input('Hvilket år er du født? ') # Input som gir fødsesår

        if(f_aar.lower() == "avslutt"): #Legger inn en betingelse hvis bruker skriver avslutt istedet for verdi så avsluttes programmet
            exit()                        #Konverterer input til småbokstaver for å sikre hvis bruker skriver med store bokstaver eller en blading
        
        try: # Gjør sjekk på input data fra brukerern
            alder = 2024 - int(f_aar) # Returnerer verdi for beregning hvis det er et tall i rett format.
            print(f"Basert på ditt fødselsår er din alder {alder} år i 2024")
        except ValueError:
            print("---FEIL---") # Skriver to linjer med tilbakemelding til brukeren om at han har skrevet inn feil format eller verdi.
            print("Du må skrive inn et år i heltall f.eks 1935")


# EN WHILE LØKKE SOM KALLER UTREGNINGSFUNKSJONEN HELT TIL MAN AVSLUTTER PROGRAMMET MED Å AVSLUTTE DET MED CTRL+C ELLER SKRIVE AVSLUTT
while True:
    utregning()


