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

1. Datensatz laden und erkunden
• Laden Sie den 'Wine Quality'-Datensatz in einen DataFrame.
• Geben Sie die ersten und letzten 5 Zeilen des DataFrames aus.
• Überprüfen Sie die Anzahl der Zeilen und Spalten sowie die Datentypen der Spalten.

2. Datenbereinigung
• Überprüfen Sie den Datensatz auf fehlende Werte und behandeln Sie diese entsprechend (z.B. durch Entfernen oder Ersetzen).
• Entfernen Sie Duplikate, falls vorhanden.
• Konvertieren Sie Datentypen, falls notwendig (z.B. wenn numerische Werte fälschlicherweise als Zeichenketten codiert sind).

3. Datenanalyse
• Berechnen Sie statistische Kennzahlen (Mittelwert, Median, Standardabweichung etc.) für jede numerische Spalte.
• Ermitteln Sie die Korrelation zwischen der Qualität des Weins und anderen chemischen Eigenschaften.

correlation = df.corr()
print(correlation['quality'].sort_values())


4. Datenvisualisierung ( erfordert matplotlib)
• Erstellen Sie Histogramme für einige chemische Eigenschaften, um ihre Verteilungen zu verstehen.
df['alcohol'].hist()
plt.title('Verteilung des Alkoholgehalts')

• Erstellen Sie ein Streudiagramm (Scatter Plot), um die Beziehung zwischen Alkoholgehalt und Qualität darzustellen.

plt.scatter(df['alcohol'], df['quality'])
plt.title('Alkoholgehalt vs. Qualität des Weins')

• Erstellen Sie Boxplots für die Qualität in Bezug auf verschiedene chemische Eigenschaften, um Unterschiede in den Qualitätsstufen zu erkennen.

df.boxplot(column='alcohol', by='quality')
plt.title('Alkoholgehalt nach Weinqualität')
