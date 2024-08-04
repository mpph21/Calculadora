from model.funciones import (suma, resta, multiplicacion, division, potencia, raiz_cuadrada, seno, coseno, tangente)
from model.historial import agregar_al_historial, obtener_historial, borrar_historial

class CalculadoraModelView:
    def __init__(self):
        self.valor_a = 0
        self.operacion = ""

    def operar(self, simbolo, valor_a):
        self.valor_a = valor_a
        self.operacion = simbolo

    def resultado(self, valor_b):
        if self.operacion == '+':
            resultado = suma(self.valor_a, valor_b)
        elif self.operacion == '-':
            resultado = resta(self.valor_a, valor_b)
        elif self.operacion == '*':
            resultado = multiplicacion(self.valor_a, valor_b)
        elif self.operacion == '^':
            resultado = potencia(self.valor_a, valor_b)
        elif self.operacion == '/':
            resultado = division(self.valor_a, valor_b)
        else:
            resultado = "Error"
        agregar_al_historial(resultado)
        return resultado

    def operacion_avanzada(self, func, valor):
        try:
            resultado = func(valor)
            agregar_al_historial(resultado)
            return resultado
        except Exception:
            return "Error"
