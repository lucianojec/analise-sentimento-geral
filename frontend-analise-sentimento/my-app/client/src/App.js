import React, { useState } from 'react';
import './App.css'; // Assumindo que você tem um arquivo CSS para estilização

function App() {
  const [cliente, setCliente] = useState('');
  const [texto, setTexto] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cliente, texto }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Erro ao enviar o texto:', error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div>
          <label>Cliente:</label>
          <input
            type="text"
            value={cliente}
            onChange={(e) => setCliente(e.target.value)}
          />
        </div>
        <div>
          <label>Texto:</label>
          <textarea
            value={texto}
            onChange={(e) => setTexto(e.target.value)}
          />
        </div>
        <button type="submit">Enviar</button>
      </form>
      {response && (
        <div className="response">
          <h2>Classe: {response.classe}</h2>
          <div>
            Sentimentos:
            <ul>
              {Object.entries(response.sentimentos).map(([key, value]) => (
                <li key={key}>{`${key}: ${value}`}</li>
              ))}
            </ul>
          </div>
          <div>
            Contribuições:
            <ul>
              {Object.entries(response.contribuicoes).map(([key, value]) => (
                <li key={key}>{`${key}: ${value}`}</li>
              ))}
            </ul>
          </div>
          <div>
            Razões Possíveis:
            <ul>
              {response.razoes_possiveis.map((razao, i) => (
                <li key={i}>{razao}</li>
              ))}
            </ul>
          </div>
          <p>{response.explicacao_modelo}</p>
        </div>
      )}
    </div>
  );
}

export default App;
