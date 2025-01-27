from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import make_scorer, adjusted_rand_score

# Dataset di esempio
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Definisci il modello
agg_clustering = AgglomerativeClustering()

# Definisci la griglia di parametri da testare
# 'euclidean' è la metrica di default
param_grid = {
    'n_clusters': range(2, 11),
    'linkage': ['ward', 'complete', 'average', 'single'],
    'metric': ['euclidean', 'l1', 'l2', 'manhattan', 'cosine'] # Aggiunte metriche compatibili
}

# Rimuovi 'euclidean' se linkage non è 'ward'
param_grid['metric'] = [m for m in param_grid['metric'] if m != 'euclidean' or 'ward' in param_grid['linkage']]


# Esegui la Grid Search
scorer = make_scorer(adjusted_rand_score, greater_is_better=True)
grid_search = GridSearchCV(agg_clustering, param_grid, cv=5, scoring=scorer)
grid_search.fit(X)

# Stampa i risultati
print("Migliori parametri:", grid_search.best_params_)
print("Miglior score (Adjusted Rand Score):", grid_search.best_score_)

# Addestra il modello con i parametri ottimali
best_agg_clustering = grid_search.best_estimator_
labels = best_agg_clustering.fit_predict(X)

# Visualizza i cluster
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.title(f"Agglomerative Clustering (n_clusters={best_agg_clustering.n_clusters}, linkage={best_agg_clustering.linkage})")
plt.show()

# Funzione per visualizzare il dendrogramma (opzionale)
def plot_dendrogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count
    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)
    dendrogram(linkage_matrix, **kwargs)

# Visualizza il dendrogramma (opzionale)
# Per visualizzarlo correttamente bisogna prima fittare il modello senza n_clusters
# Se linkage='ward', usiamo metric='euclidean', altrimenti la metrica ottimale trovata
if grid_search.best_params_['linkage'] == 'ward':
    model_temp = AgglomerativeClustering(distance_threshold=0, n_clusters=None, linkage='ward', metric='euclidean')
else:
    model_temp = AgglomerativeClustering(distance_threshold=0, n_clusters=None, linkage=grid_search.best_params_['linkage'], metric=grid_search.best_params_['metric'])
model_temp = model_temp.fit(X)
plt.title("Dendrogramma")
plot_dendrogram(model_temp, truncate_mode='level', p=3)
plt.xlabel("Numero di punti nel nodo (o indice del punto se non c'è parentesi).")
plt.show()