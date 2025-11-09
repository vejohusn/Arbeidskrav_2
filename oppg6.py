"""
Arbeidskrav 2 - OPPGAVE 6
USN - Python høst 2025
Plott f(x) = -x2 -5
av Vegard H. Johansen
Versjon 1
"""
    
import numpy as np
import matplotlib.pyplot as plt


# Funksjonen som gjør utregningen og returnerer svaret  
def f(x):
    return -x**2 - 5

# Numpy Array som inne verdiene -10 til 10 fordelt over 200 punkter   
x_array = np.linspace(-10,10,200)
    
# Tegner plottet og legger inn verdiene
plt.plot(x_array, f(x_array))
plt.title("PLOT SOM PLOTTER FUNKSJONEN f(x) = -x2 -5 OVER INTERVALLET -10,10")
plt.xlabel("X ARRAY")
plt.ylabel("VERDIER")
plt.grid() 
plt.show()