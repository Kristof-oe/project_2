from typing import Union
import asyncio
import uuid
from fastapi import FastAPI

app = FastAPI()

task={}

@app.get("/health")
def health():
    return {"status": "ok" }


async def task_proccessing(task_id: str):
    try:
        task[task_id]["status"] = "running"
        await asyncio.sleep(2)
        task[task_id]["status"] = "done"
    except Exception:
        task[task_id]["status"] = "failed"

@app.post("/task/")
async def task_making(task_data: str):
    task_id=str(uuid)
    task[task_id]["status"] = "pending"

    asyncio.task_making(task_proccessing(task_id))
    return {"task_id": task_id}
   
    
@app.get("/task/{task_id}")
async def read_task(task_id: str):
    return task.get(task_id, {"error": "there is not"})



