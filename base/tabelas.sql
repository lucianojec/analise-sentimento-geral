-- Criação da tabela analisys
CREATE TABLE public.analisys (
	id serial4 NOT NULL,
	cliente_id int4 NULL,
	classe varchar(50) NULL,
	sentimento jsonb NULL,
	contribuicoes jsonb NULL,
	razoes_possiveis jsonb NULL,
	explicacao_modelo text NULL,
	data_insercao timestamp NULL,
	email varchar(255) NULL,
	CONSTRAINT analisys_pkey PRIMARY KEY (id)
);

-- Criação da tabela clientes
CREATE TABLE public.clientes (
	id serial4 NOT NULL,
	nome varchar(255) NOT NULL,
	CONSTRAINT clientes_pkey PRIMARY KEY (id)
);

-- Criação da tabela sentimentos
CREATE TABLE public.sentimentos (
	id serial4 NOT NULL,
	analisys_id int4 NULL,
	tipo varchar(50) NULL,
	valor int4 NULL,
	CONSTRAINT sentimentos_pkey PRIMARY KEY (id)
);

-- Chave estrangeira para a tabela sentimentos
ALTER TABLE public.sentimentos ADD CONSTRAINT sentimentos_analisys_id_fkey FOREIGN KEY (analisys_id) REFERENCES public.analisys(id);
