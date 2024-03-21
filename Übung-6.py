import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

# 1.1 Daten aus CSV laden
path = "/Users/student/PycharmProjects/Clustering_PG2/winequality-red.csv"
data = pd.read_csv(path, delimiter=";")

# 1.2 die ersten und letzten 5 Zeilen ausgeben
print('#'*100)
print('Aufgabe 1.2')

print(data.head())
print(data.tail())

# 1.3 Anzahl Zeilen und Spalten + Datentyp
print('#'*100)
print('Aufgabe 1.3')

print(data.info())

# 2.1 Überprüfen Sie den Datensatz auf fehlende Werte und behandeln Sie diese entsprechend (z.B. durch Entfernen oder Ersetzen).
print('#'*100)
print('Aufgabe 2.1')

print(data.isnull().any())

# 2.2 Duplikate entfernen
print('#'*100)
print('Aufgabe 2.2')

print(data.duplicated())
data = data.drop_duplicates()
print(data.duplicated())

# 3.1 statistische Kennzahlen
print('#'*100)
print('Aufgabe 3.1')

descriptive_statistic = data.describe()
print(descriptive_statistic)

# 3.2 Ermitteln Sie die Korrelation zwischen der Qualität des Weins und anderen chemischen Eigenschaften.
print('#'*100)
print('Aufgabe 3.2')

correlation = data.corr()
print(correlation['quality'].sort_values())

# 4.1 Histogramm
print('#'*100)
print('Aufgabe 4.1')
print('Histogramm')

data['alcohol'].hist()
plt.title('Verteilung des Alkoholgehalts')
plt.show()

# 4.2 ScatterPlot
print('#'*100)
print('Aufgabe 4.2')
print('ScatterPlot')

plt.scatter(data['alcohol'], data['quality'])
plt.title('Alkoholgehalt vs. Qualität des Weins')
plt.show()

# 4.3 BoxPlot
print('#'*100)
print('Aufgabe 4.3')
print('BoxPlot')

data.boxplot(column='alcohol', by='quality')
plt.title('Alkoholgehalt nach Weinqualität')
plt.show()
