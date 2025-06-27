from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

STATS_FILE = 'stats.json'

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {}
    with open(STATS_FILE, 'r') as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    stats = load_stats()
    if request.method == 'POST':
        try:
            new_stats = json.loads(request.form['stats_json'])
            save_stats(new_stats)
            stats = new_stats
        except json.JSONDecodeError:
            pass  # Optional: handle error here
    return render_template('status.html', stats=stats, stats_json=json.dumps(stats, indent=4))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
