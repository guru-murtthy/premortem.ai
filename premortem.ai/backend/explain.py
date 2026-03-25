def generate_explanation(result, data):
    if result["risk_level"] == "HIGH":
        return f"""
High physiological stress detected.

Key factors:
- Elevated heart rate: {data['heart_rate']} bpm
- Poor sleep patterns
- Increased voice stress markers

Suggested actions:
- Stay hydrated
- Reduce workload
- Monitor blood pressure
- Seek medical advice if needed
"""
    elif result["risk_level"] == "MEDIUM":
        return "Moderate risk detected. Improve sleep and reduce stress."
    else:
        return "Low risk. Maintain healthy lifestyle."