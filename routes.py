from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/login/id')
async def get_login_id(email: Annotated[str, Query(max_length=100, pattern='^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*(?:\\.[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*)*\\.[a-zA-Z]{2,}$')], db: Session = Depends(get_db)):
    try:
        return await service.get_login_id(db, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teacher/update')
async def put_teacher_update(raw_data: schemas.PutTeacherUpdate, db: Session = Depends(get_db)):
    try:
        return await service.put_teacher_update(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teacher/id')
async def get_teacher_id(id: Annotated[str, Query(max_length=100)], headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.get_teacher_id(db, id, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/delete')
async def delete_delete(raw_data: schemas.DeleteDelete, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.delete_delete(db, raw_data, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/allrecords')
async def get_students_allrecords(headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.get_students_allrecords(db, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/file_upload')
async def post_file_upload(document: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_file_upload(db, document)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/join1')
async def get_join1(db: Session = Depends(get_db)):
    try:
        return await service.get_join1(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/join2')
async def get_join2(full_name: Annotated[str, Query(max_length=100)], email: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.get_join2(db, full_name, email)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/file_upload2')
async def post_file_upload2(document1: UploadFile, headers: Request, db: Session = Depends(get_db)):
    try:
        return await service.post_file_upload2(db, document1, headers)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/exam')
async def post_exam(raw_data: schemas.PostExam, db: Session = Depends(get_db)):
    try:
        return await service.post_exam(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teachers')
async def post_teachers(raw_data: schemas.PostTeachers, db: Session = Depends(get_db)):
    try:
        return await service.post_teachers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

