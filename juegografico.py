import tkinter as tk
from tkinter import messagebox
import random

# Función para determinar el resultado del juego
def jugar(opcion_usuario):
    opciones = ["piedra", "papel", "tijera"]
    opcion_computadora = random.choice(opciones)

    if opcion_usuario == opcion_computadora:
        resultado = "Empate"
    elif (
        (opcion_usuario == "piedra" and opcion_computadora == "tijera")
        or (opcion_usuario == "papel" and opcion_computadora == "piedra")
        or (opcion_usuario == "tijera" and opcion_computadora == "papel")
    ):
        resultado = "Ganaste"
    else:
        resultado = "Perdiste"

    messagebox.showinfo("Resultado", f"Elegiste {opcion_usuario}\nLa computadora eligió {opcion_computadora}\n\n{resultado}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("500x300")  # Ajustar el tamaño de la ventana
ventana.configure(bg="black")  # Fondo negro

# Contenedor para los botones
contenedor_botones = tk.Frame(ventana, bg="black")
contenedor_botones.pack(pady=20)

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana, text="Elige una opción:", bg="black", fg="white")
instrucciones_label.pack()

# Botones de opciones
piedra_button = tk.Button(contenedor_botones, text="Piedra", command=lambda: jugar("piedra"), width=10, height=2, bg="white", fg="black")
piedra_button.pack(side=tk.LEFT, padx=10)

papel_button = tk.Button(contenedor_botones, text="Papel", command=lambda: jugar("papel"), width=10, height=2, bg="white", fg="black")
papel_button.pack(side=tk.LEFT, padx=10)

tijera_button = tk.Button(contenedor_botones, text="Tijera", command=lambda: jugar("tijera"), width=10, height=2, bg="white", fg="black")
tijera_button.pack(side=tk.LEFT, padx=10)

# Ejecutar la ventana
ventana.mainloop()
