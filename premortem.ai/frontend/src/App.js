import React, { useState } from "react";
import Recorder from "./Recorder";
import Result from "./Result";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>PremortemAI</h1>

      <Recorder setResult={setResult} />

      <Result data={result} />
    </div>
  );
}

export default App;