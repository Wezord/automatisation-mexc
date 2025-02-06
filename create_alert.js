const data = {
    'strategy_order_name' : 'moving',
    'type' : 'buy',
    'position' : 'long',
    'stop_loss' : '0',
    'actif' : 'ARUSDT.P',
    'tim' : 'lheure de se brosser les de,ts',
    'alert_message' : 'Entry long'
}

function sendAlert(){
    try {
        const response = fetch("https://a5e3-83-202-127-170.ngrok-free.app/webhook", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        });
        if (!response.ok) {
          throw new Error(`Erreur HTTP : ${response.status}`);
        }
    } catch (error) {
        console.error("Erreur :", error);
    }
}

sendAlert()