from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint


class CallRecord(db.Model):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)

    def __repr__(self) -> str:
        return f"{self.id} - [{self.source}] -> [{self.destination}]"

    # CheckConstraint('length("source") = 9', name="regra_check_source")
