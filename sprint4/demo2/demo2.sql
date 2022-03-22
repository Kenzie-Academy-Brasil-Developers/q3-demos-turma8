DROP TABLE IF EXISTS estados;

-- uuid

CREATE TABLE IF NOT EXISTS estados(
	id 			BIGSERIAL 		PRIMARY KEY,
	nome 		VARCHAR(30) 	NOT NULL UNIQUE,
	sigla 		VARCHAR			NOT NULL UNIQUE,
	capital 	VARCHAR(50) 	NOT NULL UNIQUE,
	regiao 		VARCHAR(30),
	populacao	DECIMAL,
	"area"		DECIMAL,
	-- CHECK (length(sigla) = 2)
	CONSTRAINT check_sigla_len CHECK (length(sigla) = 2)
);

INSERT INTO estados 
	(nome, sigla, capital, populacao, "area", regiao)
VALUES
	('Santa Catarina', 'SC', 'Florianópolis', 7, 95.1, 'Sul'),
	('Rio Grande do Sul', 'RS', 'Porto Alegre', 11, NULL, 'Sul'),
	('São Paulo', 'SP', 'São Paulo', 44, 248.2, 'Sudeste'),
	('Rio de Janeiro', 'RJ', 'Rio de Janeiro', 16, 43.6, 'Sudeste'),
	('Minas Gerais', 'MG', 'Belo Horizonte', 20.8, NULL, 'Sudeste'), 
	('Bahia', 'BA', 'Salvador', 15, 567.2, 'Nordeste'),
	('Maranhão', 'MA', 'Sao Luis', 6.8, 331, 'Nordeste'),
	('Espirito Santo', 'ES', 'Vitória', NULL, 20.9, 'Sudeste');


SELECT * FROM estados;

SELECT
	nome, capital
FROM 
	estados;

SELECT
	id, nome, capital
FROM
	estados
WHERE
	nome LIKE capital;

SELECT
	id, nome, capital
FROM
	estados
WHERE
	nome LIKE capital
	AND id % 2 <> 0;

-- Ordenação
SELECT * FROM estados ORDER BY sigla;
SELECT * FROM estados ORDER BY sigla ASC;
SELECT * FROM estados ORDER BY sigla DESC;

SELECT * FROM estados ORDER BY sigla;

SELECT * FROM estados ORDER BY sigla LIMIT 2;
SELECT * FROM estados ORDER BY sigla LIMIT 2 OFFSET 2;

-- Agrupar
SELECT regiao, count(*) contador_regiao FROM estados GROUP BY regiao;

SELECT regiao, sum(e."area") FROM estados e GROUP BY regiao;

-- ERRADO
SELECT
	regiao, sum(e."area")
FROM 
	estados e 
GROUP BY regiao 
	WHERE sum(e."area") > 350;

SELECT
	regiao, sum(e."area")
FROM 
	estados e 
GROUP BY regiao 
	HAVING sum(e."area") > 300;


SELECT
	regiao, sum(e."area")
FROM 
	estados e 
GROUP BY regiao 
	HAVING sum(e."area") > 300
ORDER BY sum(e."area") DESC
LIMIT 1;


-- UPDATE
SELECT * FROM estados;

UPDATE
	estados
SET
	populacao = 3.8
WHERE
	sigla = 'ES';

UPDATE
	estados
SET
	"area" = 586
WHERE
	"area" IS NULL
RETURNING *;

UPDATE
	estados
SET
	populacao = 3.8
WHERE
	sigla = 'ES'
RETURNING nome, sigla;


-- Alteração estrutural de uma tabela
ALTER TABLE
	estados
ADD COLUMN
	clinma VARCHAR(20);

ALTER TABLE
	estados
RENAME
	clinma TO clima;

ALTER TABLE
	estados
DROP COLUMN IF EXISTS
	clima;

ALTER TABLE
	estados
DROP COLUMN
	clima;

-- Comando custoso
ALTER TABLE
	estados
ADD COLUMN
	clima VARCHAR(20) DEFAULT 'tropical';

ALTER TABLE
	estados
ALTER COLUMN
	populacao
	SET NOT NULL;

ALTER TABLE
	estados
ALTER COLUMN
	populacao
	TYPE INTEGER
	USING populacao::INTEGER;


-- 

INSERT INTO	estados
	(nome, sigla, capital, populacao, "area", regiao)
VALUES
	('Goiás', 'GO', 'Goiânia', 6, 340, 'Centro Oeste')
RETURNING *;


DELETE FROM estados WHERE id = 10 RETURNING *;


SELECT * FROM estados;

SELECT sum(populacao) FROM estados;

INSERT INTO	estados
	(nome, sigla, capital, populacao, "area", regiao, clima)
VALUES
	('Goiás', 'GO', 'Goiânia', 6, 340, 'Centro Oeste', 'outro clima'),
	('Goiáss', 'Ga', 'Goiânias', 6, 340, 'Centro Oeste', DEFAULT)
RETURNING *;
