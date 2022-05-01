from typing import List

# FastAPI
from fastapi import FastAPI, status

# Local
from .models import User, Tweet

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
def signup():
    pass


@app.post(
    path='/auth/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a new user',
    tags=['Auth'],
)
def login():
    pass


@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users'],
)
def show_all_users():
    pass


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