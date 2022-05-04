import json
from typing import List

# FastAPI
from fastapi import FastAPI, status, Body

# Local
from .models import User, Tweet, UserRegister, UserLogin

app = FastAPI()

# Path Operations

## Users

@app.post(
    path='/auth/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Create a new user',
    tags=['Auth'],
)
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operation register a user in the app

    Parametrs:
        - Request body parameter
            - user: UserRegister

    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("backend/users.json", "r+", encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user




@app.post(
    path='/auth/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a new user',
    tags=['Auth'],
)
def login(user: UserLogin = Body(...)):
    """Search in users.json for a coincidence on an email and password"""
    with open("backend/users.json", "r+", encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        for register_user in results:
            if register_user['email'] == user_dict['email'] and register_user['password'] == user_dict['password']:
                return User(**register_user)

@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users'],
)
def show_all_users():
    """
    Show all users

    This path operation returns a json with all users registered in the app
    """
    with open("backend/users.json", "r+", encoding='utf-8') as f:
        results = json.loads(f.read())
        return results


@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a user',
    tags=['Users'],
)
def show_user():
    pass


@app.delete(
    path='/users/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Delete a user',
    tags=['Users'],
)
def delete_user():
    pass


@app.patch(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['Users'],
)
def update_user():
    pass


# Tweets

@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets'],
)
def home():
    return {"Twitter API": "Working"}


@app.post(
    path='/tweets',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Create a new tweet',
    tags=['Tweets'],
)
def create_tweet():
    pass



@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets'],
)
def show_tweet():
    pass


@app.delete(
    path='/tweets/{tweet_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Delete a tweet',
    tags=['Tweets'],
)
def delete_tweet():
    pass


@app.patch(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets'],
)
def update_tweet():
    pass