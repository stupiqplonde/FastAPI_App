from fastapi import APIRouter, Depends
from forms import UserLoginForm
from models import connect_db

route = APIRouter()

@route.get("/")
def index():
    return {"message": "OK"}

@route.post("/login")
def login(user_forms: UserLoginForm, database= Depends(connect_db)):
    return {"status": "OK",
            "form": user_forms.email,
            "database": database,
    }