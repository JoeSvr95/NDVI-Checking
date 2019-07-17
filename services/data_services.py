from data.labels import Label

'''
    En este archivo se definen las funciones para ingresar documentos
    en la base de datos
'''

def create_ndvi(filename, spad: float, lab: float):
    file_info = filename.split(".")
    label = Label()
    label.name = file_info[0]
    label.extension = file_info[1]
    label.NDVI = 1.0
    label.SPAD = spad
    label.LAB = lab
    
    label.save()