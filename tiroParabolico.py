import numpy as np
import matplotlib.pyplot as plt

# Codigo para simular y graficar un tiro parabólico encontrando el mejor ángulo de forma tal que el alcance horizontal del disparo sea máximo.

def calcular_alcance_horizontal(velocidad_inicial, angulo, gravedad=9.81):
    velocidad_horizontal = velocidad_inicial * np.cos(np.deg2rad(angulo))
    tiempo_vuelo = (2 * velocidad_inicial * np.sin(np.deg2rad(angulo))) / gravedad
    alcance_horizontal = velocidad_horizontal * tiempo_vuelo
    return alcance_horizontal

# Parámetros iniciales
velocidad_inicial = 10  # m/s
angulos = np.linspace(0, 90, 90)  # Ángulos de 0 a 90 grados
mejor_alcance = 0
mejor_angulo = 0

# Iterar sobre los ángulos y calcular el alcance horizontal
for angulo in angulos:
    alcance = calcular_alcance_horizontal(velocidad_inicial, angulo)
    if alcance is not None and alcance > mejor_alcance:
        mejor_alcance = alcance
        mejor_angulo = angulo

print(f"El mejor ángulo es: {round(mejor_angulo,2)} grados")
print(f"Alcance máximo: {round(mejor_alcance,2)} metros")

# Graficar el recorrido en el eje x y eje y para el mejor ángulo
tiempo_total = (2 * velocidad_inicial * np.sin(np.deg2rad(mejor_angulo))) / 9.81
tiempo = np.linspace(0, tiempo_total, 100)
posicion_x = velocidad_inicial * np.cos(np.deg2rad(mejor_angulo)) * tiempo
posicion_y = velocidad_inicial * np.sin(np.deg2rad(mejor_angulo)) * tiempo - 0.5 * 9.81 * tiempo ** 2

plt.plot(posicion_x, posicion_y)
plt.title('Tiro parabólico')
plt.xlabel('Distancia (m)')
plt.ylabel('Altura (m)')
plt.grid(True)
plt.show()
