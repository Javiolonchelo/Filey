import os
import stat
import time

all_files = []
carpeta = "E:\Vídeos\Grabaciones de Moodle\PDS"
i = 0
index = 0

a = os.listdir(carpeta)

for filename in a:
    # os.rename(carpeta + '\\' + filename, carpeta + '\\' + filename[1:])
    # print(filename)
    stats = os.stat(carpeta + '\\' + filename)
    os.rename(carpeta + '\\' + filename, carpeta + '\\' + time.strftime("%d_%m_%Y", time.localtime(
        stats[stat.ST_MTIME])) + ' - PDS - ' + time.strftime("%H_%M_%S", time.localtime(stats[stat.ST_MTIME])) + ".mp4")
