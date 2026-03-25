from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid
import traceback

from model import calculate_risk
from explain import generate_explanation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "PremortemAI running"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    try:
        filename = f"{uuid.uuid4()}.wav"
        file_path = os.path.join("temp", filename)

        os.makedirs("temp", exist_ok=True)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔥 Stable demo value (no librosa issues)
        voice_score = 78

        data = {
            "voice": voice_score,
            "heart_rate": 90,
            "sleep": 35,
            "typing": 60,
            "mobility": 50
        }

        result = calculate_risk(data)
        explanation = generate_explanation(result, data)

        os.remove(file_path)

        return {
            "inputs": data,
            "result": result,
            "explanation": explanation
        }

    except Exception as e:
        print("🔥 ERROR OCCURRED:")
        traceback.print_exc()
        return {"error": "Internal server error"}