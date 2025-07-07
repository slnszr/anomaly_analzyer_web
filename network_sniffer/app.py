from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from network_sniffer.ml_model import predict_packet_with_confidence
from dotenv import load_dotenv
import os
import cohere

# Ortam değişkenlerini yükle
load_dotenv()

# Cohere istemcisi
co = cohere.Client(os.getenv("COHERE_API_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_key")

# Basit kullanıcı veritabanı (geliştirilebilir)
users = {
    "doruk": "deneme",
    "selin": "deneme1"
}

# ⛔ Login ekranı
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# ✅ Giriş yapılmadan erişim engeli
@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/about")
def about():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("about_us.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    if "packet_size" not in data:
        return jsonify({"error": "Missing 'packet_size' in request"}), 400

    try:
        size = int(data["packet_size"])
        label, confidence = predict_packet_with_confidence(size)
        return jsonify({
            "packet_size": size,
            "prediction": label,
            "confidence": round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chatbot", methods=["POST"])
def chatbot():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    user_msg = data.get("message", "").strip()

    if not user_msg:
        return jsonify({"response": "Please enter a message."}), 400

    try:
        response = co.chat(
            model="command-r",
            message=user_msg,
            temperature=0.5
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error from AI: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
