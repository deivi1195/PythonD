import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#df = data frames.. filas||columnas
df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
df2 = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])

#obteniendo los datos de la columna nombre
nombres = df["name"]

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("age")

#ordenandolo de forma descendente
df_ordenandolo_descendente = df.sort_values("age",ascending=False)

#concatenando los dos data frame
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
#te muestra tantas filas como le indiques de arriba hacia abajo
primera_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
#te muestra tantas filas como le indiques de abajo hacia arriba
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
#shape es una propiedad
#filas_y_columnas_totales = df.shape
#(6,3)
#filas_totales = filas_y_columnas_totales[0]
#6
#columnas_totales = filas_y_columnas_totales[1]
#3

#desempaquetando
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()







print(df_info)

















