from datetime import datetime, timezone
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "merchant_sample.json"


async def get_merchants(server: str | None = None):
    """
    지금은 웹 연결 테스트용 샘플 데이터입니다.
    실제 떠상 데이터 소스가 정해지면 이 함수 안에서 외부 API/DB 조회로 교체하면 됩니다.
    """
    with DATA_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if server:
        data["items"] = [item for item in data["items"] if item.get("server") == server]
        data["server"] = server
    else:
        data["server"] = "전체"

    data["updated_at"] = datetime.now(timezone.utc).isoformat()
    data["source"] = "sample"
    return data
