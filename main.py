import os
import re

all_files = []
carpeta = "E:\Vídeos\Grabaciones de Moodle\PDS"
i = 0
index = 0

a = os.listdir(carpeta)

for month in range(1, 12):
    regex = re.compile('.*_0'+str(month)+'_.*')
    for file in a:
        if regex.match(file):
            if (i < 9):
                all_files.append('0' + str(i + 1) + '. ' + file)
            else:
                all_files.append(str(i + 1) + '. ' + file)
            i += 1

for file in a:
    index = 0

    regex = re.compile('.*' + file + '.*')

    for n in all_files:
        if regex.match(all_files[index]):
            break
        index += 1

    if index < 9:
        os.rename(carpeta + '\\' + file, carpeta + '\\' + all_files[index])
        # print(all_files[index])
    else:
        os.rename(carpeta + '\\' + file, carpeta + '\\' + all_files[index])
        # print(all_files[index])

    index += 1
