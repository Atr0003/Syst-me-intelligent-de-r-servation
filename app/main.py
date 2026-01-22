from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine


app = FastAPI()

@app.get("/")
def root():
    return {"api_status": "API is running. See /docs for documentation."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"database_status": "connected"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)