import os

carpeta = "E:\Vídeos\Grabaciones de Moodle\PDS"
a = os.listdir(carpeta)

for filename in a:
    os.rename(carpeta + '\\' + filename, carpeta +
              '\\' + filename.replace('Parte ', 'P'))
    # print(carpeta + '\\' + filename.replace('Parte ', 'P'))
