import uuid

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from app.forms import UserCreateForm
from app.forms import UserLoginForm
from model import connect_db, User, AuthToken
from util import get_password_hash
from auth import check_auth_token

router = APIRouter()

@router.get('/')
def root():
    return {"message": "Hello World"}

@router.post('/login')
def login(user_form: UserLoginForm, datadase=Depends(connect_db)):
    user = datadase.query(User).filter(User.email==user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {"message": "Login NOT Successfully"}
    auth_token = AuthToken(token=str(uuid.uuid4()), user=user.id)
    datadase.add(auth_token)
    datadase.commit()
    return {"token": auth_token.token}


@router.post('/user', name='create_user')
def create_user(user_form: UserCreateForm, datadase=Depends(connect_db)):
    exist_user = datadase.query(User.id).filter(email=user_form.email).one_or_none()
    if exist_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        email=user_form.email,
        password=get_password_hash(user_form.password),
        first_name=user_form.first_name,
        last_name=user_form.last_name,
        nick_name=user_form.nick_name
    )
    datadase.add(new_user)
    datadase.commit()
    return {'new user id':new_user.id}
