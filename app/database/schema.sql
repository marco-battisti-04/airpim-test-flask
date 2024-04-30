DROP TABLE IF EXISTS persona;
DROP TABLE IF EXISTS test;

CREATE TABLE persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nome VARCHAR(255) NOT NULL,
    cognome VARCHAR(255) NOT NULL
);

CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL
);

INSERT INTO persona (nome, cognome) VALUES
    ('John', 'Doe'),
    ('Jane', 'Doe'),
    ('Riccardo', 'Tognetti'),
    ('Leonardo', 'Brugnara');

INSERT INTO test (name, surname) VALUES
    ('John', 'Doe'),
    ('Jane', 'Doe'),
    ('Riccardo', 'Tognetti'),
    ('Leonardo', 'Brugnara')