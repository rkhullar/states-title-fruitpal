from pydantic import BaseModel


class HelloBase(BaseModel):
    message: str


class HelloCreate(HelloBase):
    pass


class Hello(HelloBase):
    id: int

    class Config:
        orm_mode = True
