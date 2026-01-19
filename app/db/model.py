from sqlmodel import Field, SQLModel, select

class TaskBase(SQLModel):
    task_data: str
    payload: str

class TaskCreate(TaskBase):
    pass

class Tasks (TaskBase, table=True):
    task_id: int | None = Field(default=None, primary_key=True)
    status: str ="pending"


class TaskResponse(SQLModel):
    task_id: int
    status: str
    task_data: str
