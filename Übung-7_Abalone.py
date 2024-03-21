import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

# 1.1 Daten aus CSV laden
path = "/Users/student/PycharmProjects/Clustering_PG2/abalone.data"
data = pd.read_csv(path, delimiter=",", header=None)

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

# Werte der Tabelle in nummerische Werte umwandeln
data_unknown = data
data_unknown = data_unknown.astype("category")
data_unknown = data_unknown.apply(lambda x: x.cat.codes)

# KElbow verwenden, um Anzahl der Gruppen zu erhalten
model = KMeans()
visualizer = KElbowVisualizer(model, K=(2, 9), timings=False)
visualizer.fit(data_unknown)
visualizer.show()

# Anzahl Gruppen eintragen
KMeans = KMeans(n_clusters=4)

# Tabelle mit neuer Spalte 'Label' (Gruppennummer) in neue CSV speichern
pred = KMeans.fit_predict(data_unknown)
data_new = pd.concat([data, pd.DataFrame(pred, columns=["label"])], axis=1)
print(data_new)
data_new.to_csv("./data_new_abalone.data")
