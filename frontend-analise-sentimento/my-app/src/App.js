import React, { useEffect, useState } from 'react';
import './App.css'; // Assumindo que você tem um arquivo CSS para estilização

function App() {
  const [jsonData, setJsonData] = useState([]);

  useEffect(() => {
    fetch('/resultado.json')
      .then(response => response.json())
      .then(data => setJsonData([data])) // Ajustar para armazenar como array
      .catch(error => console.error('Erro ao carregar o JSON:', error));
  }, []);

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
