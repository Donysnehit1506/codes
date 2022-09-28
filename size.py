import os.path
def convert_bytes(size):
    """ Convert bytes to KB, or MB or GB"""
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

filesize = os.path.getsize(r"C:\Users\donys\Downloads\CorelDRAWGraphicsSuiteInstaller_en.zip")
x = convert_bytes(filesize)
print('file size is', x)