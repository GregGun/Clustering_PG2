import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

# Daten aus CSV laden
path = "/Users/student/PycharmProjects/Clustering_PG2/winequality-red.csv"
data = pd.read_csv(path, delimiter=";")

print(data)

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
data_new.to_csv("./data_new_winequality-red.csv")

# ScatterPlot
plt.scatter(data_new['quality'], data_new['residual sugar'])
plt.title('Weinqualität')
plt.xlabel('Qualität')
plt.ylabel('Restzucker')
plt.show()
