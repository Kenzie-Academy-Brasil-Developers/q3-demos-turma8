SELECT * FROM tabela_teste;

DROP TABLE tabela_teste;

SELECT * FROM tabela_teste;

CREATE TABLE tabela_teste(
	name VARCHAR(50)
);

DROP TABLE IF EXISTS tabela_teste;

CREATE TABLE tabela_teste(
	name VARCHAR(50)
);


-- Comentario single-line
/*
 * Comentario multi line
 *
 */

CREATE TABLE IF NOT EXISTS tabela_teste(
	name VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS users(
	id BIGSERIAL PRIMARY KEY,
	"name" VARCHAR(30) NOT NULL UNIQUE,
	birth_date DATE NOT NULL,
	created_at TIMESTAMPTZ DEFAULT NOW(),
	"height" DECIMAL,
	"quarter" VARCHAR(2)
);

INSERT INTO
	users ("name", birth_date, "height", "quarter")
VALUES
	('Chrystian', '1993-03-03', 1.79, 'Q3'),
	('Aroldo', '1982-10-23', 1.59, 'Q0'),
	('Joana', '1995-03-17', 1.80, 'M3');

SELECT
	*
FROM
	users
WHERE
	"height" > 1.60;

SELECT
	*
FROM
	users
WHERE
	"height" > 1.60
	AND "quarter" = 'Q3';

SELECT
	*
FROM
	users
WHERE
	"height" > 1.60
	AND "quarter" LIKE '%3';

SELECT
	*
FROM
	users
WHERE
	"height" > 1.60
	AND "quarter" LIKE '%Q%';

SELECT
	*
FROM
	users
WHERE
	"height" > 1.60
	AND "quarter" ILIKE '%q%';


SELECT
	"name", birth_date
FROM
	users;

SELECT
	"name" NOME2, birth_date
FROM
	users;

SELECT
	"name", AGE(birth_date) minha_coluna_age
FROM
	users;
