#Escribe el siguiente código en el archivo visualizaciónTitanic.py para importar las bibliotecas matplotlib, seaborn, y numpy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Configurar el generador de números aleatorios
rng = np.random.RandomState(0)

#Generar un rango de valores en el eje X
x = np.linspace(0, 10, 500)

#Generar datos aleatorios y calcular la suma acumulativa
y = np.cumsum(rng.randn(500, 6), axis=0)

#Graficar los datos
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set() #Aplicar estilo de seaborn
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

y_val = x ** 2
plt.scatter(x, y_val, marker='s', color='g')
plt.title("Grafico de Dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()