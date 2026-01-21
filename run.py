import sys
sys.path.append("automated-cytometry-gating-dashboard/backend")

from app.preprocessing import preprocess_data
from app.embeddings import compute_umap
from app.gating import automated_gating

adata = preprocess_data()
umap = compute_umap(adata)
labels, _ = automated_gating(umap)

print("Cells:", umap.shape[0], "Clusters:", len(set(labels)))
