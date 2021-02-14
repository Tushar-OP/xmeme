from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Xmeme API",
    description="A meme curator API",
    version="0.0.1",
    docs_url='/swagger-ui',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/memes/", response_model=schemas.Meme, status_code=201)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    exists = crud.get_meme_from_details(db, meme)
    if exists:
        raise HTTPException(
            status_code=409,
            detail="Meme with the given details already exists"
        )

    return crud.create_meme(db=db, meme=meme)


@app.get("/memes/", response_model=List[schemas.Meme])
def read_memes(db: Session = Depends(get_db)):
    memes = crud.get_memes(db)
    return memes


@app.get("/memes/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_single_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@app.patch("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(
    meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)
):
    db_meme = crud.get_single_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(
            status_code=404, detail=f"Meme with the id {meme_id} not found")

    if meme.caption is None and meme.url is None:
        raise HTTPException(
            status_code=409,
            detail="Parameters 'caption' and 'url' both must not be null")

    return crud.patch_single_meme(db=db, meme=meme, meme_id=meme_id)
