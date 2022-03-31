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

    @classmethod
    def get_order_user_info(cls, order_id: str):
        cls.get_conn_cur()

        query = """
            SELECT u.email, o.order_date
            FROM users u
            JOIN orders o
                ON u.user_id = o.customer_id
            WHERE o.order_id = %s;
        """

        cls.cur.execute(query, (order_id,))

        result = cls.cur.fetchone()

        cls.commit_and_close(commit=False)

        return result

    @classmethod
    def get_order_products(cls, order_id: str):
        cls.get_conn_cur()

        query = """
            SELECT
                p.product_id, p.name,
                op.sale_value
            FROM orders o
            JOIN orders_products op
                ON o.order_id = op.order_id
            JOIN products p
                ON p.product_id = op.product_id
            WHERE o.order_id = %s;
        """
        cls.cur.execute(query, [order_id])

        products = cls.cur.fetchall()

        cls.commit_and_close(commit=False)

        return products
