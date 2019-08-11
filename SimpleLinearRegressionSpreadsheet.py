import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from openpyxl import load_workbook

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

############### PROGRAMA ###############
# Base de datos
doc = load_workbook('Dataset.xlsx')
sheets = doc.sheetnames
hoja = doc[sheets[0]]
filas = hoja.max_row+1

# Obtener datos de x - Valor NDVIO, y - Valor Clorofila Espectrometro
x = []
yspec = []
for i in range(3,filas):
    spec = float(hoja[i][0].value)
    ndvi = float(hoja[i][10].value)
    if ndvi > 0.1:
        x.append([ndvi])
        yspec.append(spec)

################ CLOROFILA LABORATORIO ################
print("\nNDVI:\n", x)
print("\nSPEC:\n", yspec)

# Gráfica de los datos
plt.scatter(x, yspec)
plt.title('Clorofila Espectrometro')
plt.xlabel('Valor NDVI')
plt.ylabel('Valor Clorofila Espectrometro')
plt.show()

# Entrena con el 75% y predice con el 25% restante
lrs, xTrain, yTrain, xTest, yTest, yPred = train(x, yspec, 1, 0.2)

print('\nPREDICCIÓN CLOROFILA ESPECTROMETRO')
print('\nDatos de NDVI:\n', xTest)
print('\nDatos de Valor de Clorofila Espectrometro reales:\n', yTest)
print('\nDatos de Valor de Clorofila Espectrometro predichos:\n', yPred)

# Gráfica de los datos con la regresión lineal simple
plt.scatter(xTest, yTest)
plt.plot(xTest, yPred, color='red')
plt.title('Clorofila Espectrometro - Regresión Lineal Simple')
plt.xlabel('Valor NDVI')
plt.ylabel('Valor Clorofila Espectrometro')
plt.show()

print('\nPendiente (a): ', lrs.coef_)
print('Intersección (b): ', lrs.intercept_)
print('Ecuación (y = ax + b): ', 'y = ', lrs.coef_, 'x ', lrs.intercept_)
print('Precisión del modelo: ', lrs.score(xTrain, yTrain))