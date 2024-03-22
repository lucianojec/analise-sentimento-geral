-- Inserir dados do cliente Yaman na tabela clientes
INSERT INTO clientes (nome, email, classe, sentimentos, razoes_possiveis, explicacao_modelo)
VALUES (
    'Yaman',
    'yaman@example.com',
    'neutra',
    '{"esperança": "50", "frustração": "50"}',
    '["expectativa de melhora não foi atendida.", "não conseguir atingir a meta estabelecida."]',
    'a frase expressa sentimentos positivos (esperança) e sentimentos negativos (frustração) em igual intensidade, que provavelmente são resultado da mistura de sentimentos de otimismo pela melhora nos últimos dias e de decepção por não ter atingido a meta. as palavras-chave "bom dia" e "2 dias bons depois do plano" contribuem para o sentimento de esperança, enquanto as palavras-chave "voltamos a não atingir a meta" e "o que tá faltando" contribuem para o sentimento de frustração. ambas as contribuições estão presentes na frase em igual intensidade, resultando num sentimento neutro.'
) RETURNING id;

-- Obter o ID do cliente Yaman
-- O comando RETURNING id retorna o ID gerado automaticamente para o cliente inserido
-- Você precisará desse ID para associar as contribuições ao cliente específico

-- Inserir contribuições do cliente Yaman na tabela contribuicoes
INSERT INTO contribuicoes (cliente_id, contribuicao, sentimento_associado)
VALUES
    -- Contribuições e sentimentos associados
    (ID_DO_CLIENTE_YAMAN, 'bom dia', 'esperança'),
    (ID_DO_CLIENTE_YAMAN, '2 dias bons depois do plano', 'esperança'),
    (ID_DO_CLIENTE_YAMAN, 'voltamos a não atingir a meta', 'frustração'),
    (ID_DO_CLIENTE_YAMAN, 'o que tá faltando', 'frustração');
