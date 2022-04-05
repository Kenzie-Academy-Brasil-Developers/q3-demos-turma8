from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime, Date

print(f"{__name__} DB -> {id(db)}")


class CallRecord(db.Model):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(Date)
    end_time = Column(Date)
