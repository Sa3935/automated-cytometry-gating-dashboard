from pydantic import BaseModel
from typing import List

class AnalyzeResponse(BaseModel):
    umap: List[List[float]]
    labels: List[int]
    n_cells: int
