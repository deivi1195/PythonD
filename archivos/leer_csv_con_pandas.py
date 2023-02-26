import pandas as pd

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])

#obteniendo los datos de la columna nombre
nombres = df["name"]

print(df)

















