from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/send", methods=["POST"])
def send_instruction():
    data = request.json
    if "instruction" in data:
        instruction = data["instruction"]
        # Vous pouvez ici gérer l'instruction, l'envoyer ailleurs, etc.
        return jsonify({"status": "success", "instruction_sent": instruction})
    return jsonify({"status": "error", "message": "No instruction provided"})

@app.route("/receive", methods=["GET"])
def receive_instruction():
    # Simuler une instruction
    instruction = "example_command"
    return jsonify({"instruction": instruction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
