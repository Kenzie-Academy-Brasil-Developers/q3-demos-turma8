DROP TABLE IF EXISTS users, orders, invoices;

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
    -- FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- 1:1 entre invoices e orders
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id 		SERIAL PRIMARY KEY,
    release_date 	DATE NOT NULL,
    invoice_number 	VARCHAR(64) UNIQUE,
    order_id 		INT UNIQUE NOT NULL REFERENCES orders("order_id")
);

-- Adicionando registros
INSERT INTO users
    (email, birthdate, children, married, account_balance)
VALUES 
	('roberto@email.com', '1995-12-27', 3, TRUE, 7500),
	('maria@email.com', '1990-06-14', 0, FALSE, 15000),
	('carlos@email.com', '1980-12-11', 2, TRUE, 10000),
	('joao@email.com', '2003-11-18', 0, FALSE, 0),
	('renata@email.com', '1999-01-04', 0, FALSE, 18000);
	
INSERT INTO orders
    (customer_id, order_date)
VALUES 
	(1, '2021-11-08 05:28:15'),
    (2, '2021-11-13 03:53:54'), 
    (3, '2021-11-16 12:55:35'), 
    (3, '2021-11-20 20:02:13');
    
INSERT INTO invoices
    (release_date, invoice_number, order_id)
VALUES
    ('2021-11-08 05:39:15', '32752374698326546572342', 1),
    ('2021-11-13 04:03:54', '43634657348657346523441', 2),
    ('2021-11-16 13:15:35', '09345743587970123575483', 3),
    ('2021-11-20 20:31:02', '00534242758346254154238', 4);

-- Fere a regra de unico da referencia para order_id
INSERT INTO invoices
    (release_date, invoice_number, order_id)
VALUES
    ('2021-11-08 05:39:15', '32752374698326546572340', 1);

   
-- Integridade Referencial   
DELETE FROM users WHERE user_id = 3;
 

ALTER TABLE orders
DROP CONSTRAINT "orders_customer_id_fkey";


ALTER TABLE orders
ADD CONSTRAINT "orders_users_fk"
FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE CASCADE

   
DELETE FROM users WHERE user_id = 3;


ALTER TABLE invoices
DROP CONSTRAINT "invoices_order_id_fkey";

ALTER TABLE invoices
ADD CONSTRAINT "invoices_order_fk"
FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
   
DELETE FROM users WHERE user_id = 3;


-- SELECTS COM JOIN
SELECT * FROM users;

SELECT i.invoice_id, i.release_date, o.customer_id
FROM invoices i
JOIN orders o
	ON i.order_id = o.order_id;


SELECT *
FROM orders o
JOIN invoices i
	ON i.order_id = o.order_id
WHERE o.order_id = 3;


SELECT *
FROM invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON o.customer_id = u.user_id;

SELECT *
FROM invoices i
JOIN
	orders o
	ON i.order_id = o.order_id
JOIN
	users u
	ON o.customer_id = u.user_id
WHERE
	u.user_id = 3;

-- BETWEEN
SELECT *
FROM users
WHERE account_balance >= 7500 AND account_balance <= 10000;

SELECT *
FROM users
WHERE account_balance BETWEEN 7500 AND 15000;

-- IN
SELECT *
FROM users
WHERE children = 0 OR children = 2;

SELECT *
FROM users
WHERE children IN (0, 3);


-- Sub query
SELECT min(children) FROM users;
SELECT max(children) FROM users;

SELECT *
FROM users
WHERE children IN (
	(SELECT min(children) FROM users),
	(SELECT max(children) FROM users)
);


SELECT avg(account_balance) FROM users;

SELECT user_id, email, account_balance
FROM users
WHERE account_balance > (SELECT avg(account_balance) FROM users);
