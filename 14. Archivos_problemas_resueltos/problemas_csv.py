#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("14. Archivos_problemas_resueltos\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos "dalto" por "maestro"
df['apellido'].replace("dalto","maestro",inplace=True)

#mostrando la columna apellido
#print(df['apellido'])

print(df)
df = df.dropna()
print(df)













