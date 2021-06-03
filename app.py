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
        # Botón Renombrar Archivo
        self.button_delete = tk.Button(self.frame, text = 'Renombrar Archivo', width = 25, command = self.show_rename_file).pack()
        # Botón Crear Directorio
        self.button_delete = tk.Button(self.frame, text = 'Crear Carpeta', width = 25, command = self.show_create_directory).pack()
        # Botón Eliminar Directorio
        self.button_delete = tk.Button(self.frame, text = 'Eliminar Carpeta', width = 25, command = self.show_delete_directory).pack()


        self.frame.pack()
    # Abre ventana para crear nuevo archivo
    def show_create_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowCreateFile(self.newWindow)
    # Abre ventana para eliminar un archivo
    def show_delete_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowDeleteFile(self.newWindow)
    # Abre ventana para crear nuevo archivo
    def show_rename_file(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowRenameFile(self.newWindow)
    # Abre ventana para crear una carpeta
    def show_create_directory(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowCreateDirectory(self.newWindow)
    # Abre ventana para eliminar una carpeta
    def show_delete_directory(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowDeleteDirectory(self.newWindow)

# Clase Derivada (Hijo) de 'MainWindow' | Crea el archivo
class WindowCreateFile(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.filename = tk.StringVar()      # Guarda el nombre del archivo

        # Nombre del Nuevo Archivo
        self.label = tk.Label(self.frame, text = "Nombre del archivo: ").pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.filename).pack()
        # self.file_name.place(x=50, y=50) | Usar esto es una alternativa a .pack()

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

# Clase Derivada (Hijo) de 'MainWindow' | Crea un directorio(Carpeta)
class WindowCreateDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.dirname = tk.StringVar()      # Guarda el nombre de la Carpeta
        # Nombre de la Carpeta que se va a crear
        self.label = tk.Label(self.frame, text = "Nombre carpeta: ").pack()
        self.dir_name = tk.Entry(self.frame, textvariable=self.dirname).pack()

        # Botón Crear Directorio (Carpeta)
        self.acceptButton = tk.Button(self.frame, text = 'Crear carpeta', width = 25, command = self.create_directory).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Crear Carpeta")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.frame.pack()

    def create_directory(self):
        directory_name = self.dirname.get()
        manager = FileManager()
        if ( manager.create_directory(directory_name) ):
            tk.messagebox.showinfo(message="Se creo la carpeta '"+ directory_name +"' correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al crear la carpeta", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Elimina un directorio(Carpeta)
class WindowDeleteDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.dirname = tk.StringVar()      # Guarda el nombre de la Carpeta
        # Nombre de la Carpeta que se va a crear
        self.label = tk.Label(self.frame, text = "Nombre carpeta: ").pack()
        self.dir_name = tk.Entry(self.frame, textvariable=self.dirname).pack()

        # Botón Eliminar Directorio (Carpeta)
        self.acceptButton = tk.Button(self.frame, text = 'Eliminar carpeta', width = 25, command = self.delete_directory).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Eliminar Carpeta")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.frame.pack()

    def delete_directory(self):
        directory_name = self.dirname.get()
        # Muestra un mensaje de confirmación para eliminar el directorio
        confirm = messagebox.askyesno(message="Se eliminará la carpeta '"+ directory_name +"' y todo su contenido. "+
        "¿Seguro que desea continuar?", title="Eliminar Directorio")
        if( confirm ):
            manager = FileManager()
            if ( manager.delete_directory(directory_name) ):
                tk.messagebox.showinfo(message="Se eliminó la carpeta '"+ directory_name +"' correctamente", title="Python File Manager")
            else:
                tk.messagebox.showerror(message="Ocurrió un problema al eliminar la carpeta", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Renombra el archivo
class WindowRenameFile(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.filename = tk.StringVar()
        self.filerename = tk.StringVar()

        # Nombre del Archivo que quiere renombrar
        self.label = tk.Label(self.frame, text = "Nombre del archivo que desea renombrar: ").pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.filename).pack()
        # Nombre Nuevo del Archivo
        self.label = tk.Label(self.frame, text = "Nuevo nombre del archivo: ").pack()
        self.file_rename = tk.Entry(self.frame, textvariable=self.filerename).pack()

        # Botón Crear Archivo
        self.acceptButton = tk.Button(self.frame, text = 'Renombrar archivo', width = 25, command = self.rename_file_).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Renombrar Archivo")
        self.master.geometry("300x135")
        self.master.resizable(False, False)
        self.frame.pack()

    def rename_file_(self):
        file_name = self.filename.get()
        file_rename = self.filerename.get()
        manager = FileManager()
        if ( manager.rename_file(file_name, file_rename) ):
            tk.messagebox.showinfo(message="Se renombró el archivo correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al renombrar el archivo", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("600x350")
    root.resizable(False, False)
    root.title("ESIME CULHUACAN ♥ | Python File Manager")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
