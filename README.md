# CBUM TRAINING TIME PREDICTION
### Una IA que recomienda cuanto tiempo entrenar según tu injesta calorica 🔥 

>En el mundo del fitness y la nutrición, encontrar el equilibrio perfecto entre la ingesta calórica y el tiempo de entrenamiento es crucial para alcanzar los objetivos personales,
>ya sea perder peso, ganar masa muscular o simplemente mantener un estilo de vida saludable. La relación entre las calorías consumidas y el tiempo dedicado al ejercicio puede ser
>compleja, ya que involucra múltiples variables y factores individuales.
>
>CBUM Training Time Prediction es una innovadora herramienta de inteligencia artificial diseñada para facilitar este proceso. Utilizando algoritmos avanzados de aprendizaje automático,
>esta aplicación predice el tiempo de entrenamiento óptimo basado en la ingesta calórica diaria del usuario. Con una interfaz gráfica de usuario (GUI) intuitiva y fácil de usar, CBUM Training
>Time Prediction ofrece recomendaciones personalizadas, ayudando a los usuarios a maximizar la eficacia de sus rutinas de ejercicio y alcanzar sus metas de manera más eficiente.

### Informacion basica para comprender más el proyecto
TMB significa Tasa Metabólica Basal (en inglés, Basal Metabolic Rate o BMR). Es la cantidad de energía que el cuerpo necesita para mantener las funciones vitales básicas, como la respiración, la circulación sanguínea y la regulación de la temperatura corporal, en estado de reposo. La TMB varía según la edad, el sexo, el peso y la altura de una persona.

La ecuación de Harris-Benedict es una fórmula utilizada para estimar la Tasa Metabólica Basal (TMB), la cual es la cantidad de calorías que una persona necesita diariamente para mantener sus funciones corporales en reposo. Esta ecuación se desarrolló a principios del siglo XX por los científicos James Arthur Harris y Francis Gano Benedict.

### Tecnologías Usadas 

En Este proyecto se utilizan varias tecnologías y bibliotecas para crear una aplicación gráfica, manipular imágenes, manejar datos y entrenar un modelo de aprendizaje automático. Aquí se detallan 
las principales tecnologías usadas:

**Tkinter**

Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI), se utiliza para crear la ventana principal, etiquetas, campos de entrada, botones y otras componentes de la interfaz gráfica.

**Pillow (PIL)**

Pillow es una biblioteca de procesamiento de imágenes en Python, se utiliza para descargar, redimensionar y mostrar una imagen en la interfaz gráfica.

**Requests**

Requests es una biblioteca de Python para realizar solicitudes HTTP, se utiliza para descargar una imagen desde una URL.

**NumPy**

NumPy es una biblioteca para realizar operaciones matemáticas y manejar arreglos multidimensionales, se utiliza para normalizar los datos de entrada y generar datos para la gráfica de predicciones.

**Pandas**

Pandas es una biblioteca para la manipulación y análisis de datos, se utiliza para cargar datos desde un archivo CSV.

**TensorFlow y Keras**

TensorFlow es una plataforma de código abierto para el aprendizaje automático, y Keras es una API de alto nivel para construir y entrenar modelos de redes neuronales, integrada en TensorFlow, se utilizan para construir, 
compilar y entrenar un modelo de red neuronal simple para predecir el tiempo de entrenamiento basado en el déficit calórico.

**Matplotlib**

Matplotlib es una biblioteca de gráficos en 2D para Python, se utiliza para crear y mostrar una gráfica que compara los datos reales con las predicciones del modelo de aprendizaje automático.

### ¿Como hacer qué funcione en mi sistema?
Para hacer funcionar el codigo tienes que relisar solo cuatro sensillos pasos:

1. **Descargar** los archivos que estan en el repositorio y guardalos en una carpeta.

2. **Preparar el entorno** asegurarce de tener Python instalado en el sistema

3. **Crear un entorno virtual** abre una terminal y navega hasta el directorio donde almacenaste el proyecto.

4. **Instalar las dependencias** instala las dependencias usando pip
-tkinter
-pillow
-requests
-numpy
-pandas
-tensorflow
-matplotlib

**Con estos pasos podras ejecutar el codigo sin ningun problema.**

### ¿Cómo funciona el código?

### Importaciones
- **tkinter:** Biblioteca para crear interfaces gráficas de usuario.

- **PIL (Pillow):** Biblioteca para manipular imágenes.

- **requests:** Biblioteca para hacer solicitudes HTTP.

- **numpy:** Biblioteca para trabajar con arreglos y funciones matemáticas.

- **pandas:** Biblioteca para manipulación y análisis de datos.

- **tensorflow y keras:** Bibliotecas para construir y entrenar modelos de aprendizaje automático.

- **matplotlib:** Biblioteca para crear gráficos.

```python
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
```
### Función para calcular el tiempo de entrenamiento
- Recopila datos ingresados por el usuario como edad, peso, altura, género, nivel de actividad física y tipo de ingesta calórica.
```python
def calcular_tiempo_entrenamiento():
    try:
        # Recopilar datos del usuario
        edad = int(entry_edad.get())
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        genero = genero_var.get()
        actividad = actividad_var.get()
        tipo_ingesta = ingesta_var.get()

```
- Calcula la Tasa Metabólica Basal (TMB) utilizando diferentes fórmulas según el género.
```python
        # Calcular TMB
        if (10 * peso) + (6.25 * altura) - (5 * edad) + 5
        else:
            TMB = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

```
- Calcula la ingesta calórica (IC) multiplicando la TMB por un factor correspondiente al nivel de actividad física.
```python
        # Calcular ingesta calórica
        actividad_fisica = {
            "Poco ejercicio": 1.2,
            "Ejercicio ligero (1-3 días)": 1.375,
            "Ejercicio moderado (3-5 días)": 1.55,
            "Ejercicio intenso (6-7 días)": 1.725
        }
        IC = TMB * actividad_fisica[actividad]
```
- Ajusta la ingesta calórica para obtener un déficit o superávit calórico según la selección del usuario.
```python
        # Calcular déficit o superávit calórico
        if tipo_ingesta == "Déficit calórico":
            deficit_calorico_final = IC - 800
        else:
            deficit_calorico_final = IC + 500
```
-Normaliza el déficit calórico dividiéndolo por 1000.
```python
        # Asegurarnos de que la entrada esté en el formato correcto
        deficit_calorico_final_normalizado = np.array([deficit_calorico_final / 1000.0])
```
- Utiliza el modelo entrenado para predecir el tiempo de entrenamiento basado en el déficit calórico normalizado.
```python
        # Predecir el tiempo de entrenamiento
        prediccion = model.predict(deficit_calorico_final_normalizado)
        tiempo_entrenamiento = prediccion[0][0]

```
- Muestra el resultado en la interfaz de usuario o un mensaje de error si algo falla.
```python
        # Mostrar el resultado en la etiqueta de resultado
        resultado_label.config(text=f"El tiempo recomendado de entrenamiento es: {tiempo_entrenamiento:.2f} minutos")
    except Exception as e:
        messagebox.showerror("Error", str(e))

```
### Función para visualizar la predicción
- Genera datos para la gráfica de predicciones del modelo.
```python
def plot_prediction():
    # Datos para la gráfica
    deficits = np.linspace(500, 1000, 100)
    deficits_normalizados = deficits / 1000.0
    tiempos_predichos = model.predict(deficits_normalizados)

```
- Crea y muestra una gráfica que compara los datos reales con las predicciones del modelo.
```python
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(deficit_calorico, tiempo_entrenamiento, 'bo', label='Datos reales')
    plt.plot(deficits, tiempos_predichos, 'r-', label='Predicciones del modelo')
    plt.xlabel('Déficit calórico (calorías)')
    plt.ylabel('Tiempo de entrenamiento (minutos)')
    plt.title('Predicción del tiempo de entrenamiento basado en el déficit calórico')
    plt.legend()
    plt.grid(True)
    plt.show()

```
### Función para reiniciar los campos
- Reinicia los campos de entrada y la etiqueta de resultado en la interfaz de usuario.
```python
def reiniciar_campos():
    entry_edad.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    genero_var.set('')
    actividad_var.set('')
    ingesta_var.set('')
    resultado_label.config(text='')

```
### Cargar y compilar el modelo
- Carga los datos de un archivo CSV y los normaliza.
```python
df = pd.read_csv('deficit_calorico_tiempo_entrenamiento.csv')
deficit_calorico = df['Deficit Calorico'].to_numpy()
tiempo_entrenamiento = df['Tiempo Entrenamiento (min)'].to_numpy()
deficit_calorico_normalizado = deficit_calorico / 1000.0

```
- Crea y entrena un modelo de red neuronal simple para predecir el tiempo de entrenamiento basado en el déficit calórico.
```python
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(deficit_calorico_normalizado, tiempo_entrenamiento, epochs=500)

```
### Crear la ventana principal
- Crea la ventana principal de la aplicación.
```python
root = tk.Tk()
root.title("Calculadora de Tiempo de Entrenamiento")

```
### Descargar la imagen desde la URL
- Descarga y redimensiona una imagen desde una URL para mostrarla en la interfaz de usuario.
```python
url = "https://assets-global.website-files.com/5e0fdda1c7ec61ff259e5d42/654afb738cb77a9e0cd7408b_cb-open.png"
response = requests.get(url)
image_data = response.content
image = Image.open(BytesIO(image_data))
image = image.resize((500, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

```
### Crear el marco para el formulario
- Crea un marco para contener los elementos del formulario en la interfaz de usuario.
```python
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

```
### Añadir la imagen al formulario
- Añade la imagen descargada al formulario.
```python
image_label = ttk.Label(frame, image=photo)
image_label.grid(row=0, columnspan=2, pady=10)

```
### Etiquetas y campos de entrada
```python
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

```
### Capturas del funcionamiento del código
- **En esta parte el código esta entrenando**
  
  ![image](https://github.com/user-attachments/assets/fe848b9f-165d-49e9-bba7-8470d2d42f8a)


- **Interfas de la IA**
  
  ![image](https://github.com/user-attachments/assets/caac3356-e852-45d4-ac8e-d8aee5fc87e1)

- **Se llenan los datos y arroja la prediccion**
  
  ![image](https://github.com/user-attachments/assets/34e73401-52bd-488e-a1af-2be42651fcf7)

- **Muestra el gráfico**
  
  ![image](https://github.com/user-attachments/assets/017a183f-03dc-4970-bbae-e4eb2a48d315)

  ![image](https://github.com/user-attachments/assets/1814f7cd-b3f2-4c39-8de3-0ba7493b40c5)

### Video Explicando el codigo y ejecutandolo

[GitHub Pages](https://www.youtube.com/watch?v=pPD3krd7ric).


### Conclusión
CBUM Training Time Prediction es una herramienta avanzada de inteligencia artificial diseñada para recomendar el tiempo de entrenamiento óptimo basado en la ingesta calórica diaria del usuario. Utilizando algoritmos de aprendizaje automático y una interfaz gráfica intuitiva, esta aplicación ofrece recomendaciones personalizadas que ayudan a los usuarios a alcanzar sus metas de fitness de manera más eficiente. Al integrar tecnologías como Tkinter, Pillow, Requests, NumPy, Pandas, TensorFlow y Matplotlib, la herramienta asegura un rendimiento robusto y una experiencia de usuario enriquecida. La facilidad de configuración y uso del sistema, junto con la capacidad de visualizar y ajustar las predicciones de entrenamiento, hacen de CBUM Training Time Prediction una valiosa adición al conjunto de herramientas de cualquier entusiasta del fitness.

