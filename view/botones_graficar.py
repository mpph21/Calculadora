import tkinter as tk
from tkinter import ttk

class ModernButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.config(
            relief=tk.FLAT,
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2",
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
        self['background'] = '#1976D2'

    def on_leave(self, e):
        self['background'] = '#2196F3'

def crear_boton(parent, entry, text, command, color='#2196F3', hover_color='#1976D2', font=None):
    btn = ModernButton(parent, text=text, command=lambda: command(entry), bg=color, activebackground=hover_color, font=font)
    btn.config(width=8, height=2)
    return btn

def crear_pestana_botones(parent, entry, botones, color, filas, columnas, font=None):
    frame = ttk.Frame(parent)
    for i, (texto, comando) in enumerate(botones):
        crear_boton(frame, entry, texto, comando, color, font=font).grid(row=i//columnas, column=i%columnas, padx=4, pady=4, sticky="nsew")
    for i in range(filas):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(columnas):
        frame.grid_columnconfigure(i, weight=1)
    return frame
