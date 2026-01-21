import React, { useEffect, useState } from "react";
import { fetchAnalysis } from "./api";
import UMAPPlot from "./components/UMAPPlot";

export default function App() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetchAnalysis().then(setData).catch(console.error);
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div style={{ padding: 20 }}>
      <h2>Automated Gating Dashboard</h2>
      <p>Cells: {data.n_cells}</p>
      <UMAPPlot umap={data.umap} labels={data.labels} />
    </div>
  );
}
