import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.svm import SVC

def automated_gating(embeddings: np.ndarray):
    clustering = DBSCAN(eps=0.6, min_samples=30).fit(embeddings)
    labels = clustering.labels_

    mask = labels != -1
    if mask.sum() < 10:
        labels = np.zeros((embeddings.shape[0],), dtype=int)
        mask = np.ones_like(labels, dtype=bool)

    clf = SVC(kernel="rbf", probability=True, gamma="scale")
    clf.fit(embeddings[mask], labels[mask])

    return labels, clf
