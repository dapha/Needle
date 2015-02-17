# David Phan
# Zip Reader

import zipfile
import math

def byteConvert(size):
    size_name = ("KB", "MB", "GB", "TB") # Suffix
    if (size < 1024): # For files < 1KB
        return '%sB' % (size)
    i = int(math.floor(math.log(size,1024))) # Calculate order of byte
    p = math.pow(1024,i)
    s = round(size/p,1)
    if (s > 0):
        return '%s%s' % (s, size_name[i])
    else:
        return '0B'
    

def zip_reader(archive_name):
    zFile = zipfile.ZipFile(archive_name) # Read zip file
    for info in zFile.infolist():
        fSize = byteConvert(info.file_size) # Convert byte to correct order
        print(info.filename, '\t', fSize) # Print filename and file size
        
        
        
        

