chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "saveEmail") {
      // Tentar localizar o corpo do email
    //   let emailBody = document.querySelector("div[role='main'] .ii.gt"); // Tente encontrar o corpo do email de forma dinâmica
    //   let emailBody = document.querySelector("//*[@id='UniqueMessageBody_2']/div/div"); // Tente encontrar o corpo do email de forma dinâmica
    //   let emailBody = document.querySelector("//*[contains(@class, 'wide-content-host')]");
      let emailBody = document.querySelector("//*[@role='document']");

    //   if (!emailBody) {
    //     emailBody = document.querySelector("div[role='main'] .a3s.aiL"); // Tente outra abordagem
    //   }
  
      // Tentar localizar o remetente do email
      let senderemailbase = "//*[@id='ItemReadingPaneContainer']/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/span/span/div"
      let senderEmail = document.querySelector(senderemailbase); // Isso pode precisar de ajustes dependendo da estrutura do Outlook
      if (!senderEmail) {
        senderEmail = document.querySelector("span[data-hovercard-id]"); // Tente outra abordagem
      }
  
      if (emailBody && senderEmail) {
        sendResponse({body: emailBody.innerText, from: senderEmail.getAttribute('email') || senderEmail.getAttribute('data-hovercard-id')});
      } else {
        sendResponse({error: "Informações do email não encontradas."});
      }
    }
  });