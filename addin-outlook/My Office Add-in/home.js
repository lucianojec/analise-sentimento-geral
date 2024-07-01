Office.onReady(info => {
    if (info.host === Office.HostType.Outlook) {
        document.getElementById("saveEmail").onclick = saveEmail;
    }
});

async function saveEmail() {
    const item = Office.context.mailbox.item;
    const message = await item.body.getAsync(Office.CoercionType.Text);
    const from = item.from.emailAddress;

    const emailData = {
        from: from,
        body: message.value
    };

    // Salvar emailData em um servidor ou localmente
    console.log(emailData);

    // Aqui você pode adicionar uma chamada a uma API para salvar o emailData
    // fetch('http://seu-servidor.com/api/save-email', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(emailData)
    // });
}
