#Librerías
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de datos SQL
data = pd.read_csv('TEST2.csv')

#Diferencial de temperatura
DTemp = data.HTemp - data.LTemp

#Gráfica de datos experimentales
x = data.Time
y = data.Voltage * 100
#El Coeficiente Seebeck del cobre es 0.0035
y2 = DTemp * 0.0035 * 100
z = DTemp
plt.plot(x, y)
plt.plot(x, z)
#Valor teórico
plt.plot(x,y2)
plt.title("Al amanecer")
plt.xlabel("Time")
plt.ylabel("Voltaje en V x 10^2 \n" + "Temperatura en °C")
plt.legend(["Voltaje (Vx10^2)", "Diferencial de temperatura (°C)", "Voltaje teórico (Vx10^2)"])
plt.show()

