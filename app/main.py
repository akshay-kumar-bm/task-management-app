from fastapi import FastAPI

app = FastAPI(title="Task Management App")


@app.get("/health")
def health():
    return {"status": "ok"}
