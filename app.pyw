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
        self.button_rename = tk.Button(self.frame, text = 'Renombrar Archivo', width = 25, command = self.show_rename_file).pack()
        # Botón Crear Directorio
        self.button_create_dir = tk.Button(self.frame, text = 'Crear Carpeta', width = 25, command = self.show_create_directory).pack()
        # Botón Eliminar Directorio
        self.button_delete_dir = tk.Button(self.frame, text = 'Eliminar Carpeta', width = 25, command = self.show_delete_directory).pack()
        # Botón Renombrar Carpeta
        self.button_rename_dir = tk.Button(self.frame, text = 'Renombrar Carpeta', width = 25, command = self.show_rename_directory).pack()
        # Botón Mover Archivo/Carpeta
        self.button_move = tk.Button(self.frame, text = 'Mover Archivo/Carpeta', width = 25, command = self.show_move).pack()
        # Botón Mostrar Directorio
        self.button_show_dir = tk.Button(self.frame, text = 'Listar contenido', width = 25, command = self.show_list_directory).pack()


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
    # Abre ventana para renombrar una carpeta
    def show_rename_directory(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowRenameDirectory(self.newWindow)
    # Abre ventana para mover un archivo o carpeta
    def show_move(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowMoveDirectory(self.newWindow)
    # Abre ventana para indicar qué directorio se desea consultar
    def show_list_directory(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowSelectDirectory(self.newWindow)

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
        self.master.iconbitmap('icon.ico')
        self.frame.pack()

    def create_file(self):
        file_name = self.filename.get()
        manager = FileManager()
        if ( manager.create_file(file_name) ):
            tk.messagebox.showinfo(message="Se creo el archivo '"+ file_name +"' correctamente", title="Python File Manager")
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
        self.master.iconbitmap('icon.ico')
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
        self.master.iconbitmap('icon.ico')
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
        self.master.iconbitmap('icon.ico')
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
        self.master.iconbitmap('icon.ico')
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

# Clase Derivada (Hijo) de 'MainWindow' | Renombra el directorio
class WindowRenameDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.directoryname = tk.StringVar()
        self.directoryrename = tk.StringVar()

        # Nombre del Archivo que quiere renombrar
        self.label = tk.Label(self.frame, text = "Nombre y ruta de la carpeta: ").pack()
        self.file_name = tk.Entry(self.frame, textvariable=self.directoryname).pack()
        # Nombre Nuevo del Archivo
        self.label = tk.Label(self.frame, text = "Nuevo nombre de la carpeta: ").pack()
        self.file_rename = tk.Entry(self.frame, textvariable=self.directoryrename).pack()

        # Botón Crear Archivo
        self.acceptButton = tk.Button(self.frame, text = 'Renombrar carpeta', width = 25, command = self.rename_directory).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Renombrar Carpeta")
        self.master.geometry("300x135")
        self.master.resizable(False, False)
        self.master.iconbitmap('icon.ico')
        self.frame.pack()

    def rename_directory(self):
        directory_name = self.directoryname.get()
        directory_rename = self.directoryrename.get()
        manager = FileManager()
        if ( manager.rename_file(directory_name, directory_rename) ):
            tk.messagebox.showinfo(message="Se renombró la carpeta correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al renombrar la carpeta", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Mueve Archivo o Carpetas
class WindowMoveDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.path = tk.StringVar()
        self.new_path = tk.StringVar()

        # Nombre del Archivo/Carpeta que desea remover
        self.label = tk.Label(self.frame, text = "Nombre y ruta del archivo o carpeta: ").pack()
        self.path_origen = tk.Entry(self.frame, textvariable=self.path).pack()
        # Nueva ruta del Archivo/Carpeta
        self.label = tk.Label(self.frame, text = "Carpeta destino: ").pack()
        self.path_destino = tk.Entry(self.frame, textvariable=self.new_path).pack()

        # Botón Mover
        self.acceptButton = tk.Button(self.frame, text = 'Mover archivo/carpeta', width = 25, command = self.move).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Renombrar Carpeta")
        self.master.geometry("300x135")
        self.master.resizable(False, False)
        self.master.iconbitmap('icon.ico')
        self.frame.pack()

    def move(self):
        path = self.path.get()
        new_path = self.new_path.get()
        manager = FileManager()
        if ( manager.move(path, new_path) ):
            tk.messagebox.showinfo(message="Se movió el archivo/carpeta a la ruta '"+ new_path +"' correctamente", title="Python File Manager")
        else:
            tk.messagebox.showerror(message="Ocurrió un problema al mover el archivo/carpeta", title="¡Error!")
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Muestra el Formulario para indicar el directorio
class WindowSelectDirectory(MainWindow):
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.directoryname = tk.StringVar()

        # Nombre del directorio que se quiere Mostrar
        self.label = tk.Label(self.frame, text = "Directorio: ").pack()
        self.directory_name = tk.Entry(self.frame, textvariable=self.directoryname).pack()

        # Botón Mostrar Directorio
        self.acceptButton = tk.Button(self.frame, text = 'Mostrar contenido', width = 25, command = self.show_select_dir).pack()
        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cancelar', width = 25, command = self.close_windows).pack()

        self.master.title("Mostrar contenido")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.master.iconbitmap('icon.ico')
        self.frame.pack()

    def show_select_dir(self):
        directoryname = self.directoryname.get()
        self.newWindow = tk.Toplevel(self.master)
        self.app = WindowListDirectory(self.newWindow, directoryname)

    def close_windows(self):
        self.master.destroy()

# Clase Derivada (Hijo) de 'MainWindow' | Muestra la ventana con los archivos/carpetas
class WindowListDirectory(MainWindow):
    def __init__(self, master, directoryname):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.directoryname = tk.StringVar()

        manager = FileManager()
        content = manager.get_content(directoryname)          #Obtiene el contenido de la carpeta

        if(content):
            # print(content)
            directories = []
            files = []
            hidden_files = []
            for item in content:
                # Verifica si es un archivo oculto
                if( item.find(".")==0 ):
                    hidden_files.append(item)
                elif( item.find(".")== -1 ):
                    # Verifica si es un directorio
                    if( manager.directory_exist(directoryname +"./"+ item) ):
                        directories.append(item)
                # Si NO es un archivo oculto o directorio entonces es un archivo
                else:
                    files.append(item)
            # Muestra un label con un mensaje
            msg = "Mostrando el contenido del directorio '"+ directoryname +"'"
            tk.Label(self.frame, text = msg).pack()

            # Muestra las carpetas
            if( directories ):
                tk.Label(self.frame, text = "Carpetas: ", fg="green").pack()
                for directory in directories:
                    tk.Label(self.frame, text = directory).pack()
            # Muestra los archivos
            if( files ):
                tk.Label(self.frame, text = "Archivos: ", fg="green").pack()
                for directory in files:
                    tk.Label(self.frame, text = directory).pack()
            # Muestra los archivos ocultos
            if( hidden_files ):
                tk.Label(self.frame, text = "Archivos ocultos: " ,fg="green").pack()
                for directory in hidden_files:
                    tk.Label(self.frame, text = directory).pack()
        else:
            tk.messagebox.showerror(message="Ocurrió un error al listar el contenido del directorio '"+ directoryname +
             "' o el directorio se encuentra vacío verifique que el directorio exista", title="¡Error!")

        # Botón Cancelar
        self.quitButton = tk.Button(self.frame, text = 'Cerrar', width = 25, command = self.close_windows).pack()

        self.master.title("Mostrando contenido de la carpeta")
        self.master.geometry("500x350")
        self.master.resizable(False, False)
        self.master.iconbitmap('icon.ico')
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    root.geometry("600x350")
    root.resizable(False, False)
    root.title("ESIME CULHUACAN ♥ | Python File Manager")
    root.iconbitmap('icon.ico')
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
