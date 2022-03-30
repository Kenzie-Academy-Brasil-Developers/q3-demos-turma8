from app.models import DatabaseConnector


class Order(DatabaseConnector):
    table_name = "orders"
    order_columns = ["order_id", "order_date", "customer_id"]

    def __init__(self, **kwargs):
        self.order_id = kwargs["order_id"]
        self.order_date = kwargs["order_date"]
        self.customer_id = kwargs["customer_id"]

    @classmethod
    def select_all(cls):
        return super().select_all(cls.table_name)

    @classmethod
    def serialize(cls, values: tuple):
        return super().serialize(values, cls.order_columns)
