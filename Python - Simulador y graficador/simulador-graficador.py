#Librerías
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as smp
from scipy.integrate import quad
from scipy.integrate import cumulative_trapezoid

#Lectura de datos SQL
data = pd.read_csv('Final_Measurements.csv')
#Diferencial de temperatura
DTemp = data.htemp - data.ltemp

#Gráfica de datos experimentales
x = data.time
y = data.voltage * 100
#El Coeficiente Seebeck del cobre es 0.0035
y2 = DTemp * 0.32
z = DTemp
z2 = data.htemp
z3 = data.ltemp
plt.plot(x, y, color = 'black')
plt.plot(x, y2, color = 'orange')
plt.plot(x, z)

#Valor teórico
plt.plot(x,y2)
plt.xlabel("Time")
plt.ylabel("Voltaje en V x 10^2 \n" + "Temperatura en °C")
plt.legend(["Voltaje (Vx10^2)", "Voltaje teórico (Vx10^2)", "Diferencial de temperatura (°C)"])
plt.show()

#Notas
#Test 1 = Prueba con datos falsos
#Test 2 = Primeras mediciones en clime nublado
#Test 3 = Nube densa
#Test 100 = Celda Peltier sin termosifón ni parábola