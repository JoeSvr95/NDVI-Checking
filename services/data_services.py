from data.labels import Label

'''
    En este archivo se definen las funciones para ingresar documentos
    en la base de datos
'''

def create_ndvi(filename, spad: float, lab: float, pixels):
    file_info = filename.split(".")
    label = Label()
    label.name = file_info[0]
    label.extension = file_info[1]
    label.NDVI = pixels
    label.SPAD = spad
    label.LAB = lab
    
    label.save()

def getAllLAB():
    return list(Label.objects().all().values_list('LAB'))

def getAllNDVI():
    return list(Label.objects().all().values_list('NDVI'))

def getAllSPAD():
    return list(Label.objects().all().values_list('SPAD'))

def getNDVIbyFile(fileName):
    label = Label.objects.get(name=fileName) 
    return label.NDVI