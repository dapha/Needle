# David Phan
# Zip Reader

import zipfile
import math

def byteConvert(size):
    size_name = ("KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size,1024)))
    p = math.pow(1024,i)
    s = round(size/p,1)
    if (s > 0):
        return '%s%s' % (s, size_name[i])
    else:
        return '0B'
    

def print_info(archive_name):
    zFile = zipfile.ZipFile(archive_name)
    for info in zFile.infolist():
        fSize = byteConvert(info.file_size)
        print(info.filename, '\t', fSize)
        
        
        
        

