-- Criação do banco de dados
CREATE DATABASE datafeelings;

\ c datafeelings;

-- Criação da tabela clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    classe VARCHAR(20) NOT NULL,
    sentimentos JSONB NOT NULL,
    razoes_possiveis JSONB NOT NULL,
    explicacao_modelo TEXT NOT NULL,
    data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela contribuicoes
CREATE TABLE contribuicoes (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id) ON DELETE CASCADE,
    contribuicao TEXT NOT NULL,
    sentimento_associado VARCHAR(20) NOT NULL
);