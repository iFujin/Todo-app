from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import TODO
from database import(
    get_one_todo,
    get_all_todos,
    insert_todo,
    update_todo,
    remove_todo
)

app=FastAPI()
origins=['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todo")
async def get_todo():
    response= await get_all_todos()
    return response

@app.get("/todo_get{title}",response_model=(TODO))
async def get_todo(title):
    response= await get_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f'{title} no database exists on the title')
  
@app.post("/todo_id",response_model=TODO)
async def post_todo(todo:TODO):
    response=await insert_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400,'no database exists on the title')

@app.put("/todo_update/{title}/",response_model=TODO)
async def put_todo(title:str,desc:str):
    response= await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404,f'{title} no database exists as per the title')


@app.delete("/todo_delete/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "todo sucessfully deleted"
    raise HTTPException(404,f'{title} no database exists')

        