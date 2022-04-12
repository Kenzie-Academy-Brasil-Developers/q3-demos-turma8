from dataclasses import dataclass
from datetime import datetime as dt

from app.configs.database import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref


@dataclass
class Invoice(db.Model):
    invoice_id: int
    invoice_number: str
    release_time: str
    order: str

    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True)
    invoice_number = Column(String(63), unique=True)
    release_time = Column(DateTime, default=dt.now())

    order_id = Column(Integer, ForeignKey("orders.order_id"), unique=True)

    order = relationship("Order", backref=backref("invoice", uselist=False))
