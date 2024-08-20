import tkinter as tk
from tkinter import ttk
from model.funciones_graficar import insertar_texto

class ModernButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.config(
            relief=tk.FLAT,
            bg="#D02090",  # violet red
            fg="white",
            activebackground="#B01776",  # dark violet red
            activeforeground="white",
            highlightthickness=0,
            bd=0,
            padx=12,
            pady=6,
            font=kw.get('font')
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.config(text=self.cget("text").lower())

    def on_enter(self, e):
        self['background'] = '#B01776'  # dark violet red

    def on_leave(self, e):
        self['background'] = '#D02090'  # violet red

def crear_boton(parent, entry, text, command, color='#D02090', hover_color='#B01776', font=None):
    btn = ModernButton(parent, text=text, command=lambda: command(entry), bg=color, activebackground=hover_color, font=font)
    btn.config(width=8, height=2)
    return btn

def crear_pestana_botones(parent, entry, botones, color, filas, columnas, font=None):
    frame = ttk.Frame(parent, style="Dark.TFrame")
    for i, (texto, comando) in enumerate(botones):
        crear_boton(frame, entry, texto, comando, color, font=font).grid(row=i//columnas, column=i%columnas, padx=4, pady=4, sticky="nsew")
    for i in range(filas):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(columnas):
        frame.grid_columnconfigure(i, weight=1)
    return frame


# Definición de botones
botones_basicos = [
    ('7', lambda entry: insertar_texto(entry, '7')), ('8', lambda entry: insertar_texto(entry, '8')), 
    ('9', lambda entry: insertar_texto(entry, '9')), ('+', lambda entry: insertar_texto(entry, '+')), 
    ('/', lambda entry: insertar_texto(entry, '/')), ('4', lambda entry: insertar_texto(entry, '4')), 
    ('5', lambda entry: insertar_texto(entry, '5')), ('6', lambda entry: insertar_texto(entry, '6')), 
    ('-', lambda entry: insertar_texto(entry, '-')), ('*', lambda entry: insertar_texto(entry, '*')), 
    ('1', lambda entry: insertar_texto(entry, '1')), ('2', lambda entry: insertar_texto(entry, '2')), 
    ('3', lambda entry: insertar_texto(entry, '3')), ('=', lambda entry: insertar_texto(entry, '=')), 
    ('^', lambda entry: insertar_texto(entry, '^')), ('0', lambda entry: insertar_texto(entry, '0')), 
    ('.', lambda entry: insertar_texto(entry, '.')), ('(', lambda entry: insertar_texto(entry, '(')), 
    (')', lambda entry: insertar_texto(entry, ')')), ('C', lambda entry: entry.delete(0, tk.END))
]

botones_trigo = [
    ('sin', lambda entry: insertar_texto(entry, 'sin(')), ('cos', lambda entry: insertar_texto(entry, 'cos(')), 
    ('tan', lambda entry: insertar_texto(entry, 'tan(')), ('asin', lambda entry: insertar_texto(entry, 'asin(')), 
    ('acos', lambda entry: insertar_texto(entry, 'acos(')), ('atan', lambda entry: insertar_texto(entry, 'atan('))
]

botones_log = [
    ('ln', lambda entry: insertar_texto(entry, 'ln(')), ('log', lambda entry: insertar_texto(entry, 'log(')), 
    ('log2', lambda entry: insertar_texto(entry, 'log2(')), ('e', lambda entry: insertar_texto(entry, 'e')), 
    ('10^', lambda entry: insertar_texto(entry, '10^')), ('exp', lambda entry: insertar_texto(entry, 'exp('))
]

botones_calculo = [
    ('d/dx', lambda entry: insertar_texto(entry, 'd/dx(')), ('∫', lambda entry: insertar_texto(entry, '∫(')), 
    ('lim', lambda entry: insertar_texto(entry, 'lim(')), ('sum', lambda entry: insertar_texto(entry, 'sum(')), 
    ('prod', lambda entry: insertar_texto(entry, 'prod('))
]

botones_varios = [
    ('|x|', lambda entry: insertar_texto(entry, 'abs(')), ('√', lambda entry: insertar_texto(entry, 'sqrt(')), 
    ('∛', lambda entry: insertar_texto(entry, 'cbrt(')), ('π', lambda entry: insertar_texto(entry, 'pi')), 
    ('%', lambda entry: insertar_texto(entry, '%')), ('mod', lambda entry: insertar_texto(entry, 'mod('))
]

