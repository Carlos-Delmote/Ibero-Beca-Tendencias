#Librerías
import pandas as pd
import matplotlib.pyplot as plt

#Lectura de datos SQL
data = pd.read_csv('Measurements1.csv')
#Delimitar la gráfica a las pruebas reales e ignorar el resto de datos usado para pruebas
Idata = data[6 < data.index]
Pdata = Idata[ Idata.index < 62 ]
#Diferencial de temperatura
DTemp = Pdata.HTemp - Pdata.LTemp

#Gráfica de datos experimentales
x = Pdata.Time
y = Pdata.Voltage * 100
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

#Notas
#Test 1 = Prueba con datos falsos
#Test 2 = Primeras mediciones en clime nublado
#Test 3 = Nube densa
#Test 100 = Celda Peltier sin termosifón ni parábola