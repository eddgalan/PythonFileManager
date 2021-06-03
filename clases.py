from pathlib import Path
from os import remove, mkdir, rename
from shutil import rmtree, move

class FileManager(object):
    """ Clase para Manipular Archivos """

    def __init__(self):
        pass

    # Función para crear un archivo
    def create_file(self, filename):
        try:
            f = open(filename, "x")
            return True
        except:
            return False

    # Función para eliminar un archivo
    def delete_file(self, filename):
        fileObj = Path(filename)
        # Verifica que el archivo exista
        if( fileObj.is_file() ):
            remove(fileObj)
            # Verifica que el archivo ya NO exista
            if( fileObj.is_file() ):
                return False
            else:
                return True
        else:
            return False

    # Función para crear un directorio (Carpeta)
    def create_directory(self, dir_name):
        try:
            mkdir(dir_name)
            return True
        except:
            return False

    # Función para eliminar un directorio (Carpeta)
    def delete_directory(self, dir_name):
        fileObj = Path(dir_name)
        try:
            # Verifica que el directorio exista
            if( fileObj.is_dir() ):
                rmtree(dir_name)
                # Verifica que el directorio ya NO exista
                if( fileObj.is_dir() ):
                    return False
                else:
                    return True
            else:
                return False
        except:
            return False

    # Función para renombrar un archivo
    def rename_file(self, filename, new_name):
        try:
            rename(filename, new_name)
            return True
        except:
            return False

    # Función para mover archivos/carpetas
    def move(self, path, new_path):
        try:
            move(path, new_path)
            return True
        except:
            return False
    
