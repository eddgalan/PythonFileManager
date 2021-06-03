import tkinter as tk
from tkinter import messagebox
from clases import FileManager

#Clase Primaria (Padre)
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        # Botón Crear Archivo
        self.button_create = tk.Button(self.frame, text = 'Crear Archivo', width = 25, command = self.show_create_file).pack()
        # Botón Eliminar Archivo
        self.button_delete = tk.Button(self.frame, text = 'Eliminar Archivo', width = 25, command = self.show_delete_file).pack()


        self.frame.pack()
    # Abre ventana para crear nuevo archivo
    def show_create_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowCreateFile(self.newWindow)

    # Abre ventana para eliminar un archivo
    def show_delete_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowDeleteFile(self.newWindow)

# Clase Derivada (Hijo) de 'MainWindow' | Crea el archivo
class WindowCreateFile(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.filename = tk.StringVar()      # Guarda el nombre del archivo

        # Nombre del Nuevo Archivo
        self.label = tk.Label(self.frame, text = "Nombre del archivo: ")
        self.label.pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.filename)
        self.file_name.pack()
        # self.file_name.place(x=50, y=50)

        # Botón Crear Archivo
        self.acceptButton = tk.Button(self.frame, text = 'Crear archivo', width = 25, command = self.create_file).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Crear Archivo")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.frame.pack()

    def create_file(self):
        file_name = self.filename.get()
        manager = FileManager()
        if ( manager.create_file(file_name) ):
            tk.messagebox.showinfo(message="Se creo el archivo "+ file_name +" correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al crear el archivo", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Crea un directorio(Carpeta)
class WindowCreateDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.filename = tk.StringVar()      # Guarda el nombre del archivo

        # Nombre del Nuevo Archivo
        self.label = tk.Label(self.frame, text = "Nombre del archivo: ")
        self.label.pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.filename)
        self.file_name.pack()
        # self.file_name.place(x=50, y=50)

        # Botón Crear Archivo
        self.acceptButton = tk.Button(self.frame, text = 'Crear archivo', width = 25, command = self.create_file).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Crear Archivo")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.frame.pack()

    def create_file(self):
        file_name = self.filename.get()
        manager = FileManager()
        if ( manager.create_file(file_name) ):
            tk.messagebox.showinfo(message="Se creo el archivo "+ file_name +" correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al crear el archivo", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Borra el archivo
class WindowDeleteFile(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.filename = tk.StringVar()      # Guarda el nombre del archivo

        # Nombre del archivo a borrar
        self.label = tk.Label(self.frame, text = "Nombre del archivo a eliminar: ")
        self.label.pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.filename)
        self.file_name.pack()
        # self.file_name.place(x=50, y=50)

        # Botón Crear Archivo
        self.acceptButton = tk.Button(self.frame, text = 'Borrar archivo', width = 25, command = self.delete_file).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Eliminar Archivo")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.frame.pack()

    def delete_file(self):
        file_name = self.filename.get()
        manager = FileManager()
        if ( manager.delete_file(file_name) ):
            tk.messagebox.showinfo(message="Se eliminó el archivo '"+ file_name +"' correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un error al eliminar el archivo o el archivo no existe", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("600x350")
    root.resizable(False, False)
    root.title("ESIME CULHUACAN | Python File Manager")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
