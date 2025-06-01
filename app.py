import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No JSON received"}), 400

        comment = data.get("comment", "")
        score = float(data.get("score", 0))

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

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
