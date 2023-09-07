from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Users"], responses={404: {"message":"No encontrado"} })

# Inicia el server: uvicorn users:app --reload

# Entidad Users
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Ariel", surname="Tapia", url="https://moure.dev", age=31),
              User(id=2, name="Marcela", surname="Navarrete",url="https://mouredev.com", age=29),
              User(id=3, name="Brais", surname="Moure", url="https://haakon.com", age=35)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Ariel", "surname": "Tapia", "url": "https://moure.dev", "age": 31},
            {"name": "Marcela", "surname": "Navarrete", "url": "https://moure.dev", "age": 29},
            {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35}]

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}") # Path
async def user(id: int):
    return search_user(id)


@router.get("/user/") # Query enviar parametro en url con ?id=2&name=marcela por ejemplo
async def user(id: int):
    return search_user(id)

@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        #return {"Error": "El usuario ya existe"}
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    users_list.append(user)
    return user

@router.put("/user/")
async def user(user: User):
    
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    return user

@router.delete("/user/{id}")
async def user(id:int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    #return user

# funcion para obtener usuario por id
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}