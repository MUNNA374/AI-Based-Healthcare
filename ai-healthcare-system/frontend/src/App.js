import React, { useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleFileChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image!");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    try {
      const res = await axios.post("http://localhost:5000/predict", formData);
      setPrediction(res.data.prediction);
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to get prediction.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h2>AI Healthcare Diagnosis</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Predict</button>
      {prediction && <h3>Prediction: {prediction}</h3>}
    </div>
  );
}

export default App;
