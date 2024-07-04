const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch');
const { Client } = require('pg');

const app = express();
const port = 5000;

app.use(bodyParser.json());

const pgClient = new Client({
  user: 'postgres',
  host: 'localhost',
  database: 'datafeelings',
  password: 'admin',
  port: 5432,
});

pgClient.connect();

app.post('/api/analyze', async (req, res) => {
  const { cliente, texto } = req.body;

  const comando = `
    {
      "prompt": "Analyze the following text and provide sentiment analysis, contributions, possible reasons, and model explanation.",
      "input": "${texto}"
    }
  `;

  try {
    const geminiResponse = await fetch('https://gemini-api-url.com/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer YOUR_GEMINI_API_KEY`,
      },
      body: JSON.stringify({ prompt: comando }),
    });

    const geminiData = await geminiResponse.json();

    const insertQuery = `
      INSERT INTO analisys (cliente_id, classe, sentimento, contribuicoes, razoes_possiveis, explicacao_modelo, data_insercao)
      VALUES (
        (SELECT id FROM clientes WHERE nome = $1),
        $2,
        $3,
        $4,
        $5,
        $6,
        NOW()
      ) RETURNING *;
    `;

    const values = [
      cliente,
      geminiData.classe,
      JSON.stringify(geminiData.sentimentos),
      JSON.stringify(geminiData.contribuicoes),
      JSON.stringify(geminiData.razoes_possiveis),
      geminiData.explicacao_modelo,
    ];

    const dbResponse = await pgClient.query(insertQuery, values);
    res.status(200).json(dbResponse.rows[0]);
  } catch (error) {
    console.error('Erro ao processar o texto:', error);
    res.status(500).json({ error: 'Erro ao processar o texto' });
  }
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
