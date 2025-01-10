document.getElementById("changeUrlButton").addEventListener("click", () => {
  // Récupérer l'URL actuelle
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
          // Redirige la page actuelle vers l'URL modifiée
          window.location.href = `${url}`;
          console.log(url)
        },
        args: [currentUrl], // Passe l'URL actuelle comme argument
      });
    } else {
      console.error("Aucun onglet actif trouvé.");
    }
  });
});

document.getElementById("fillFormButton").addEventListener("click", () => {
  console.log("hello world");
  //let listElements = document.querySelectorAll("#mexc_contract_v_open_position .ant-input");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        const currentTab = tabs[0];
        const currentUrl = currentTab.url;
  
        // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
          const listElements = document.querySelectorAll("#mexc_contract_v_open_position .ant-input");
          console.log("listElements:", listElements);
          element=listElements[0];
          console.log("listElements:", listElements);
          console.log("Elements:", element);
          
          if (!element){
              alert("Aucun élément avec la classe 'maClasse' trouvé dans l'élément avec ID 'monId'.");
          }
          else{
              //element.value="9495";
              element.click();
              element.value="98";

              // Simuler un événement 'input' pour indiquer que la valeur a changé
              const inputEvent = new Event("input", { bubbles: true });
              element.dispatchEvent(inputEvent);

              // Optionnel : Simuler un événement 'change' si nécessaire
              const changeEvent = new Event("change", { bubbles: true });
              element.dispatchEvent(changeEvent);
      
              alert("Texte inséré (enfin normalement)");
          }
      }
      });
  }
  });     
});

document.getElementById("sendRequest").addEventListener("click", async () => {
  const url = "https://98e9-83-202-127-170.ngrok-free.app/alert";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
  console.log("1");
    if (!response.ok) {
      throw new Error(`Erreur HTTP : ${response.status}`);
    }
    const data = await response.json();
    console.log("Réponse :", data);
    process_alert(data)
  } catch (error) {
    console.error("Erreur :", error);
    alert("Erreur lors de la requête : " + error.message);
  }
});

document.getElementById("clickButton").addEventListener("click", () => {
  console.log("hello world");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        const currentTab = tabs[0];
        const currentUrl = currentTab.url;
  
        // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
          const listElements = document.querySelectorAll(".component_longBtn__BBkFR");
          element=listElements[0];
          
          if (!element){
              alert("Aucun élément avec la classe 'maClasse' trouvé dans l'élément avec ID 'monId'.");
          }
          else{
              element.click();

              // Optionnel : Simuler un événement 'change' si nécessaire
              const changeEvent = new Event("change", { bubbles: true });
              element.dispatchEvent(changeEvent);
      
              alert("Button cliqué");
          }
      }
      });
  }
  });     
});

async function process_alert(alerte){
  if(alerte["strategies"].length > 0){
    for (const element of alerte["strategies"]) {
      const nomActif = element["actif"].split("USDT")[0];
      console.log(nomActif);
      await attendre(10000);
      change_url(nomActif);
      await attendre(8000);
      buy_long(0);
      delete_alert(element);
       // Attente de 5 secondes avant de passer à l'élément suivant
    }
  }
}

function change_url(actif){
  // Récupérer l'URL actuelle
  console.log("test ?");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      console.log("test");

      // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (newActif) => {
          // Redirige la page actuelle vers l'URL modifiée
          console.log(newActif);
          window.location.href = `https://futures.mexc.com/fr-FR/exchange/` + newActif + "_USDT?type=linear_swap";
          console.log(`https://futures.mexc.com/fr-FR/exchange/` + newActif + "_USDT?type=linear_swap");
        },
        args: [actif], // Passe l'URL actuelle comme argument
      });
    } else {
      console.error("Aucun onglet actif trouvé.");
    }
  });
}

async function delete_alert(alerte_to_delete){
  const url = "https://98e9-83-202-127-170.ngrok-free.app/delete_alert";
  const data = {
    action : "delete",
    alerte : alerte_to_delete
  };
  try {
    const response = await fetch(url, {
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

function click_button(class_component, numero_component){
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour modifier l'URL de la page
    chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
        const listElements = document.querySelectorAll(class_component);
        element=listElements[numero_component];
        
        if (!element){
            alert("Aucun élément avec la classe 'maClasse' trouvé dans l'élément avec ID 'monId'.");
        }
        else{
            element.click();

            // Optionnel : Simuler un événement 'change' si nécessaire
            const changeEvent = new Event("change", { bubbles: true });
            element.dispatchEvent(changeEvent);
    
            alert("Button cliqué");
        }
      }
      });
  }
  });
}

function fillButton(class_component, numero_component, value) {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour modifier l'URL de la page
    chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
        const listElements = document.querySelectorAll(class_component);
        element=listElements[numero_component];
        
        if (!element){
            alert("Aucun élément avec la classe 'maClasse' trouvé dans l'élément avec ID 'monId'.");
        }
        else{
            element.value=value;

            // Simuler un événement 'input' pour indiquer que la valeur a changé
            const inputEvent = new Event("input", { bubbles: true });
            element.dispatchEvent(inputEvent);

            // Optionnel : Simuler un événement 'change' si nécessaire
            const changeEvent = new Event("change", { bubbles: true });
            element.dispatchEvent(changeEvent);
    
            alert("Texte inséré (enfin normalement)");
        }
      }
      });
    }
    });     
}

async function buy_long(){
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  if(stopLoss > 0){
    click_button(".ant-checkbox-input", 2);
    await attendre(1000);
    click_button(".InputNumberExtend_wrapper__qxkpD", 2);
    await attendre(1000);
    fillButton(".InputNumberExtend_wrapper__qxkpD", 2)
    await attendre(1000);
  }
  click_button(".component_longBtn__BBkFR", 0);
}

async function buy_short(){
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button(".component_shortBtn__s8HK4", 0);
}

function attendre(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
