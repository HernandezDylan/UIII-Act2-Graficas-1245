
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Hernadez Dylan NC: 1245

# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 peliculas con 4 elementos por lista

avt = ['Avatar', 2.9, False, 2009]
end = ['Avengers: Endgame', 2.7, False, 2019]
ttn = ['Titanic', 2.2, True, 1997]
sw7 = ['Star Wars VII', 2.0, False, 2015]
inf = ['Avengers: Infinity War', 2.0, False, 2018]

# Creamos una lista de listas
lista_peliculas = [avt, end, ttn, sw7, inf]

# Utilizar pandas para organizar la tabla (DataFrame)
# A cada columna le ponemos nombre

df_peliculas = pd.DataFrame(
    lista_peliculas,
    columns=["Titulo", "Recaudacion", "Gano_Oscar", "Año"]
)

print(df_peliculas)

# Creamos el archivo CSV y lo guardamos
# df_peliculas.to_csv("peliculas.csv", index=False)

# Crear grafica de lineas
# X es el titulo en el eje horizontal
# Y es la recaudacion en el eje vertical

plt.plot(df_peliculas["Titulo"], df_peliculas["Recaudacion"])
plt.title("Grafica de peliculas 1245")
plt.xlabel("Nombre de las peliculas")
plt.ylabel("Recaudacion en billones USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Creamos una grafica de puntos

plt.scatter(df_peliculas["Titulo"], df_peliculas["Recaudacion"])
plt.title("Grafica de puntos 1245")
plt.xlabel("Peliculas")
plt.ylabel("Recaudacion en billones USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafica de barras

plt.bar(df_peliculas["Titulo"], df_peliculas["Recaudacion"])

# Etiquetas y titulo
plt.title("Peliculas 1245")
plt.xlabel("Las peliculas")
plt.ylabel("Recaudacion en billones USD")
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la grafica
plt.show()

# Ordenar la grafica de barras de manera descendente
# De la mas grande a la mas pequeña

df_peliculas_ordenar = df_peliculas.sort_values(
    "Recaudacion", ascending=False
)

plt.bar(df_peliculas_ordenar["Titulo"],
        df_peliculas_ordenar["Recaudacion"])
plt.title("Peliculas ordenadas 1245")
plt.xlabel("Peliculas")
plt.ylabel("Recaudacion en billones USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Coloreando la grafica

df_peliculas_ordenar = df_peliculas.sort_values(
    "Recaudacion", ascending=False
)

plt.bar(df_peliculas_ordenar["Titulo"],
        df_peliculas_ordenar["Recaudacion"],
        color=["b", "g", "c", "m", "y"])

plt.title("Peliculas con colores 1245")
plt.xlabel("Peliculas")
plt.ylabel("Recaudacion en billones USD")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafica de pastel

plt.pie(
    df_peliculas["Recaudacion"],
    labels=df_peliculas["Titulo"],
    autopct="%1.1f%%"
)

plt.title("Grafica de pastel peliculas 1245")
plt.show()

# Imprimir nombre y numero de control

print("Programa realizado por Hernadez Dylan NC: 1245")
