from PIL import Image

import os

downloads_folder = "/Users/Gustavo Santos/Downloads/"  #Cambia la dirrecion de la carpeta por tu direccion de descargas
folder_pictures = "/Users/Gustavo Santos/Pictures/"    #Cambia la dirrecion de la carpeta por tu direccion de imagines

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(downloads_folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloads_folder + filename)
            picture.save(folder_pictures + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloads_folder + filename)