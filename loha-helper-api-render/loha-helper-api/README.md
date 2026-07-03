# LoHA Helper API

FastAPI backend for LoA Helper web/program.

## Local run
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Endpoints
- `GET /`
- `GET /health`
- `GET /merchant`
- `GET /merchant?server=카제로스`
- `GET /fieldboss`
- `GET /chaosgate`
- `GET /adventure`
- `GET /character/{name}`

## Render
- Runtime: Python
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- Plan: Free

현재 `merchant`는 웹 연결 테스트용 샘플 데이터입니다. 실제 실시간 데이터 소스가 확정되면 `services/merchant_service.py` 안의 fetch 부분만 교체하면 됩니다.
