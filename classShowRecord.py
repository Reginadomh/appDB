import tkinter as tk

class ShowRecord:

    def __init__(self):
        self.__textoRegistro = None

        # Configuración de la interfaz gráfica
        self.app = tk.Tk()
        self.app.title("Último Registro Estudiante")
        self.app.geometry("300x200")

        # Label para mostrar los resultados
        self.resultado_label = tk.Label(self.app, text="", justify="left")
        self.resultado_label.pack(pady=10)

        # Botón para obtener el último registro
        self.boton = tk.Button(self.app, text="Obtener Último Registro", command=self.obtener_ultimo_registro)
        self.boton.pack(pady=10)

        # Iniciar la aplicación
        self.app.mainloop()

    # Función para mostrar los datos en la interfaz gráfica
    def mostrar_datos(self, registro):
        self.__textoRegistro = registro
        self.resultado_label.config(text=self.__textoRegistro)

    # Aquí iría la función que obtiene el registro de la API
    def obtener_ultimo_registro(self):
        # Este es un ejemplo, debes reemplazarlo con la llamada real a la API
        ultimo_registro = "ID: 1\nNombre: John\nApellido: Doe\nCiudad: Nueva York\nCalle: 123"
        self.mostrar_datos(ultimo_registro)


# Crear instancia de la clase para ejecutar la aplicación
app = ShowRecord()
