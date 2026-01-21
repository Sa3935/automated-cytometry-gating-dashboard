# Automated Cytometry Gating & Interactive Visualization Dashboard

End-to-end pipeline for automated gating and interactive visualization of high-dimensional single-cell immune data using Python, FastAPI, and React (TypeScript).

## Features
- Preprocessing + QC + normalization (Scanpy)
- UMAP embedding
- Automated gating (DBSCAN) + learned boundaries (SVM)
- FastAPI endpoint `/analyze`
- Integration tests (pytest)
- CI-ready repo structure

## Run tests
pytest backend/tests
