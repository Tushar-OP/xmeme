from sqlalchemy.orm import Session
import models
import schemas


def get_single_meme(db: Session, meme_id: int):
    return db.query(models.Meme).filter(models.Meme.id == meme_id).first()


def patch_single_meme(db: Session, meme_id: int, meme: schemas.MemeUpdate):
    db_meme = db.query(models.Meme).filter(models.Meme.id == meme_id).first()
    if meme.caption:
        db_meme.caption = meme.caption
    if meme.url:
        db_meme.url = meme.url
    db.commit()
    db.refresh(db_meme)
    return db_meme


def get_memes(db: Session):
    return db.query(models.Meme).order_by(models.Meme.timestamp.desc()).limit(100).all()


def create_meme(db: Session, meme: schemas.MemeCreate):
    db_meme = models.Meme(name=meme.name, caption=meme.caption, url=meme.url)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def get_meme_from_details(db: Session, meme: schemas.MemeCreate):
    db_meme_with_caption = db.query(
        models.Meme).filter(models.Meme.caption == meme.caption).first()
    db_meme_with_url = db.query(models.Meme).filter(
        models.Meme.url == meme.url).first()

    if (db_meme_with_caption is None) and (db_meme_with_url is None):
        return False

    return True
