document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('saveEmail');
    saveButton.addEventListener('click', function() {
      const cliente = document.getElementById('cliente').value;
      if (!confirm('Deseja salvar este email?')) {
        return;
      }
  
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { action: 'saveEmail' }, function(response) {
        //   if (!response) {
        //     alert('Nenhuma resposta do conteudo da aba.');
        //     return;
        //   } else 
          {
            let emailData = {
            //   from: response.from,
              body: response.body,
              cliente: cliente
            };
            console.log('Dados do Email:', JSON.stringify(emailData, null, 2));
  
            // Criar um blob com os dados do email em formato JSON
            const blob = new Blob([JSON.stringify(emailData, null, 2)], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
  
            // Criar um link para download
            const a = document.createElement('a');
            a.href = url;
            a.download = 'email_data.txt';
            document.body.appendChild(a);
            a.click();
  
            // Remover o link após o download
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
  
            alert('Arquivo salvo com sucesso!');
          }
        });
      });
    });
  });
  