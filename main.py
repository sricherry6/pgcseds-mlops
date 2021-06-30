from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Cred Scoring",
    docs_url="/"
)


@app.get("/ping")
def ping():
    return {"ping": "pong"}

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)
