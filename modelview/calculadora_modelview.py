import tkinter as tk
from tkinter import messagebox
from model.funciones import (suma, resta, multiplicacion, division, potencia)
from model.historial import agregar_al_historial

class CalculadoraModelView:
    def __init__(self):
        self.valor_a = 0
        self.operacion = ""

    def operar(self, simbolo, valor_a):
        try:
            # Verificar que valor_a es numérico
            self.valor_a = float(valor_a)
        except ValueError:
            # Mostrar mensaje de error si valor_a no es numérico
            messagebox.showerror("Error", "Valor inválido. Por favor, ingrese un número válido.")
            self.valor_a = 0
            self.operacion = ""
            return

        self.operacion = simbolo

    def resultado(self, valor_b):
        try:
            # Verificar que valor_b es numérico
            valor_b = float(valor_b)
            
            if self.operacion == '+':
                resultado = suma(self.valor_a, valor_b)
                calculo = f"{self.valor_a} + {valor_b}"
            elif self.operacion == '-':
                resultado = resta(self.valor_a, valor_b)
                calculo = f"{self.valor_a} - {valor_b}"
            elif self.operacion == '*':
                resultado = multiplicacion(self.valor_a, valor_b)
                calculo = f"{self.valor_a} * {valor_b}"
            elif self.operacion == '^':
                resultado = potencia(self.valor_a, valor_b)
                calculo = f"{self.valor_a} ^ {valor_b}"
            elif self.operacion == '/':
                if valor_b == 0:
                    raise ValueError("No se puede dividir por cero.")
                resultado = division(self.valor_a, valor_b)
                calculo = f"{self.valor_a} / {valor_b}"
            else:
                raise ValueError("Operación desconocida.")

            # Guardar en el historial con el cálculo y el resultado
            agregar_al_historial(calculo, resultado)
            return resultado

        except ValueError as e:
            # Mostrar un mensaje de error al usuario
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}\nPor favor, revisa la operación y los valores ingresados.")
            return "Error"