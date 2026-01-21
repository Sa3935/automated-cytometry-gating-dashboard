import React from "react";

type Props = { umap: number[][]; labels: number[] };

export default function UMAPPlot({ umap }: Props) {
  const width = 800, height = 500;
  const xs = umap.map(p => p[0]);
  const ys = umap.map(p => p[1]);
  const minX = Math.min(...xs), maxX = Math.max(...xs);
  const minY = Math.min(...ys), maxY = Math.max(...ys);

  const scaleX = (x:number) => ((x - minX) / (maxX - minX)) * (width - 40) + 20;
  const scaleY = (y:number) => height - (((y - minY) / (maxY - minY)) * (height - 40) + 20);

  return (
    <svg width={width} height={height} style={{ border: "1px solid #ccc" }}>
      {umap.slice(0, 5000).map((p, i) => (
        <circle key={i} cx={scaleX(p[0])} cy={scaleY(p[1])} r={2} opacity={0.7} />
      ))}
    </svg>
  );
}
