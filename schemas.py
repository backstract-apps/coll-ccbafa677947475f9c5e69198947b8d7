from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class School(BaseModel):
    school_name: str
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadSchool(BaseModel):
    school_name: str
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Subjects(BaseModel):
    subject_name: Optional[str]=None
    subject_code: Optional[str]=None
    school_id: Optional[int]=None
    created_at: Optional[datetime.time]=None


class ReadSubjects(BaseModel):
    subject_name: Optional[str]=None
    subject_code: Optional[str]=None
    school_id: Optional[int]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Exams(BaseModel):
    exam_name: Optional[str]=None
    total_marks: Optional[int]=None


class ReadExams(BaseModel):
    exam_name: Optional[str]=None
    total_marks: Optional[int]=None
    class Config:
        from_attributes = True


class Teachers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    subject: Optional[str]=None
    phone_number: Optional[str]=None
    school_id: Optional[int]=None


class ReadTeachers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    subject: Optional[str]=None
    phone_number: Optional[str]=None
    school_id: Optional[int]=None
    class Config:
        from_attributes = True


class Students(BaseModel):
    full_name: str
    email: str
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None
    password: Optional[str]=None


class ReadStudents(BaseModel):
    full_name: str
    email: str
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None
    password: Optional[str]=None
    class Config:
        from_attributes = True


class Classes(BaseModel):
    class_name: Optional[str]=None
    section: Optional[str]=None
    grade_level: Optional[str]=None


class ReadClasses(BaseModel):
    class_name: Optional[str]=None
    section: Optional[str]=None
    grade_level: Optional[str]=None
    class Config:
        from_attributes = True




class PutTeacherUpdate(BaseModel):
    full_name: str = Field(..., max_length=100)
    id: int = Field(...)

    class Config:
        from_attributes = True



class DeleteDelete(BaseModel):
    id: int = Field(...)

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str = Field(..., max_length=100)

    @field_validator('email')
    def validate_email(cls, value: Optional[str]):
        if value is None:
            if False:
                return value
            else:
                raise ValueError("Field 'email' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]{2,}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field '{schema.key}' does not match regex pattern: {repr(                  schema.regularExpression)}")
        return value
    password: Optional[str]=None

    @field_validator('password')
    def validate_password(cls, value: Optional[str]):
        if value is None:
            if True:
                return value
            else:
                raise ValueError("Field 'password' cannot be None")
        # Ensure re is imported in the generated file
        pattern = r'''^[a-zA-Z0-9!@#$%^&*()_+\-=]{8,64}$'''
        if isinstance(value, str) and not re.match(pattern, value):
            # Use repr() for the regex pattern in the error for clarity
            raise ValueError(f"Field '{schema.key}' does not match regex pattern: {repr(                  schema.regularExpression)}")
        return value

    class Config:
        from_attributes = True



class PostExam(BaseModel):
    exam_name: str = Field(..., max_length=100)
    total_marks: int = Field(...)

    class Config:
        from_attributes = True



class PostTeachers(BaseModel):
    full_name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)
    subject: str = Field(..., max_length=100)
    phone_number: str = Field(..., max_length=100)
    school_id: int = Field(...)
    id: int = Field(...)

    class Config:
        from_attributes = True

