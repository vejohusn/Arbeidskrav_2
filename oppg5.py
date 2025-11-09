"""
Arbeidskrav 2 - OPPGAVE 5
USN - Python høst 2025
Regne ut areal og omkrets av en figur
av Vegard H. Johansen
Versjon 1
"""

#IMPORTS
import numpy as np 

# OPPSTARTS INFORMASJON
print("*******************************************************************")
print("Program som regner areal og omkrets av en figur")
print("*******************************************************************")



# Funksjon for å håndtere inn data
def inn_data():
    
    verdi_A = input("Skriv inn verdi A: ")
    verdi_B = input("Skriv innn verdi B: ")



    # Gjør en sjekk med try for å se at det er verdier som kan bli floats 
    try:
        verdi_A = float(verdi_A)
        verdi_B = float(verdi_B)
    except:
        print("Verdiene må være et heltall eller et desimaltall")
        exit()


    regn_ut(verdi_A, verdi_B) #Når riktige verdier er hentet, kaller funksjonen for å gjøre utregnigen

# Funskjon for å gjøre breregningene
def regn_ut(a,b):
    
    areal = round(((a**2 * np.pi)/2) + ((a*b)/2), 3) # Areal utregning anrundet til 3 desimaler


    omkrets = round((a*np.pi) + b + ((a**2 + b**2)**0.5), 3) # Omkretsutregning avrundet til 3 desimaler

    # Presenterer verdiene som tekst
    print(f"Arealet på figuren er {areal} ")
    print(f"Omkretsen av figuren er {omkrets} ")

# Kaller funskjonen inn_data for å starte programmet
inn_data()
