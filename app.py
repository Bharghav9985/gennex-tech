from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name    = data.get("name", "")
    email   = data.get("email", "")
    company = data.get("company", "")
    message = data.get("message", "")
    # TODO: hook up email / database here
    print(f"New enquiry from {name} ({email}) at {company}: {message}")
    return jsonify({"status": "ok", "message": "Thank you! We'll be in touch shortly."})

if __name__ == "__main__":
    app.run(debug=True)
