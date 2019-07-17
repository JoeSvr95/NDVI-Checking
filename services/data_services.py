from data.labels import Label

def create_ndvi(spad: float, lab: float):
    label = Label()
    label.name = 'imagen'
    label.extension = 'jpg'
    label.NDVI = 1.0
    label.SPAD = spad
    label.LAB = lab
    
    label.save()