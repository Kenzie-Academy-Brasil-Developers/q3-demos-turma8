DROP TABLE IF EXISTS users, orders, invoices, products, orders_products, orders;

CREATE TABLE IF NOT EXISTS users (
    user_id       	SERIAL PRIMARY KEY,
    email           VARCHAR(64) UNIQUE NOT NULL,
    birthdate       DATE NOT NULL,
    children        INT NOT NULL,
    married         BOOLEAN NOT NULL,
    account_balance REAL NOT NULL
);

-- 1:N entre users e orders
CREATE TABLE IF NOT EXISTS orders (
    order_id        SERIAL PRIMARY KEY,
    order_date      TIMESTAMP NOT NULL,
    customer_id     INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES users("user_id")
);

-- 1:1 entre invoices e orders
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id 		SERIAL PRIMARY KEY,
    release_date 	DATE NOT NULL,
    invoice_number 	VARCHAR(64) UNIQUE,
    order_id 		INT UNIQUE NOT NULL REFERENCES orders("order_id")
);

CREATE TABLE IF NOT EXISTS products (
	product_id 	SERIAL 		PRIMARY KEY,
	"name" 		VARCHAR(50) NOT NULL,
	price 		REAL 		NOT NULL
);

CREATE TABLE IF NOT EXISTS orders_products(
	orders_products_id 	SERIAL PRIMARY KEY,
	sale_value 			REAL,
	order_id 			INT,
	product_id 			INT,
	FOREIGN KEY (order_id) 	 REFERENCES orders("order_id"),
	FOREIGN KEY (product_id) REFERENCES products("product_id")
);


-- Adicionando registros em users
INSERT INTO users
    (email, birthdate, children, married, account_balance)
VALUES 
	('roberto@email.com', '1995-12-27', 3, TRUE, 7500),
	('maria@email.com', '1990-06-14', 0, FALSE, 15000),
	('carlos@email.com', '1980-12-11', 2, TRUE, 10000),
	('joao@email.com', '2003-11-18', 0, FALSE, 0),
	('renata@email.com', '1999-01-04', 0, FALSE, 18000);

-- Adicionando registros em orders
INSERT INTO orders
    (customer_id, order_date)
VALUES 
	(1, '2021-11-08 05:28:15'),
    (2, '2021-11-13 03:53:54'), 
    (3, '2021-11-16 12:55:35'), 
    (3, '2021-11-20 20:02:13');

-- Adicionando registros em invoices
INSERT INTO invoices
    (release_date, invoice_number, order_id)
VALUES
    ('2021-11-08 05:39:15', '32752374698326546572342', 1),
    ('2021-11-13 04:03:54', '43634657348657346523441', 2),
    ('2021-11-16 13:15:35', '09345743587970123575483', 3),
    ('2021-11-20 20:31:02', '00534242758346254154238', 4);

INSERT INTO products
	("name", price)
VALUES
	('Fogão', 750.50),
	('Geladeira', 1000.1),
	('Televisão', 2000),
	('Sofá', 550);

INSERT INTO orders_products  
   (order_id, product_id, sale_value)
VALUES
	(1, 1, 900),
	(2, 2, 1500.50),
	(2, 3, 2900),
	(3, 4, 799),
	(3, 1, 800),
	(4, 1, 1000)
   
 
SELECT *
FROM orders o
JOIN orders_products op
	ON o.order_id = op.order_id
JOIN products p
	ON op.product_id = p.product_id;

SELECT o.order_id, p."name", p.price, op.sale_value 
FROM orders o
JOIN orders_products op
	ON o.order_id = op.order_id
JOIN products p
	ON op.product_id = p.product_id;


SELECT o.order_id, p."name", p.price, op.sale_value 
FROM orders o
JOIN orders_products op
	ON o.order_id = op.order_id
JOIN products p
	ON op.product_id = p.product_id
WHERE
	o.order_id = 3;


SELECT *
FROM invoices i
JOIN orders o
	ON i.order_id = o.order_id
JOIN users u 
	ON u.user_id = o.customer_id
JOIN
	orders_products op
	ON op.order_id = o.order_id
JOIN products p
	ON p.product_id = op.product_id;
	
	
SELECT 
	u.user_id, u.email,
	o.order_id, o.order_date,
	i.invoice_number, i.release_date,
	op.sale_value,
	p."name"
FROM invoices i
JOIN orders o
	ON i.order_id = o.order_id
JOIN users u 
	ON u.user_id = o.customer_id
JOIN
	orders_products op
	ON op.order_id = o.order_id
JOIN products p
	ON p.product_id = op.product_id;
	
SELECT 
	u.user_id, u.email,
	o.order_id, o.order_date,
	i.invoice_number, i.release_date,
	op.sale_value,
	p."name"
FROM invoices i
JOIN orders o
	ON i.order_id = o.order_id
JOIN users u 
	ON u.user_id = o.customer_id
JOIN
	orders_products op
	ON op.order_id = o.order_id
JOIN products p
	ON p.product_id = op.product_id
WHERE
	u.user_id = 1;

SELECT u.email, COUNT(*)
FROM users u
JOIN orders o
	ON o.customer_id = u.user_id
JOIN invoices i
	ON i.order_id = o.order_id
GROUP BY
	u.email;