from flask import Blueprint
from app.controllers import call_record_controller

bp = Blueprint("call-records", __name__, url_prefix="/call-records")


bp.post("")(call_record_controller.create_call_record)
bp.get("")(call_record_controller.retrieve_call_record)
