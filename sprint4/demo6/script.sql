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
    -- customer_id INT NOT NULL REFERENCES users("user_id")
);

-- 1:1 entre orders e invoices
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id 		SERIAL PRIMARY KEY,
    release_date 	DATE NOT NULL,
    invoice_number 	VARCHAR(64) UNIQUE,
    order_id 		INT UNIQUE NOT NULL REFERENCES orders("order_id")
);