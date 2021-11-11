from models import TODO
import motor.motor_asyncio

client= motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database=client.todolist
collection=database.todo

async def get_one_todo(title):
    document=await collection.find_one({'title':title})
    return document

async def get_all_todos():
    todo=[]
    header= collection.find({})
    async for document in header:
        todo.append(TODO(**document))
    return todo

async def insert_todo(todo):
    document=todo
    result=await collection.insert_one(document) 
    return document
  
async def update_todo(title,desc):
    await collection.update_one({"title":title},{"$set":{
        "description":desc}})
    document= await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({'title':title})
    return True

    


        

    

