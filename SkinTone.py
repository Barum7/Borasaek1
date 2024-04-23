from pyswip import Prolog
import tkinter as tk
from tkinter import messagebox

# Cargar la base de conocimiento de Prolog
prolog = Prolog()
prolog.consult("C:/Users/beatr/OneDrive/Desktop/new.pl")

# Función para mostrar la imagen y el mensaje en una ventana personalizada
def mostrar_imagen_y_mensaje(mensaje, imagen_path):
    # Crear una ventana Toplevel
    ventana_imagen = tk.Toplevel(ventana)
    # Establecer el color de fondo de la ventana
    ventana_imagen. config(bg='White')
    # Establecer el tamaño de la ventana
    ventana_imagen.geometry("250x300+500+200")
    # Establecer el icono de la ventana
    ventana_imagen.iconbitmap(r"D:\python\programas\pythonPROLOG DANI\fashion_23852.ico")
    # Crear una etiqueta para mostrar el mensaje
    mensaje_label = tk.Label(ventana_imagen, text=mensaje)
    mensaje_label.pack()
    mensaje_label.config(fg="#FFB6C1", font=("Segoe Script", 25, "italic"), bg="White")
    # Cargar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    # Crear una etiqueta para mostrar la imagen
    imagen_label_local = tk.Label(ventana_imagen, image=imagen)
    imagen_label_local.pack()

    # Hacer que la ventana se muestre sobre la ventana principal
    ventana_imagen.transient(ventana)
    # Hacer que la ventana se enfoque y capture los eventos
    ventana_imagen.grab_set()
    # Esperar a que la ventana se cierre
    ventana.wait_window(ventana_imagen)

# Función para determinar el tono de la persona
def determinar_tono():
    # Obtener los valores seleccionados en los radiobuttons
    vena = vena_var.get()
    piel = piel_var.get()
    # Realizar una consulta a la base de conocimiento de Prolog
    query = prolog.query(f"determinar_tono(Tono, '{vena}', '{piel}')")
    solutions = list(query)

    if solutions:
        # Obtener el tono de la persona
        tono = solutions[0]["Tono"]
        # Establecer el mensaje a mostrar
        mensaje = "Tus Colores"
        # Determinar la imagen a mostrar según el tono de la persona
        if tono == "calido":
            imagen_path = r"C:\Users\beatr\OneDrive\Desktop\FOTO COLOR DANI\3.1.png"
        elif tono == "frio":
            imagen_path = r"C:\Users\beatr\OneDrive\Desktop\FOTO COLOR DANI\1.1.png"
        elif tono == "neutral":
            imagen_path = r"C:\Users\beatr\OneDrive\Desktop\FOTO COLOR DANI\2.1.png"
        else:
            # Mostrar un mensaje de error si el tono no es reconocido
            messagebox.showerror("Error", "Tono no reconocido.")
            return

        # Mostrar la imagen y el mensaje en una ventana personalizada
        mostrar_imagen_y_mensaje(mensaje, imagen_path)
    else:
        # Mostrar un mensaje de error si no se encuentra una persona con las características seleccionadas
        messagebox.showerror("IMPOSIBLE", "No hay persona con tales características.")

# Crear la interfaz gráfica (Ventana Principal)
ventana = tk.Tk()
ventana.title("Colorimetria")

# Variables para los radiobuttons
vena_var = tk.StringVar()
piel_var = tk.StringVar()

# Etiquetas y radiobuttons
ventana.resizable(False, False)
ventana.geometry("250x300+500+200")
ventana.config(bg='#FFB6C1')
ventana.iconbitmap(r"D:\python\programas\pythonPROLOG DANI\fashion_23852.ico")

# Crear una etiqueta para mostrar el nombre del programa
nombre = tk.Label(ventana, text="Tone-Skin")
nombre.config(fg="White", font=("Segoe Script", 25, "italic"), bg='#FFB6C1')
nombre.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Crear etiquetas y radiobuttons para el color de piel
tk.Label(ventana, text="Color de Piel:", bg='#FFB6C1').grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(ventana, text="Amarillenta", variable=piel_var, value="amarillenta", bg='#FFB6C1').grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(ventana, text="Oscura", variable=piel_var, value="oscura", bg='#FFB6C1').grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(ventana, text="Pálida", variable=piel_var, value="pálida", bg='#FFB6C1').grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(ventana, text="Rosada", variable=piel_var, value="rosada", bg='#FFB6C1').grid(row=5, column=0, padx=10, pady=5, sticky="w")

# Crear etiquetas y radiobuttons para el color de venas
tk.Label(ventana, text="Color de Venas:", bg='#FFB6C1').grid(row=1, column=1, padx=10, pady=5, sticky="e")
tk.Radiobutton(ventana, text="Verde", variable=vena_var, value="verde", bg='#FFB6C1').grid(row=2, column=1, padx=10, pady=5, sticky="e")
tk.Radiobutton(ventana, text="Violeta", variable=vena_var, value="violeta", bg='#FFB6C1').grid(row=3, column=1, padx=10, pady=5, sticky="e")
tk.Radiobutton(ventana, text="Azul", variable=vena_var, value="azul", bg='#FFB6C1').grid(row=4, column=1, padx=10, pady=5, sticky="e")

# Crear una etiqueta para mostrar la imagen
imagen_label = tk.Label(ventana)
imagen_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Crear un botón para determinar el tono
tk.Button(ventana, text="Determinar Tono", command=determinar_tono).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()