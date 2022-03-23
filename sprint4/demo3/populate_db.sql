DROP TABLE IF EXISTS users, products;

-- TABLE users
CREATE TABLE IF NOT EXISTS users (
    id              SERIAL          PRIMARY KEY,
    email           VARCHAR(255)    UNIQUE NOT NULL,
    birthdate       DATE            NOT NULL,
    children        INT             NOT NULL,
    married         BOOLEAN         NOT NULL,
    account_balance REAL            NOT NULL
);

-- INSERINDO DADOS
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

-- CRIANDO TABELA PRODUCTS
CREATE TABLE IF NOT EXISTS products (
    id      SERIAL      PRIMARY KEY,
    "name"  VARCHAR(50) NOT NULL,
    price   REAL        NOT NULL
);

-- INSERINDO DADOS
INSERT INTO products
    ("name", price)
VALUES
	('Fogão', 800),
    ('Geladeira', 2000),
    ('Televisão', 3200),
    ('Forno', 700),
    ('Panelas', 150);

