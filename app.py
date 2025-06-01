import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env (optional, helpful for local testing)
load_dotenv()

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    comment = data.get("comment", "")
    score = float(data.get("score", 0))

    # Basic rule for blocking based on score or keyword
    if score > 0.8 or any(word in comment.lower() for word in ["suck", "idiot", "stupid"]):
        return jsonify({
            "final_decision": "block",
            "reason": "High toxicity or keyword match"
        }), 200
    else:
        return jsonify({
            "final_decision": "allow",
            "reason": "Low risk"
        }), 200

# Main entry for Render (bind to dynamic port)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
