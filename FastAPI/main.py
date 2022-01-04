from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# defines how a post should look like
class Post(BaseModel):
    title: str
    Content: str
    published : bool = True
    rating : Optional[int] = None

my_posts = [{"title": "title of post 1","content":"content of post 1","id":1},{"title":"favourite foods", "content":"I like pizza", "id":2}]


@app.get("/")
def read_root():
    return {"Hello": "Welcome To My First API"}

@app.get("/posts")
def get_posts():
    return {"Data":my_posts}

# making use of the Model
@app.post("/createposts")
def createposts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 100000000)
    my_posts.append()
    return{"data": post_dict}



