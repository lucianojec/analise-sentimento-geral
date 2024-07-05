import React, { useState } from 'react';
import './App.css'; // Assumindo que você tem um arquivo CSS para estilização
import Modal from 'react-modal';

Modal.setAppElement('#root');

function App() {
  const [cliente, setCliente] = useState('');
  const [email, setEmail] = useState('');
  const [texto, setTexto] = useState('');
  const [response, setResponse] = useState(null);
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cliente, email, texto }),
      });
      const data = await res.json();
      setResponse(data);
      setModalIsOpen(true);
    } catch (error) {
      console.error('Erro ao enviar o texto:', error);
    }
  };

  const handleSave = async () => {
    try {
      const res = await fetch('http://localhost:5000/api/save', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(response),
      });
      const data = await res.json();
      if (data.success) {
        alert('Dados salvos com sucesso!');
      } else {
        alert('Erro ao salvar os dados');
      }
      setModalIsOpen(false);
    } catch (error) {
      console.error('Erro ao salvar os dados:', error);
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
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={() => setModalIsOpen(false)}
          contentLabel="Resultado da Análise"
        >
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
          <button onClick={handleSave}>Gravar no Banco</button>
          <button onClick={() => setModalIsOpen(false)}>Fechar</button>
        </Modal>
      )}
    </div>
  );
}

export default App;
