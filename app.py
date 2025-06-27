from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_stats():
    with open("stats.json", "r") as f:
        return json.load(f)

def save_stats(data):
    with open("stats.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        updated_stats = {key: request.form[key] for key in request.form}
        save_stats(updated_stats)
        return redirect("/")
    
    stats = load_stats()
    return render_template("status.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
