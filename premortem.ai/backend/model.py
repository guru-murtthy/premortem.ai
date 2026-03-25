import librosa
import numpy as np

def analyze_voice(file_path):
    y, sr = librosa.load(file_path, sr=16000)

    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13))
    pitch = np.mean(librosa.yin(y, fmin=50, fmax=300))
    energy = np.mean(librosa.feature.rms(y=y))

    score = abs((mfcc + pitch + energy) % 100)

    return round(score, 2)


def calculate_risk(data):
    risk = (
        0.35 * data["voice"] +
        0.25 * data["heart_rate"] +
        0.15 * data["sleep"] +
        0.15 * data["typing"] +
        0.10 * data["mobility"]
    )

    if risk > 70:
        level = "HIGH"
    elif risk > 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": round(risk, 2),
        "risk_level": level
    }