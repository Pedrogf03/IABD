from flask import Flask, render_template, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)

# Conexión MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.smartparking

def parse_bay(bay_id: str):
    """
    Extrae planta (level) y número (int) del bay_id, ej: L2-A-14 → (2, 14)
    """
    if not bay_id:
        return None, None
    match = re.match(r"L(\d+)[-_]A[-_](\d+)", bay_id.upper())
    if match:
        level = int(match.group(1))
        number = int(match.group(2))
        return level, number
    return None, None

@app.route('/')
def index():
    return render_template('bays.html')

@app.route('/api/bays')
def api_bays():
    docs = list(db.bays.find({}, {'_id': 0}))
    grouped = {}

    for d in docs:
        level, number = parse_bay(d.get('bay_id', ''))
        if level is None:
            continue
        d['level'] = level
        d['number'] = number
        grouped.setdefault(level, []).append(d)

    # ordenar internamente cada planta
    for level in grouped:
        grouped[level] = sorted(grouped[level], key=lambda x: x['number'])

    # ordenar las plantas
    sorted_levels = dict(sorted(grouped.items(), key=lambda x: x[0]))

    # contadores globales
    all_bays = [b for bays in grouped.values() for b in bays]
    occupied = sum(1 for b in all_bays if b.get('occupied'))
    free = len(all_bays) - occupied

    return jsonify({
        "levels": sorted_levels,
        "counts": {"occupied": occupied, "free": free, "total": len(all_bays)}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
