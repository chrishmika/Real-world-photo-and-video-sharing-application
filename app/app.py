from fastapi import FastAPI, HTTPException


server = FastAPI()

text_post = {
    1: {"title": "First Post", "post": "This is the content of the first post."},
    2: {"title": "Morning Routine", "post": "Started the day with coffee and a short walk."},
    3: {"title": "FastAPI Notes", "post": "Learning how path parameters and validation work."},
    4: {"title": "Photo Dump", "post": "Uploaded a few sunset photos from last weekend."},
    5: {"title": "Workout Log", "post": "Completed a 30-minute cardio session today."},
    6: {"title": "Travel Idea", "post": "Planning a trip to the mountains next month."},
}

@server.get("/posts")
def get_al_posts():
    return text_post
    
    
@server.get("/posts/{id}")
def get_post(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_post.get(id)