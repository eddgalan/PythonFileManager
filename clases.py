from pathlib import Path
from os import remove

class FileManager(object):
    """ Clase para Manipular Archivos """

    def __init__(self):
        pass

    # Función para crear un directorio
    def create_dir(path, dirname):
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
