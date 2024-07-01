-- Tabela de Clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Tabela de Analisys
CREATE TABLE analisys (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    classe VARCHAR(50),
    contribuicoes JSONB,
    razoes_possiveis JSONB,
    explicacao_modelo TEXT,
    data_insercao TIMESTAMP
);

-- Tabela de Sentimentos
CREATE TABLE sentimentos (
    id SERIAL PRIMARY KEY,
    analisys_id INT REFERENCES analisys(id),
    tipo VARCHAR(50),
    valor INT
);
