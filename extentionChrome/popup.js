const dicStrats = {
  "X3-test": 69356848,
  "Bollinge-Test": 69261661
};
let varStratSelect;

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

/*document.getElementById("hoverElement").addEventListener("click", () => {
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
});*/

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

///////////////////////////////////////////////////
/////Code pour le changement de compte/////////////
///////////////////////////////////////////////////
// Références aux éléments HTML
const selectElement = document.getElementById("choixStrategies");
const resultElement = document.getElementById("choixStratResult");
const formElement = document.getElementById("strategiesForm");

// Remplir la liste déroulante avec les clés du dictionnaire
function populateSelectOptions() {
  for (const key in dicStrats) {
    const option = document.createElement("option");
    option.value = key; // La valeur de l'option sera la clé
    option.textContent = key; // Le texte affiché sera la clé
    selectElement.appendChild(option);
  }
}
function demandeChangementUtilisateur(data) {
  return new Promise((resolve, reject) => {
      chrome.runtime.sendMessage(
          { action: "changeUser",data: data }, // Le message à envoyer
          (response) => {
              if (chrome.runtime.lastError) {
                  reject(chrome.runtime.lastError);
              } else {
                  resolve(response.result);
              }
          }
      );
  });
}

// Gérer la soumission du formulaire
formElement.addEventListener("submit", (event) => {
  event.preventDefault(); // Empêcher le rechargement de la page

  // Récupérer la clé sélectionnée
  const selectedKey = selectElement.value;

  // Trouver la valeur correspondante dans le dictionnaire
  const value = dicStrats[selectedKey];
  varStratSelect=value;

  // Afficher la valeur dans l'élément <p>
  resultElement.textContent = `Valeur sélectionnée : ${value}`;
});

// Initialiser la liste déroulante
populateSelectOptions();

document.getElementById("changeAccount").addEventListener("click", async () => {
  const url = "https://www.mexc.co/fr-FR/user/switch-account";
  const stratSelect = varStratSelect; // Assure-toi que cette variable est définie
  
  //alert("Valeur de stratSelect :"+ stratSelect);
  //attendre(2000);
  demandeChangementUtilisateur(stratSelect);
  // Ouvrir un nouvel ongletC
  chrome.tabs.create({ url: url }, async (tab) => {
    console.log("Nouvel onglet ouvert :", tab);

    // Attendre 10 secondes pour que la page charge (augmente si nécessaire)
    await attendre(10000);

    // Injecter le code dans le nouvel onglet
    
  });
});

/////////////////////////////////////////////////////////////////
//////////////FIN CHANGEMENT COMPTE//////////////////////////////


// Fonction principale
async function process_alert(alerte){
  if(alerte["strategies"].length > 0){
    // Parcours les alertes
    for (const element of alerte["strategies"]) {
      // Récupère uniquement la mention qui nous intéresse car Trading View envoie l'actif AAVEUSDT.P et MEXC prends AAVE_USDT
      const nomActif = element["actif"].split("USDT")[0];
      let typeOrdre = element.type;
      const stopLoss = element.type;
      const quantite = 90;
      console.log(nomActif);
      // Change l'url
      changementURL2("https://futures.mexc.com/fr-FR/exchange/" + nomActif + "_USDT?type=linear_swap");
      await attendre(15000);
      // Achete au long
      if(typeOrdre.toUpperCase() == "SHORT"){
        buy_short(quantite, stopLoss);
      }
      buy_long(10);
      // Supprime l'alerte
      await attendre(15000);
      delete_alert(element);
    }
  }
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

function changementURL2(data){
  return new Promise((resolve, reject) => {
    chrome.runtime.sendMessage(
      { action: "changeURL", data }, // Le message à envoyer
      (response) => {
          if (chrome.runtime.lastError) {
              reject(chrome.runtime.lastError);
          } else {
              resolve(response.result);
          }
      }
    );
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
  click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 0);
  await attendre(2000);
  fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 0, 10);
  if(stopLoss > 0){
    console.log("stoploss")
    // Coche la case long Sl
    click_button(".ant-checkbox-input", 2);
    await attendre(2000);
    // Clique sur la case du stoploss
    click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 2);
    await attendre(2000);
    // Remplie la case
    fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 2, 1);
    await attendre(2000);
    console.log("achat");
  }
  // Appuie sur open long
  click_button(".component_longBtn__BBkFR", 0);
  await attendre(2000);
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

