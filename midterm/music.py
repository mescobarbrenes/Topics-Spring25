from fastapi import APIRouter, Path, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List
from user import User
from auth import get_current_user

music_router = APIRouter()

class MusicItem(BaseModel):
    id: int
    title: str
    artist: str
    description: str = ""
    owner: str

class MusicItemRequest(BaseModel):
    title: str 
    artist: str 
    description: str = ""

music_list = []
max_id: int = 0

#create a new music item (protected)
@music_router.post("", status_code = status.HTTP_201_CREATED, response_model = MusicItem)
def add_music(item: MusicItemRequest, current_user: User = Depends(get_current_user)): #accepts request model without id
    global max_id
    max_id += 1
    new_item = MusicItem(id = max_id, title = item.title, artist = item.artist, description = item.description, owner = current_user.username)
    music_list.append(new_item)
    return new_item

#reads all music items (protected)
@music_router.get("", response_model = List[MusicItem])
def get_music(current_user: User = Depends(get_current_user)):
    return [item for item in music_list if item.owner == current_user.username]

#gets a specific music item by id (protected)
@music_router.get("/{id}", response_model = MusicItem)
def get_music_by_id(id: int = Path(..., title = "Music ID"), current_user: User = Depends(get_current_user)):
    for item in music_list:
        if item.id == id:
            if item.owner != current_user.username:
                raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "You are not the owner of this post.")
            return item
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Music item with ID={id} not found.")

#updates a music item (protected)
@music_router.put("/{id}", response_model = MusicItem)
def update_music(id: int, updated_item: MusicItemRequest, current_user: User = Depends(get_current_user)):
    for index, item in enumerate(music_list):
        if item.id == id:
            if item.owner != current_user.username:
                raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "You can't update someone else's post.")
            music_list[index] = MusicItem(id=id, **updated_item.dict())
            return music_list[index]
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Music item with ID={id} not found.")

#deletes a music item
@music_router.delete("/{id}")
def delete_music(id: int, current_user: User = Depends(get_current_user)):
    global music_list
    for item in music_list:
        if item.owner != current_user.username:
            raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "You can't delete someone else's post.")
    music_list = [item for item in music_list if item.id != id]
    return {"message": f"Music item with ID={id} has been deleted."}