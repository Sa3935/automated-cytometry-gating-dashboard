import scanpy as sc

def compute_umap(adata, seed: int = 42):
    sc.tl.pca(adata, svd_solver="arpack", random_state=seed)
    sc.pp.neighbors(adata, n_neighbors=15, n_pcs=30, random_state=seed)
    sc.tl.umap(adata, random_state=seed)
    return adata.obsm["X_umap"]
