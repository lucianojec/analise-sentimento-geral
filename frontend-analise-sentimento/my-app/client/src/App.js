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
            // value={cliente}
            value="BMG"
            onChange={(e) => setCliente(e.target.value)}
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            // value={email}
            value="testeyaman@bmg.com.br"
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label>Texto:</label>
          <textarea
            // value={texto}
            value="Olá, Ricardo, tudo bem?Conforme alinhado em reunião, ficou definido que no Q1 – 2025 iremos atuar na entrega dos itens listados abaixo.Solicitamos o seu de acordo para que possamos eguir com esse planejamento.1.	(M) RITM0059335 - Oficio SUSEP - Nome Social - Demanda Regulatório - Forte para Q1-2025a.	O tamanho dessa melhoria foi definido como M (>1 mês e <= 2 meses) erá necessário incluir o campo Nome Social para que seja coletado no Direct e armazenado no AUTBANK para que seja possível gerar as propostas de Auto Integrado e Proteção Financeira com sse ampo, além de encaminhar o Nome Social para as seguradoras (Mitsui, Tokio e Cardif).2.	(GG) SEGURO FRANQUIA - Segona.	O tamanho do projeto foi classificado como GG (> 3 meses – não cabe um nico ciclo). No Q1-2025 iremos entregar o desenvolvimento referente ao Segon e em paralelo iremos continuar a análise dos demais pontos de desenvolvimento para que seja possível concluir a stimativa do projeto como um todo.b.	Segue anexo o Mapa Mental do projeto.Obrigado,Marciu"
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
