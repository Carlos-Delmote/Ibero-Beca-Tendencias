#librerias
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#seleccione el test
test = '2'

#obtener el nombre de la prueba
queryName = "SELECT Name FROM Test where Test=" + test
connT = sqlite3.connect('Seebeck.db') 
t = connT.cursor()
t.execute(queryName)
names = t.fetchall()
for name in names[0]:
    a=0

#obtener datos de la prueba
query = "SELECT Voltage*100 as Voltaje, HTemp-LTemp as Dif_Temp, (HTemp-LTemp)*0.35 as V_Teorico FROM Measurements where Test=" + test

connM = sqlite3.connect('Seebeck.db') 
m = connM.cursor()
m.execute(query)

df = pd.DataFrame(m.fetchall(), columns = ['Voltaje', 'Dif_Temp', 'V_Teorico'])

#configurar la pantalla
df.plot( title = name,  ylabel ='Temp °C, Voltaje Vx10²', xlabel='Minutos')
plt.show()