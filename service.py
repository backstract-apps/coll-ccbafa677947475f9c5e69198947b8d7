from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_login_id(db: Session, email: str):

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.email == email))

    login = query.first()

    login = (
        (login.to_dict() if hasattr(login, "to_dict") else vars(login))
        if login
        else login
    )

    bs_jwt_payload = {
        "exp": int(
            (
                datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
            ).timestamp()
        ),
        "data": login,
    }

    jwt_secret_keys_login = jwt.encode(
        bs_jwt_payload,
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
        algorithm="HS256",
    )

    res = {
        "login": login,
        "jwt_secret_keys_login": jwt_secret_keys_login,
    }
    return res


async def put_teacher_update(db: Session, raw_data: schemas.PutTeacherUpdate):
    full_name: str = raw_data.full_name
    id: int = raw_data.id

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.id == id))
    update_records = query.first()

    if update_records:
        for key, value in {"full_name": full_name}.items():
            setattr(update_records, key, value)

        db.commit()
        db.refresh(update_records)

        update_records = (
            update_records.to_dict()
            if hasattr(update_records, "to_dict")
            else vars(update_records)
        )
    res = {
        "update_records": update_records,
    }
    return res


async def get_teacher_id(db: Session, id: str, request: Request):
    header_authorization: str = request.headers.get("header-authorization")

    t = aliased(models.Teachers)
    query = db.query(models.Teachers, t)

    query = query.join(t, and_(models.Teachers.id == t.id))

    teacher_all_records = query.first()

    if teacher_all_records:
        s1, s2 = teacher_all_records
        teacher_all_records = {
            "teacher_all_records_1": (
                s1.to_dict() if hasattr(s1, "to_dict") else vars(s1)
            ),
            "teacher_all_records_2": (
                s2.to_dict() if hasattr(s2, "to_dict") else vars(s2)
            ),
        }

    try:
        decode_jwt = jwt.decode(
            header_authorization,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithms=["HS256"],
        )
    except jwt.ExpiredSignatureError:
        decode_jwt = "Token has expired."
    except jwt.InvalidTokenError:
        decode_jwt = "Invalid token."

    res = {
        "teacher_all_records": teacher_all_records,
        "yghtfy": decode_jwt,
    }
    return res


async def delete_delete(db: Session, raw_data: schemas.DeleteDelete, request: Request):
    id: int = raw_data.id

    header_authorization: str = request.headers.get("header-authorization")

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        delete_a_records = record_to_delete.to_dict()
    else:
        delete_a_records = record_to_delete
    res = {
        "delete_a_records": delete_a_records,
    }
    return res


async def get_students_allrecords(db: Session, request: Request):
    header_authorization: str = request.headers.get("header-authorization")

    query = db.query(models.Students)

    oiyjuky = query.all()
    oiyjuky = [new_data.to_dict() for new_data in oiyjuky] if oiyjuky else oiyjuky

    try:
        sfsffdsa = jwt.decode(
            header_authorization,
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
            algorithms=["HS256"],
        )
    except jwt.ExpiredSignatureError:
        sfsffdsa = "Token has expired."
    except jwt.InvalidTokenError:
        sfsffdsa = "Invalid token."

    res = {
        "asdsf": oiyjuky,
        "dvcsd": sfsffdsa,
    }
    return res


async def post_login(db: Session, raw_data: schemas.PostLogin):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Students)
    query = query.filter(
        and_(models.Students.email == email, models.Students.password == password)
    )

    login_record = query.first()

    login_record = (
        (
            login_record.to_dict()
            if hasattr(login_record, "to_dict")
            else vars(login_record)
        )
        if login_record
        else login_record
    )

    bs_jwt_payload = {
        "exp": int(
            (
                datetime.datetime.utcnow() + datetime.timedelta(seconds=100000)
            ).timestamp()
        ),
        "data": login_record,
    }

    jwt_secret_keys_login = jwt.encode(
        bs_jwt_payload,
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30",
        algorithm="HS256",
    )

    res = {
        "login": login_record,
        "jwt_1": jwt_secret_keys_login,
    }
    return res


async def post_file_upload(db: Session, document: UploadFile):

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document.read()

    name = document.filename
    file_path = file_path + "/" + name

    import mimetypes

    document.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    document_url = file_url
    res = {
        "document_url": document_url,
    }
    return res


async def get_join1(db: Session):

    s = aliased(models.School)
    query = db.query(models.Students, s)

    query = query.join(s, and_(models.Students.student_id == s.school_id))

    join1 = query.first()

    if join1:
        s1, s2 = join1
        join1 = {
            "join1_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
            "join1_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
        }

    res = {
        "join1": join1,
    }
    return res


async def get_join2(db: Session, full_name: str, email: str):

    s = aliased(models.School)
    query = db.query(models.Students, s)

    query = query.join(
        s, and_(models.Students.full_name == full_name, models.Students.email == email)
    )

    join2 = query.first()

    if join2:
        s1, s2 = join2
        join2 = {
            "join2_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
            "join2_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
        }

    res = {
        "join2": join2,
    }
    return res


async def post_file_upload2(db: Session, document1: UploadFile, request: Request):
    header_authorization: str = request.headers.get("header-authorization")

    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        "s3",
        aws_access_key_id="AKIATET5D5CPSTHVVX25",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1",
    )

    # Read file content
    file_content = await document1.read()

    name = document1.filename
    file_path = file_path + "/" + name

    import mimetypes

    document1.file.seek(0)

    content_type = mimetypes.guess_type(name)[0] or "application/octet-stream"
    s3_client.upload_fileobj(
        document1.file, bucket_name, name, ExtraArgs={"ContentType": content_type}
    )

    file_type = Path(document1.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    wfegdrtfyjgk = file_url
    res = {
        "sdfgdh": wfegdrtfyjgk,
    }
    return res


async def post_exam(db: Session, raw_data: schemas.PostExam):
    exam_name: str = raw_data.exam_name
    total_marks: int = raw_data.total_marks

    record_to_be_added = {"exam_name": exam_name, "total_marks": total_marks}
    new_exams = models.Exams(**record_to_be_added)
    db.add(new_exams)
    db.commit()
    db.refresh(new_exams)
    add_a_record = new_exams.to_dict()

    try:
        thislist = ["apple", "banana", "cherry"]
        print(len(thislist))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    teacher_list = []  # Creating new list

    # Add element to the list 'teacher_list'
    teacher_list.insert(0, exam_name)

    try:
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

    # Add element to the list 'thislist'
    thislist.insert(0, exam_name)
    res = {
        "add_a_records": add_a_record,
        "list": thislist,
        "vnvb": teacher_list,
    }
    return res


async def post_teachers(db: Session, raw_data: schemas.PostTeachers):
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    subject: str = raw_data.subject
    phone_number: str = raw_data.phone_number
    school_id: int = raw_data.school_id
    id: int = raw_data.id

    record_to_be_added = {
        "id": id,
        "email": email,
        "subject": subject,
        "full_name": full_name,
        "school_id": school_id,
        "phone_number": phone_number,
    }
    new_teachers = models.Teachers(**record_to_be_added)
    db.add(new_teachers)
    db.commit()
    db.refresh(new_teachers)
    add_A_records = new_teachers.to_dict()

    test = []  # Creating new list

    # Add element to the list 'test'
    test.insert(0, test)
    res = {
        "add_a_records": add_A_records,
    }
    return res
