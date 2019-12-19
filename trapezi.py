import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x)

print("questo programma calcola l'integrale di log(x) in [a,b]")
a = input("inserisci il valore di a: ")
b = input("inserisci il valore di b: ")
while N < 2:
    N = input("su quanti intervalli vuoi integrare (edevono essere almeno 2)? --->")
x = np.linspace(a,b,N+1)
h = np.fabs(b-a)/(N-1)
for i in range(1,N):
    g += f(x)
I = (h / 2) * (f(a) + f(b) + 2*g)
print("l'integrale calcolato e':",I)
