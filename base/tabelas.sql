CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE analisys (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id) ON DELETE CASCADE,
    classe VARCHAR(50),
    sentimento JSONB,
    contribuicoes JSONB,
    razoes_possiveis JSONB,
    explicacao_modelo TEXT
);
