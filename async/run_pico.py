import os

if  os.name == 'nt' :
    os.system("C:/Python27/python.exe -m pico.server")
else:
    raise "Not supported os"
