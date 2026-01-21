from app.preprocessing import preprocess_data
from app.embeddings import compute_umap
from app.gating import automated_gating

def test_pipeline_runs_end_to_end():
    adata = preprocess_data(seed=42)
    umap = compute_umap(adata, seed=42)
    labels, model = automated_gating(umap)

    assert umap.shape[0] == len(labels)
    assert umap.shape[1] == 2
    assert model is not None
