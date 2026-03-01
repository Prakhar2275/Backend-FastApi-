from fastapi import FastAPI,Depends,HTTPException,status

from sqlalchemy.orm import Session
from APP import models
from APP import schemas
from APP import crud

from APP.database import engine,get_db,Base

from typing import List
app=FastAPI(
    title="Mini Notes API",
    description="A simple CRUD API to create, read, update and delete notes.",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.post("/notes",response_model=List[schemas.NoteResponse])

def create_note(note:schemas.NoteCreate,db:Session=Depends(get_db)):
    return crud.create_note(db,note)



@app.get("/notes",response_model=schemas.NoteResponse)

def get_notes(db:Session=Depends(get_db)):
    return crud.get_all_notes(db)



@app.get("/notes/{note_id}",response_model=schemas.NoteResponse)

def get_note(note_id:int,db:Session=Depends(get_db)):
    note=crud.get_note(db,note_id)

    if not note:
        raise HTTPException(status_code=404,detail=f"User with id {note_id} not Found!!!")

    return note

@app.put("/notes/{note_id}",response_model=schemas.NoteResponse)

def update_node(note_id:int,note:schemas.NoteUpdate,db:Session=Depends(get_db)):
    return crud.update_note(db,note_id,note)

@app.delete("/notes/{note_id}")
def delete_note(note_id:int,db:Session=Depends(get_db)):
    delete_note=crud.delete_node(db,note_id)

    if not delete_note:
        raise HTTPException(status_code=404,detail="Note Not Found")
    
    return {"message":"Note Deleted"}

