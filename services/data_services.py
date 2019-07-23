from data.labels import Label

'''
    En este archivo se definen las funciones para ingresar documentos
    en la base de datos
'''

def create_ndvi(filename, spad: float, lab: float):
    pixels = [1,2]
    file_info = filename.split(".")
    label = Label()
    label.name = file_info[0]
    label.extension = file_info[1]
    label.NDVI = pixels
    label.SPAD = spad
    label.LAB = lab
    
    label.save()

def getAllLAB():
    return Label.objects().filter().values_list('LAB')

def getAllNDVI():
    return Label.objects().filter().values_list('NDVI')

def getAllSPAD():
    return Label.objects().filter().values_list('SPAD')