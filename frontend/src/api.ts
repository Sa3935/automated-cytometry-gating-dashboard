export async function fetchAnalysis() {
  const res = await fetch("http://localhost:8000/analyze?seed=42");
  if (!res.ok) throw new Error("API request failed");
  return res.json();
}
