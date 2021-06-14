import os

all_files = []
carpeta = "E:\Vídeos\Grabaciones de Moodle\PDS"
i = 0
index = 0

a = os.listdir(carpeta)

for filename in a:
    os.rename(carpeta + '\\' + filename, carpeta + '\\' + filename[1:])
    print(filename)
