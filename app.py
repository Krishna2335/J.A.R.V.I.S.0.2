from flask import Flask, render_template, jsonify
import threading

print("✅ app.py loaded")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start_jarvis():
    print("🎤 /start endpoint hit")
    import jarvis
    threading.Thread(target=jarvis.main, daemon=True).start()
    return jsonify({"status": "Jarvis started"})

if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(host="127.0.0.1", port=8080, debug=False, use_reloader=False)
