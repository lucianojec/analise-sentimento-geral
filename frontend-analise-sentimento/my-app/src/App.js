import React from 'react';
import './App.css'; // Assumindo que você tem um arquivo CSS para estilização

const jsonData = [
  {
    classe: "positivo",
    sentimentos: {
      contentamento: 100
    },
    contribuicoes: {
      boa: "contentamento",
      noite: "contentamento",
      "a todos": "contentamento"
    },
    razoes_possiveis: [
      "boa noite",
      "a todos",
      "expressão educada",
      "expressão de cumprimento"
    ],
    explicacao_modelo: "a frase expressa um sentimento positivo de contentamento..."
    // Conteúdo truncado para brevidade
  },
  // Outros objetos do JSON...
];

function App() {
  return (
    <div className="App">
      {jsonData.map((item, index) => (
        <div key={index} className="item">
          <h2>Classe: {item.classe}</h2>
          <div>
            Sentimentos:
            <ul>
              {Object.entries(item.sentimentos).map(([key, value]) => (
                <li key={key}>{`${key}: ${value}`}</li>
              ))}
            </ul>
          </div>
          <div>
            Contribuições:
            <ul>
              {Object.entries(item.contribuicoes).map(([key, value]) => (
                <li key={key}>{`${key}: ${value}`}</li>
              ))}
            </ul>
          </div>
          <div>
            Razões Possíveis:
            <ul>
              {item.razoes_possiveis.map((razao, i) => (
                <li key={i}>{razao}</li>
              ))}
            </ul>
          </div>
          <p>{item.explicacao_modelo}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
