import React from "react";
import { uploadAudio } from "./api";

let mediaRecorder;
let audioChunks = [];

function Recorder({ setResult }) {

  const startRecording = async () => {
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert("Microphone not supported. Use localhost.");
        return;
      }

      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: "audio/wav" });
        const file = new File([blob], "voice.wav");

        try {
          const data = await uploadAudio(file);
          console.log("API RESPONSE:", data);
          setResult(data);
        } catch (err) {
          console.error("UPLOAD ERROR:", err);
        }

        audioChunks = [];
      };

      mediaRecorder.start();

      setTimeout(() => {
        mediaRecorder.stop();
      }, 4000);

    } catch (err) {
      console.error("MIC ERROR:", err);
    }
  };

  return (
    <button onClick={startRecording}>
      Start Voice Scan
    </button>
  );
}

export default Recorder;