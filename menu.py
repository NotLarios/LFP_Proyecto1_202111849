from analize import * 

import tkinter as tk
from tkinter import filedialog

class textEditor:
    def __init__(self, window):
        self.window = window
        window.title("Proyecto 1 - Lenguajes Formales de Programación - Sergio Larios")

        #Cuadro de texto
        self.textbox = tk.Text(window, font="Arial,18")
        self.textbox.pack(fill="both", expand=True)

        #Agregar label donde estarán los menús desplegables
        menubar = tk.Menu(window)

        #Agregar filemenu
        filemenu = tk.Menu(menubar, tearoff=0, bg="light green", font="Arial, 12")

        #Agregar opciones al menú de Archivo
        filemenu.add_command(label="Abrir", command=self.open_file)
        filemenu.add_command(label="Guardar", command=self.save_file)
        filemenu.add_command(label="Guardar como...", command=self.save_as)
        filemenu.add_command(label="Analizar", command=self.analizar)
        filemenu.add_command(label="Errores")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=window.quit)

        #Agregar helpmenu
        helpmenu = tk.Menu(menubar, tearoff=0, bg="light green", font="Arial, 12")

        #Agregar opciones al menú de Ayuda	
        helpmenu.add_command(label="Manual de Usuario")
        helpmenu.add_command(label="Manual Técnico")
        helpmenu.add_command(label="Temas de Ayuda", command=self.temas_de_ayuda)

        #Se agregan los menús a un menú de cascada cada uno
        menubar.add_cascade(label="Archivo", menu=filemenu, font="Arial, 12")
        menubar.add_cascade(label="Ayuda", menu=helpmenu, font="Arial, 12")
        window.config(menu=menubar)

    #Método para abrir el archivo
    def open_file(self):
        try:
            self.filepath = filedialog.askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
            #Se verifica que se haya abierto un archivo y que no esté vacío
            if self.filepath is not None:
                self.file = open(self.filepath, "r")
                lineas = self.file.read()
                #Se elimina lo que se encuentre en el cuadro de texto
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, lineas)
        except Exception as e:
            print("Seleccione un archivo válido " + str(e))

    def save_file(self):
        try:
            if self.filepath is not None:
            #Se verifica que el archivo no esté vacío
                file = open(self.filepath, "w")
                #Obtiene todos los caracteres del cuadro de texto
                lineas = self.textbox.get(1.0, tk.END)
                file.write(lineas)
                file.close()
        except Exception as e:
            print(e)
            self.save_as()
    
    def save_as(self):
        file = filedialog.asksaveasfile(title = "Guardar archivo como...", filetypes=[("Archivos de texto", "*.txt")], defaultextension=".txt")
        #Se verifica que el archivo no esté vacío
        if file is not None:
            self.saved_file = file.name
            lineas = self.textbox.get(1.0, tk.END)
            file.write(lineas)
            file.close()

    def analizar(self):
        file = open(self.filepath, "r")
        lineas = file.read()

        instruccion(lineas)
        respuestas = evaluate_()
        for respuesta in respuestas:
            print(respuesta.evaluate(None))

    def temas_de_ayuda(self):
        ventana_ayuda = tk.Toplevel(self.window)
        ventana_ayuda.title("Temas de ayuda")
        ventana_ayuda.resizable(False, False)

        #Cuadro de texto
        label1 = tk.Label(ventana_ayuda, text="Temas de ayuda", font=('Arial', 12, 'bold'), padx=8, pady=8)
        label2 = tk.Label(ventana_ayuda, text="Sergio Andrés Larios Fajardo", font="Arial, 12", padx=5, pady=5)
        label3 = tk.Label(ventana_ayuda, text="202111849", font="Arial, 12", padx=5, pady=5)
        label4 = tk.Label(ventana_ayuda, text="Lenguajes Formales de Programación", font="Arial, 12", padx=5, pady=5)
        label5 = tk.Label(ventana_ayuda, text="Sección B-", font="Arial, 12", padx=5, pady=5)
        label6 = tk.Label(ventana_ayuda, text="Facultad de Ingeniería", font="Arial, 12", padx=5, pady=5)
        label7 = tk.Label(ventana_ayuda, text="Universidad de San Carlos de Guatemala", font="Arial, 12", padx=15, pady=5)
        label8 = tk.Label(ventana_ayuda, text="Ingeniería en Ciencias y Sistemas", font="Arial, 12", padx=5, pady=5)
        label9 = tk.Label(ventana_ayuda, text=" ", font="Arial, 5", padx=5, pady=5)
        
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()
        label9.pack()
        

root = tk.Tk()
root.geometry("800x600")
editor = textEditor(root)
root.mainloop()