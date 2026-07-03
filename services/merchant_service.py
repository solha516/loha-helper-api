import json
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "merchants.json"

def _load_data() -> dict[str, Any]:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def get_merchants(server: str | None = None) -> dict[str, Any]:
    data = _load_data()
    merchants = data.get("merchants", [])
    if server:
        merchants = [m for m in merchants if m.get("server") == server]
    return {
        "status": "ok",
        "source": data.get("source", "sample"),
        "updated_at": data.get("updated_at"),
        "server": server,
        "count": len(merchants),
        "merchants": merchants,
    }
