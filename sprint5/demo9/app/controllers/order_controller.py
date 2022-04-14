from http import HTTPStatus

from sqlalchemy.orm import Session, Query
from flask import jsonify, url_for
from app.exc.generic_exc import IdNotFoundError
from app.models.order_model import Order
from app.models.order_product_model import OrderProduct
from app.models.product_model import Product
from app.services.query_service import get_by_id
from ipdb import set_trace
from app.configs.database import db
from dataclasses import asdict


def retrieve_by_id(order_id: int):
    try:
        order = get_by_id(Order, order_id)
    except IdNotFoundError:
        return {"detail": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_order = {"products": url_for(".order_products", order_id=order_id)}

    print(f"{serialized_order}")

    print(f"{order.__dict__}")

    serialized_order.update(asdict(order))
    # set_trace()

    return jsonify(serialized_order), HTTPStatus.OK


def order_products(order_id: int):
    """
    SELECT
        p.product_id, p."name",
        op.sale_value
    FROM orders o
    JOIN orders_products op
        ON o.order_id = op.order_id
    JOIN products p
        ON p.product_id = op.product_id
    WHERE o.order_id = 2;
    """
    session: Session = db.session

    query: Query = (
        session.query(Product.product_id, Product.name, OrderProduct.sale_value)
        .select_from(Order)
        .join(OrderProduct)
        .join(Product)
        .filter(Order.order_id == order_id)
        .all()
    )

    print(f"{type(query[0])=}")

    # Cada item da lista é um Row object
    products = [product._asdict() for product in query]

    return jsonify(products), HTTPStatus.OK
