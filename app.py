import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

# Simple endpoint to test moderation
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    comment = data.get("comment", "")
    score = float(data.get("score", 0))

    # Example logic – modify later for Perspective API integration
    if score > 0.8 or "suck" in comment.lower():
        return jsonify({
            "final_decision": "block",
            "reason": "High toxicity or keyword match"
        })
    else:
        return jsonify({
            "final_decision": "allow",
            "reason": "Low risk"
        })

# Render requires listening on dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
