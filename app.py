from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_comment():
    data = request.get_json()
    comment = data.get("comment", "")
    score = data.get("score", 0.0)

    if score >= 0.85 or "hate" in comment.lower():
        return jsonify({
            "final_decision": "block",
            "reason": "High toxicity or keyword match"
        })
    else:
        return jsonify({
            "final_decision": "allow",
            "reason": "Low risk"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)