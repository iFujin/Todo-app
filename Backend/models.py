from pydantic import BaseModel
class TODO(BaseModel):
    title:str
    description:str