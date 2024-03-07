import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

path = "/Users/student/PycharmProjects/Clustering_PG2/diamonds.csv"
data = pd.read_csv(path, delimiter=",")
data_unknown = data.drop(['cut', 'Unnamed: 0'], axis=1)
# transformieren
conv_num = ['clarity', 'color']
data_unknown[conv_num] = data_unknown[conv_num].astype('category')
data_unknown[conv_num] = data_unknown[conv_num].apply(lambda x: x.cat.codes)

s_scaler = StandardScaler()
data_unknown = pd.DataFrame(s_scaler.fit_transform(data_unknown), columns=data_unknown.columns)
print(data_unknown)

model = KMeans()
visualizer = KElbowVisualizer(model, K=(2, 9), timings=False)
visualizer.fit(data_unknown)
visualizer.show()
KMeans = KMeans(n_clusters=5)
pred = KMeans.fit_predict(data_unknown)
data_new = pd.concat([data, pd.DataFrame(pred, columns=["label"])], axis=1)
print(data_new)
data_new.to_csv("./data_new_dimonds.csv")
