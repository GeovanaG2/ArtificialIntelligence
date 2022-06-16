# ejecutar como:
# python program<n>.py
# n es el numero de programa
# Uso de pandas
#

# importamos librerias
import pandas as pd

# creamos un diccionario
d = {'hora':[1, 2, 4, 6, 10], 
     'lugar':['sala', 'cocina', 'comedor', 'baño', 'cuarto'],
     'cantidad':[2.2, 4.85, 5.22, 4.2, 6.56]}

# creamos el dataframe
df = pd.DataFrame(d)

#imprimimos el dataframe
print(df)
print()

# cambiamos el valor de los indices
df.index = ['A0', 'B0', 'C0', 'D0', 'E0']
print(df)
print()

# accedemos a todas las filas y columnas lugar y cantidad
print(df.loc[:, ['lugar', 'cantidad']])
print()

# accedemos a todas las fila y columnas lugar y cantidad
print(df.iloc[:, [1, 2]])