import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Función para calcular el tiempo de entrenamiento
def calcular_tiempo_entrenamiento():
    try:
        edad = int(entry_edad.get())
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        genero = genero_var.get()
        actividad = actividad_var.get()
        tipo_ingesta = ingesta_var.get()

        if genero == "Hombre":
            TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        else:
            TMB = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
        
        print ("Calorias de mantenimiento: " + str(TMB))

        actividad_fisica = {
            "Poco ejercicio": 1.2,
            "Ejercicio ligero (1-3 días)": 1.375,
            "Ejercicio moderado (3-5 días)": 1.55,
            "Ejercicio intenso (6-7 días)": 1.725
        }
        IC = TMB * actividad_fisica[actividad]
        
        print ("Injesta calorica: " +  str(IC))

        if tipo_ingesta == "Déficit calórico":
            deficit_calorico_final = IC - 800
        else:
            deficit_calorico_final = IC + 500
        
        print ("Deficit: " + str(deficit_calorico_final))

        deficit_calorico_final_normalizado = np.array([deficit_calorico_final / 1000.0])

        prediccion = model.predict(deficit_calorico_final_normalizado)
        tiempo_entrenamiento = prediccion[0][0]

        resultado_label.config(text=f"El tiempo recomendado de entrenamiento es: {tiempo_entrenamiento:.2f} minutos")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Función para visualizar la predicción
def plot_prediction():
    try:
        deficits = np.linspace(500, 1000, 100)
        deficits_normalizados = deficits / 1000.0
        tiempos_predichos = model.predict(deficits_normalizados)

        plt.figure(figsize=(10, 6))
        plt.plot(deficit_calorico, tiempo_entrenamiento, 'bo', label='Datos reales')
        plt.plot(deficits, tiempos_predichos, 'r-', label='Predicciones del modelo')
        plt.xlabel('Déficit calórico (calorías)')
        plt.ylabel('Tiempo de entrenamiento (minutos)')
        plt.title('Predicción del tiempo de entrenamiento basado en el déficit calórico')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para reiniciar los campos
def reiniciar_campos():
    entry_edad.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    genero_var.set('')
    actividad_var.set('')
    ingesta_var.set('')
    resultado_label.config(text='')

# Cargar y compilar el modelo
df = pd.read_csv('deficit_calorico_tiempo_entrenamiento.csv')
deficit_calorico = df['Deficit Calorico'].to_numpy()
tiempo_entrenamiento = df['Tiempo Entrenamiento (min)'].to_numpy()
deficit_calorico_normalizado = deficit_calorico / 1000.0

model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(deficit_calorico_normalizado, tiempo_entrenamiento, epochs=500)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Tiempo de Entrenamiento")

# Descargar la imagen desde la URL
url = "https://assets-global.website-files.com/5e0fdda1c7ec61ff259e5d42/654afb738cb77a9e0cd7408b_cb-open.png"
response = requests.get(url)
image_data = response.content
image = Image.open(BytesIO(image_data))
image = image.resize((500, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Crear el marco para el formulario
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Añadir la imagen al formulario
image_label = ttk.Label(frame, image=photo)
image_label.grid(row=0, columnspan=2, pady=10)

# Etiquetas y campos de entrada
ttk.Label(frame, text="Edad:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_edad = ttk.Entry(frame)
entry_edad.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Peso (kg):").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_peso = ttk.Entry(frame)
entry_peso.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Altura (cm):").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_altura = ttk.Entry(frame)
entry_altura.grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Género:").grid(row=4, column=0, sticky=tk.W, pady=5)
genero_var = tk.StringVar()
genero_combobox = ttk.Combobox(frame, textvariable=genero_var, state="readonly", width=23)
genero_combobox['values'] = ("Hombre", "Mujer")
genero_combobox.grid(row=4, column=1, pady=5)

ttk.Label(frame, text="Actividad Física:").grid(row=5, column=0, sticky=tk.W, pady=5)
actividad_var = tk.StringVar()
actividad_combobox = ttk.Combobox(frame, textvariable=actividad_var, state="readonly", width=23)
actividad_combobox['values'] = ("Poco ejercicio", "Ejercicio ligero (1-3 días)", "Ejercicio moderado (3-5 días)", "Ejercicio intenso (6-7 días)")
actividad_combobox.grid(row=5, column=1, pady=10)

ttk.Label(frame, text="Tipo de Ingesta:").grid(row=6, column=0, sticky=tk.W, pady=5)
ingesta_var = tk.StringVar()
ingesta_combobox = ttk.Combobox(frame, textvariable=ingesta_var, state="readonly", width=23)
ingesta_combobox['values'] = ("Déficit calórico", "Superávit calórico")
ingesta_combobox.grid(row=6, column=1, pady=5)

# Botón para calcular
calcular_button = ttk.Button(frame, text="Calcular", command=calcular_tiempo_entrenamiento)
calcular_button.grid(row=7, columnspan=2, pady=5)

# Etiqueta para mostrar el resultado
resultado_label = ttk.Label(frame, text="", font=("Helvetica", 12))
resultado_label.grid(row=8, columnspan=2, pady=5)

# Botón para mostrar la gráfica
grafica_button = ttk.Button(frame, text="Mostrar Gráfica", command=plot_prediction)
grafica_button.grid(row=9, columnspan=2, pady=5)

# Botón para reiniciar los campos
reiniciar_button = ttk.Button(frame, text="Nuevo Cálculo", command=reiniciar_campos)
reiniciar_button.grid(row=10, columnspan=2, pady=5)

root.mainloop()
