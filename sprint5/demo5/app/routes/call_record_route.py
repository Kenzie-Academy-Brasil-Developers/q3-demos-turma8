from flask import Blueprint
from app.controllers import call_record_controller

bp = Blueprint("call-records", __name__, url_prefix="/call-records")


bp.post("")(call_record_controller.create_call_record)
bp.get("/<int:call_id>")(call_record_controller.retrive_call_by_id)
bp.get("")(call_record_controller.retrieve_call_record)
bp.get("/some_columns")(call_record_controller.retrive_some_columns)
bp.get("/group_by")(call_record_controller.retrieve_group_by)
bp.patch("/<int:call_id>")(call_record_controller.update_call_by_id)
bp.delete("/<int:call_id>")(call_record_controller.delete_call_by_id)
