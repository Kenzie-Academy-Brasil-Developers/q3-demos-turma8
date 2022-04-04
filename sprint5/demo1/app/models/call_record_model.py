from app import db
from sqlalchemy import Column, Integer, String, DateTime


class CallRecord(db.Model):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
