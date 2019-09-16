import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import data.mongo_setup as mongo_setup
import services.data_services as svc

#Función para entrenar
def train(x, y, booleanTrainTotal, testPercent):
    # x es NDVI, y es Clorofila
    # booleanTrainTotal indica si se usa todos los datos para entrenar, testPercent indica porcentaje de datos para predecir
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=testPercent)
    
    if (booleanTrainTotal):
        xTrain = x
        yTrain = y

    if (testPercent == 1):
        xTest = x
        yTest = y

    # Definir regresión lineal simple y entrenar modelo
    lrs = linear_model.LinearRegression()
    lrs.fit(xTrain, yTrain)

    # Realizar predicción con datos de prueba
    yPred = lrs.predict(xTest)

    return lrs, xTrain, yTrain, xTest, yTest, yPred

# base = datasets.load_diabetes() # DE PRUEBA
# x = base.data[:, np.newaxis, 5] # DE PRUEBA
# ylab = base.target #DE PRUEBA
# yspad = base.target #DE PRUEBA


############### PROGRAMA ###############
# Base de datos
mongo_setup.global_init()

# Obtener datos de x - Valor NDVI
tempx = svc.getAllNDVI()

# Obtener datos de y - Valor Clorofila Laboratorio y SPAD
templab = svc.getAllLAB()
tempspad = svc.getAllSPAD()

x = []
ylab = []
yspad = []
for i in tempx:
    for j in i:
        if j > 0.1:
            x.append([j])
            ylab.append(templab[tempx.index(i)])
            yspad.append(tempspad[tempx.index(i)])

################ CLOROFILA LABORATORIO ################
#print("\nNDVI:\n", x)
#print("\nLAB:\n", ylab)

# Gráfica de los datos
#plt.scatter(x, ylab)
#plt.title('Clorofila Laboratorio')
#plt.xlabel('Valor NDVI')
#plt.ylabel('Valor Clorofila Laboratorio')
#plt.show()

# Entrena con el 75% y predice con el 25% restante
#lrs, xTrain, yTrain, xTest, yTest, yPred = train(x, ylab, 1, 0.25)

#print('\nPREDICCIÓN CLOROFILA LABORATORIO')
#print('\nDatos de NDVI:\n', xTest)
#print('\nDatos de Valor de Clorofila Laboratorio reales:\n', yTest)
#print('\nDatos de Valor de Clorofila Laboratorio predichos:\n', yPred)

# Gráfica de los datos con la regresión lineal simple
#plt.scatter(xTest, yTest)
#plt.plot(xTest, yPred, color='red')
#plt.xlabel('Valor NDVI')
#plt.title('Clorofila Laboratorio - Regresión Lineal Simple')
#plt.ylabel('Valor Clorofila Laboratorio')
#plt.show()

#print('\nPendiente (a): ', lrs.coef_)
#print('Intersección (b): ', lrs.intercept_)
#print('Ecuación (y = ax + b): ', 'y = ', lrs.coef_, 'x ', lrs.intercept_)
#print('Precisión del modelo: ', lrs.score(xTrain, yTrain))


################ CLOROFILA SPAD ################
#print("\nNDVI:\n", x)
#print("\nSPAD:\n", yspad)

# Gráfica de los datos
#plt.scatter(x, yspad)
#plt.title('Clorofila SPAD')
#plt.xlabel('Valor NDVI')
#plt.ylabel('Valor Clorofila SPAD')
#plt.show()

# Entrena con el 75% y predice con el 25% restante
lrs, xTrain, yTrain, xTest, yTest, yPred = train(x, yspad, 1, 0.25)

print('\nPREDICCIÓN CLOROFILA SPAD')
print('\nDatos de NDVI:\n', xTest)
print('\nDatos de Valor de Clorofila SPAD reales:\n', yTest)
print('\nDatos de Valor de Clorofila SPAD predichos:\n', yPred)

# Gráfica de los datos con la regresión lineal simple
#plt.scatter(xTest, yTest)
#plt.plot(xTest, yPred, color='red')
#plt.title('Clorofila SPAD - Regresión Lineal Simple')
#plt.xlabel('Valor NDVI')
#plt.ylabel('Valor Clorofila SPAD')
#plt.show()

print('\nPendiente (a): ', lrs.coef_)
print('Intersección (b): ', lrs.intercept_)
print('Ecuación (y = ax + b): ', 'y = ', lrs.coef_, 'x', lrs.intercept_)
print('Precisión del modelo: ', lrs.score(xTrain, yTrain))