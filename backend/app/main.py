from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.preprocessing import preprocess_data
from app.embeddings import compute_umap
from app.gating import automated_gating
from app.schemas import AnalyzeResponse

app = FastAPI(title="Automated Gating API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze", response_model=AnalyzeResponse)
def analyze(seed: int = 42):
    adata = preprocess_data(seed=seed)
    umap = compute_umap(adata, seed=seed)
    labels, _ = automated_gating(umap)

    return AnalyzeResponse(
        umap=umap.tolist(),
        labels=labels.tolist(),
        n_cells=int(umap.shape[0]),
    )
