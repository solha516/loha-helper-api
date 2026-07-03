import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "merchants_sample.json"

def get_merchants(server: str | None = None):
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if server:
        return {"server": server, "merchants": data.get(server, [])}
    return {"servers": list(data.keys()), "data": data}
