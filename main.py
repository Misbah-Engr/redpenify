from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI(title="RedPenify API", version="0.1.0")

@app.get("/")
async def health():
    return {"status": "alive"}

@app.post("/grade/objective")
async def grade_objective(key: List[str], answers: List[str]):
    if len(key) != len(answers):
        raise HTTPException(400, "mismatched lengths")
    score = sum(a == b for a, b in zip(key, answers))
    return {"score": score, "total": len(key)}
