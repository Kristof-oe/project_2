import time
import asyncio
from app.db.model import *
from fastapi import APIRouter, HTTPException
from app.db.session import *

router = APIRouter(
    prefix="/task"
)


async def task_proccessing(task_id: int):
    with Session(engine) as session:
        task = session.get(Tasks, task_id)
        if not task:
            return
        
        task.status = "running"
        session.commit()

        try:
            time.sleep(2)
            task.status = "done"
        except Exception:
            task.status = "failed" 

        session.commit()


@router.post("/")
async def create_task(tasks_create: TaskCreate, session: SessionType) -> TaskResponse:

    tasks = Tasks (

        task_data=tasks_create.task_data,

    )
    session.add(tasks)
    session.commit()
    session.refresh(tasks)

    asyncio.create_task(task_proccessing(tasks.task_id))

    return {TaskResponse(
        task_id=tasks.task_id,
        status=tasks.status
        ) }

@router.get("/{task_id}")
async def read_task(task_id: int, session: SessionType) -> TaskResponse: 
    tasks = session.get(Tasks, task_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return TaskResponse(

        task_id=tasks.task_id,
        task_data=tasks.task_data,
        status=tasks.status
    )
       

@router.delete("/{task_id}")
async def del_task(task_id: int, session: SessionType): 
    try:
        tasks = await read_task(task_id, session)
    except HTTPException:
        raise

    session.delete(tasks)
    session.commit()
    return {"ok": True}


@router.get("/")
async def read_task_all(session = SessionType) -> list[TaskResponse]:

    tasks=session.exec(select(Tasks)).all()

    for task in tasks:
        
        return TaskResponse(
        task_id=task.task_id,
        task_data=task.stask_data,
        status=task.status
    )