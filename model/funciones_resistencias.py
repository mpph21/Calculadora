# funciones_resistencias.py

# Diccionario con los valores de los colores
colores_bandas = {
    'Negro': 0, 'Marrón': 1, 'Rojo': 2, 'Naranja': 3, 'Amarillo': 4,
    'Verde': 5, 'Azul': 6, 'Violeta': 7, 'Gris': 8, 'Blanco': 9
}

# Diccionario con los multiplicadores de las bandas
multiplicadores = {
    'Negro': 1, 'Marrón': 10, 'Rojo': 100, 'Naranja': 1000, 'Amarillo': 10000,
    'Verde': 100000, 'Azul': 1000000, 'Violeta': 10000000, 'Gris': 100000000, 'Blanco': 1000000000,
    'Oro': 0.1, 'Plata': 0.01
}

# Diccionario con las tolerancias
tolerancias = {
    'Marrón': 1, 'Rojo': 2, 'Verde': 0.5, 'Azul': 0.25, 'Violeta': 0.1,
    'Gris': 0.05, 'Oro': 5, 'Plata': 10
}

def calcular_resistencia(banda1, banda2, banda3, tolerancia):
    # Calcula el valor de la resistencia
    valor = (colores_bandas[banda1] * 10 + colores_bandas[banda2]) * multiplicadores[banda3]
    # Obtiene la tolerancia
    tolerancia_valor = tolerancias[tolerancia]
    return valor, tolerancia_valor
