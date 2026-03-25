import React from "react";

function Result({ data }) {
  if (!data) return null;

  if (data.error) {
    return <h3 style={{ color: "red" }}>Error: {data.error}</h3>;
  }

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>
        Risk Score: {data?.result?.risk_score ?? "Loading..."}
      </h2>

      <h3>
        Status: {data?.result?.risk_level ?? "Loading..."}
      </h3>

      <p>{data?.explanation ?? ""}</p>
    </div>
  );
}

export default Result;