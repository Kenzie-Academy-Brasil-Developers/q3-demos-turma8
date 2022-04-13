from app.configs.database import db
from sqlalchemy.orm.session import Session

from app.exc import IdNotFoundError


def get_by_id(model, id):
    session: Session = db.session

    resource = session.query(model).get(id)

    if not resource:
        raise IdNotFoundError

    return resource
