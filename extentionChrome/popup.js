document.getElementById("changeUrlButton").addEventListener("click", () => {
  console.log("test ?");

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      console.log("test");

      // Construire la nouvelle URL avec la valeur 'actif'
      const newUrl = "https://futures.mexc.com/fr-FR/exchange/SPELL_USDT?type=linear_swap";
      console.log(newUrl); // Affiche l'URL modifiée

      // Mettre à jour l'URL et forcer un rechargement
      chrome.tabs.update(currentTab.id, { url: newUrl }, () => {
        // Après la mise à jour de l'URL, forcer un rechargement de la page
        console.log("reload " + newUrl);
        //chrome.tabs.reload(currentTab.id);
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

document.getElementById("hoverElement").addEventListener("click", () => {
  console.log("hello world");
  //let listElements = document.querySelectorAll("#mexc_contract_v_open_position .ant-input");
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        const currentTab = tabs[0];
        const currentUrl = currentTab.url;
  
        // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({target: { tabId: currentTab.id },func: (url) => {
        const element = document.querySelector('.ant-col'); // Remplace '.element-cible' par le sélecteur de ton élément
        console.log(element);
        element.click();
        // Simuler l'événement 'mouseenter' (le survol de l'élément)
        const simulateMouseEnter = () => {
          console.log("survol");
            const event = new MouseEvent('mouseenter', {
                bubbles: true,
                cancelable: true,
                view: window
            });
            element.dispatchEvent(event);
        };
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
    // Envoie le json des stratégies à process 
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
          const listElements = document.querySelectorAll(".ant-checkbox-input");
          element=listElements[2];
          
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

// Fonction principale
async function process_alert(alerte){
  if(alerte["strategies"].length > 0){
    // Parcours les alertes
    for (const element of alerte["strategies"]) {
      // Récupère uniquement la mention qui nous intéresse car Trading View envoie l'actif AAVEUSDT.P et MEXC prends AAVE_USDT
      const nomActif = element["actif"].split("USDT")[0];
      console.log(nomActif);
      await attendre(12000);
      // Change l'url
      change_url(nomActif);
      await attendre(8000);
      // Achete au long
      buy_long(10);
      // Supprime l'alerte
      delete_alert(element);
    }
  }
}

function change_url(actif){
  console.log("test ?");

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      console.log("test");

      // Construire la nouvelle URL avec la valeur 'actif'
      const newUrl = `https://futures.mexc.com/fr-FR/exchange/` + actif + "_USDT?type=linear_swap";
      console.log(newUrl); // Affiche l'URL modifiée

      // Mettre à jour l'URL et forcer un rechargement
      chrome.tabs.update(currentTab.id, { url: newUrl }, () => {
        // Après la mise à jour de l'URL, forcer un rechargement de la page
        //chrome.tabs.reload(currentTab.id);
        console.log(newUrl)
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
    chrome.scripting.executeScript({
      target: { tabId: currentTab.id },
      func: (class_component, numero_component) => {
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
    
            console.log("Button cliqué");
        }
      },
      args: [class_component, numero_component]  // Passer les arguments ici
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
    chrome.scripting.executeScript({
      target: { tabId: currentTab.id },
      func: (class_component, numero_component, value) => {
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
    
            console.log("Texte inséré (enfin normalement)");
        }
      },
      args : [class_component, numero_component, value] // Argument à injecter
      });
    }
    });     
}

async function buy_long(stopLoss){
  //Clique sur ouvrir
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button("#mexc_contract_v_open_position .ant-input", 1);
  await attendre(1000);
  fillButton("#mexc_contract_v_open_position .ant-input", 1, 10);
  if(stopLoss > 0){
    console.log("stoploss")
    // Coche la case long Sl
    click_button(".ant-checkbox-input", 1);
    await attendre(1000);
    // Clique sur la case du stoploss
    click_button(".InputNumberExtend_wrapper__qxkpD", 4);
    await attendre(1000);
    // Remplie la case
    fillButton(".InputNumberExtend_wrapper__qxkpD", 4, "0.00004");
    await attendre(1000);
    console.log("achat");
  }
  // Appuie sur open long
  click_button(".component_longBtn__BBkFR", 0);
  console.log("ordre réalisé");
}

async function buy_short(){
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button(".component_shortBtn__s8HK4", 0);
}

function attendre(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

