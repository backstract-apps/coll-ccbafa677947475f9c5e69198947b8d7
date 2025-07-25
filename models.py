from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class School(Base):
    __tablename__ = 'school'
    school_id = Column(Integer, primary_key=True, autoincrement=True)
    school_name = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    state = Column(String, primary_key=False)
    pincode = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String, primary_key=False)
    subject_code = Column(String, primary_key=False)
    school_id = Column(Integer, primary_key=False)
    created_at = Column(Time, primary_key=False)


class Exams(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True, autoincrement=True)
    exam_name = Column(String, primary_key=False)
    total_marks = Column(Integer, primary_key=False)


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    subject = Column(String, primary_key=False)
    phone_number = Column(String, primary_key=False)
    school_id = Column(Integer, primary_key=False)


class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    age = Column(Integer, primary_key=False)
    grade = Column(String, primary_key=False)
    school_id = Column(Integer, primary_key=False)
    enrolled_at = Column(Time, primary_key=False)
    password = Column(String, primary_key=False)


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String, primary_key=False)
    section = Column(String, primary_key=False)
    grade_level = Column(String, primary_key=False)


