"""
Arbeidskrav 2 - OPPGAVE 2
USN - Python høst 2025
Beregninger pizza i klassefest
av Vegard H. Johansen
Versjon 1
"""
#IMPORTS
import math


# OPPSTARTS INFORMASJON
print("************************************************************")
print("Program som regner ut pizzaer du trenger til klassefesten")
print("Skriv 'avslutt' istedet for antall elever eller ")
print("Trykk Ctrl+C for å avslutte program")
print("************************************************************")

# FUNKSJON FOR Å MOTTA INNDATA (Antall elever) FRA BRUKEREN AV PROGRAMMET OG REGNE UT ANTALL PIZZA DU TRENGER
def utregning(): 
    while True: #Kjøres til den brytes av exit()
        
        antall_elev = input('Hvor mange elever skal delta på klassefesten ? ') # Input som gir antall elever

        if(antall_elev.lower() == "avslutt"): #Legger inn en betingelse hvis bruker skriver avslutt istedet for km så avsluttes programmet
            exit()                        #Konverterer input til småbokstaver for å sikre hvis bruker skriver med store bokstaver eller en blading
        
        try: # Gjør sjekk på input data fra brukerern
            pizza = math.ceil(int(antall_elev)*0.25) # Returnerer verdi for beregning hvis det er et tall i rett format.
            print(f"Basert på antall elever trenger du handle inn {pizza} pizza til klassefesten")
        except ValueError:
            print("---FEIL---") # Skriver to linjer med tilbakemelding til brukeren om at han har skrevet inn feil format eller verdi.
            print("Du må skrive inn et antall i heltall f.eks 3")


# EN WHILE LØKKE SOM KALLER UTREGNINGSFUNKSJONEN HELT TIL MAN AVSLUTTER PROGRAMMET MED Å AVSLUTTE DET MED CTRL+C ELLER SKRIVE AVSLUTT
while True:
    utregning()


