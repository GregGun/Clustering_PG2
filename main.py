import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#Aufgabe 1
path = "/Users/student/PycharmProjects/Clustering_PG2/iris.csv"
data = pd.read_csv(path, delimiter=',')
print(data.head())

#Aufgabe 3
#x = [data['sepal.length']]
#y = [data['sepal.width']]


#Aufgabe 4 (siehe auch OneNote'Clustering')

setosa = data[data['species'] == 'Setosa']
versicolor = data[data['species'] == 'Versicolor']
virginica = data[data['species'] == 'Virginica']

#mögliche Lösung
'''
x = [setosa['sepal.length'], versicolor['sepal.length'], virginica['sepal.length']]
y = [setosa['sepal.width'], versicolor['sepal.width'], virginica['sepal.width']]

plt.scatter(x, y)
plt.show()
'''

#Lehrer-Lösung
plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color='red', marker='s')
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color='blue', marker='o')
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color='green', marker='^')

plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()
