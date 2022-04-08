from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass


@dataclass
class CallRecord(db.Model):
    id: bool
    source: str
    destination: str
    start_time: str
    end_time: str

    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)

    def __repr__(self) -> str:
        return f"{self.id} - [{self.source}] -> [{self.destination}]"
