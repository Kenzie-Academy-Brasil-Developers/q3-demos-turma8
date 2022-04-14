-- users
INSERT INTO users
    (email, birthdate, children, married, account_balance)
VALUES
	('roberto@email.com', '1995-12-27', 3, TRUE, 7500),
	('maria@email.com', '1990-06-14', 0, FALSE, 15000),
	('carlos@email.com', '1980-12-11', 2, TRUE, 10000),
	('joao@email.com', '2003-11-18', 0, FALSE, 0),
	('renata@email.com', '1999-01-04', 0, FALSE, 18000),
	('wesley@email.com', '2007-06-06', 0, FALSE, 15),
	('ana@email.com', '1979-10-11', 2, TRUE, 80000),
	('ricardo@email.com', '1989-12-13', 2, TRUE, 20000);

-- orders
INSERT INTO
	orders (customer_id, order_date)
VALUES
	(1, '2021-11-08 05:28:15'), -- ORDER associada ao USER de id 1
    (2, '2021-11-13 03:53:54'), -- ORDER associada ao USER de id 2
	(3, '2021-11-16 12:55:35'), -- ORDER associada ao USER de id 3
	(3, '2021-11-20 20:02:13'); -- ORDER associada ao USER de id 3

-- invoices
INSERT INTO invoices
    (release_time, invoice_number, order_id)
VALUES
    ('2021-11-08 05:39:15', '32752374698326546572342', 1),
    ('2021-11-13 04:03:54', '43634657348657346523441', 2),
    ('2021-11-16 13:15:35', '09345743587970123575483', 3),
    ('2021-11-20 20:31:02', '00534242758346254154238', 4);

-- products
INSERT INTO products
    ("name", price)
VALUES
	('Fogão', 800),
    ('Geladeira', 2000),
    ('Televisão', 3200),
    ('Forno', 700),
    ('Panelas', 150);

-- orders_products
INSERT INTO
	orders_products (order_id, product_id, sale_value)
VALUES
	(1, 1, 750.0),
    (2, 2, 1500.50),
    (2, 3, 3000.0),
    (3, 4, 799.0),
    (3, 1, 850.50),
    (4, 1, 800.0);