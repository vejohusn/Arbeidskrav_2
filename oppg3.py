"""
Arbeidskrav 2 - OPPGAVE 3
USN - Python høst 2025
Omregning fra grader til radianer
av Vegard H. Johansen
Versjon 1
"""
#IMPORTS
import numpy as np


# OPPSTARTS INFORMASJON
print("************************************************************")
print("Program som regner om grader til radianer")
print("Skriv 'avslutt' istedet for grade-tallet eller ")
print("Trykk Ctrl+C for å avslutte program")
print("************************************************************")

# FUNKSJON FOR Å MOTTA INNDATA (grader) FRA BRUKEREN AV PROGRAMMET OG REGNE UT GRADER TIL RADIANER
def utregning(): 
        
    v_grad = input('Skriv inn gradtallet: ') # Input som gir gradtallet

    if(v_grad.lower() == "avslutt"): #Legger inn en betingelse hvis bruker skriver avslutt istedet for km så avsluttes programmet
        exit()                        #Konverterer input til småbokstaver for å sikre hvis bruker skriver med store bokstaver eller en blading
    
    try: # Gjør sjekk på input data fra brukerern
        v_grad = float(v_grad) # Gjør om input il float
        v_rad = round(v_grad*np.pi/180, 5) # Returnerer verdi for beregning hvis det er et tall i rett format.
        print(f"Tallet {v_grad} i grader som du skrev inn, tilsvarer {v_rad} i radianer")
    except ValueError:
        print("---FEIL---") # Skriver to linjer med tilbakemelding til brukeren om at han har skrevet inn feil format eller verdi.
        print("Du må skrive inn en grad i heltall eller desimaltall f.eks 3.23")


# EN WHILE LØKKE SOM KALLER UTREGNINGSFUNKSJONEN HELT TIL MAN AVSLUTTER PROGRAMMET MED Å AVSLUTTE DET MED CTRL+C ELLER SKRIVE AVSLUTT
while True:
    utregning()


