from fastapi import FastAPI

app = FastAPI(title="Rohit AI Video Agent")


@app.get("/")
def home():
    return {
        "message": "Rohit AI Video Agent is running"
    }
