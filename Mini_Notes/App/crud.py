from sqlalchemy.orm import Session
from APP import models
from APP import schemas
from fastapi import Depends,HTTPException,status

def create_note(db:Session,note:schemas.NoteCreate):
    db_note=models.Note(
        title=note.title,
        content=note.content
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note




def get_all_notes(db:Session):
    return db.query(models.Note).all()




def get_note(db:Session,note_id:int):
    return db.query(models.Note).filter(models.Note.id==note_id).first()




def update_note(db:Session,note_id:int,note:schemas.NoteUpdate):

    db_note=db.query(models.Note).filter(models.Note.id==note_id).first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {note_id} not Found!!!")
    
    if note.title is not None:
        db_note.title=note.title

    if note.content is not None:
        db_note.content=note.content

    db.commit()
    db.refresh(db_note)

    return db_note
    



def delete_node(db:Session,note_id:int):
    db_note=db.query(models.Note).filter(models.Note.id==note_id).first()

    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {note_id} not Found!!!")
    
    db.delete(db_note)

    db.commit()

    return db_note

