const dicStrats = {
  "x3" : 1,
  "rsi": 2,
  "bollinger" : 3,
  "moving" : 4,
  "X3-test": 69356848,
  "Bollinge-Test": 69261661
};
const ngrokURL = "https://704e-83-202-127-170.ngrok-free.app"
var varStratSelect;
var selectStrat;

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

async function infiniteTrade(strat_to_use = "alert"){
  const strat = strat_to_use;
  const url = ngrokURL + "/" + strat;
  console.log(strategies);
  if(Object.keys(strategies).length > 0){
    console.log("process data");
    await process_alert(strategies);
    strategies = [];
  }
  else {
    console.log("get new data");
    try {
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-Custom-Message": "get_alert"
        },
      });
      if (!response.ok) {
        throw new Error(`Erreur HTTP : ${response.status}`);
      }
      const data = await response.json();
      console.log("Réponse :", data);
      // Envoie le json des stratégies à process 
      strategies = data;
    } 
    catch (error) {
      console.error("Erreur :", error);
      alert("Erreur lors de la requête : " + error.message);
    }
  }
  await attendre(1000);
  infiniteTrade(strat);
}

let strategies = [];
document.getElementById("sendRequest").addEventListener("click", async () => {
  infiniteTrade(selectStrat);
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
  selectStrat = selectedKey;

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
      //const nomActif = element["actif"].split("USDT")[0];
      const nomActif = element["actif"].split(".")[0];
      const position = element.position;
      const type = element.type;
      const stopLoss = parseInt(element.stopLoss, 10);
      const valueStopLoss = parseFloat(element.alert_message, 10);;
      const quantite = 90;
      console.log(nomActif + " " + position + " " + type +" "  + element.strategy_order_name);
      // Change l'url
      delete_alert(element);
      await attendre(2000);
      await searchCrypto(nomActif);
      //changementURL2("https://futures.mexc.com/fr-FR/exchange/" + nomActif + "_USDT?type=linear_swap");
      await attendre(3000);
      // Achete au long
      if(position == "short" && type == "buy"){
        await buy_short(stopLoss, valueStopLoss, 90);
      }
      else if (position == "long" && type == "buy"){
        await buy_long(stopLoss, valueStopLoss, 90);
      }
      else if (position == "short" && type == "sell"){
        closeTrade(nomActif, "short");
        await attendre(1000);
      }
      else if (position == "long" && type == "sell"){
        closeTrade(nomActif, "long");
        await attendre(1000);
      }
      else if(position == "flat"){
        closeTrade(nomActif, "long");
        await attendre(1000);
        closeTrade(nomActif, "short");
        await attendre(1000);
      }
      else { 
        console.log("wut?")
      }
      // Supprime l'alerte
      await attendre(1000);
    }
  }
  return alerte;
}

async function delete_alert(alerte_to_delete){
  const url = ngrokURL + "/delete_alert";
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

function click_button(class_component, numero_component, isHandler=false){
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour modifier l'URL de la page
    chrome.scripting.executeScript({
      target: { tabId: currentTab.id },
      func: (class_component, numero_component, isHandler) => {
        const listElements = document.querySelectorAll(class_component);
        element=listElements[numero_component];
        if(isHandler){
          element=element.children[1];
        }
        
        if (!element){
          console.log("Aucun élément avec la classe voulue trouvé dans l'élément recherché'.");
        }
        else{
            element.click();

            // Optionnel : Simuler un événement 'change' si nécessaire
            const changeEvent = new Event("change", { bubbles: true });
            element.dispatchEvent(changeEvent);
    
            console.log("Button cliqué");
        }
      },
      args: [class_component, numero_component, isHandler]  // Passer les arguments ici
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
            console.log("Aucun élément avec la classe 'maClasse' trouvé dans l'élément avec ID 'monId'." + class_component + " " + numero_component);
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

async function buy_long(stopLoss,  value_stopLoss = 0.1, value_buy=10){
  //Clique sur ouvrir
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 0);
  await attendre(2000);
  fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 0, value_buy);
  await attendre(2000);
  if(stopLoss > 0){
    console.log("stoploss")
    // Coche la case long Sl
    click_button(".ant-checkbox-input", 2);
    await attendre(2000);
    // Clique sur la case du stoploss
    click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 2);
    await attendre(2000);
    // Remplie la case
    fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 2, value_stopLoss);
    await attendre(2000);
    console.log("achat");
  }
  // Appuie sur open long
  click_button(".component_longBtn__BBkFR", 0);
  await attendre(2000);
  console.log("ordre réalisé");
}

async function buy_short(stopLoss, value_stopLoss = 400, value_buy =10){
  //Clique sur ouvrir
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 0);
  await attendre(2000);
  fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 0, value_buy);
  await attendre(2000);
  if(stopLoss > 0){
    console.log("stoploss")
    // Coche la case long Sl
    click_button(".ant-checkbox-input", 3);
    await attendre(2000);
    // Clique sur la case du stoploss
    click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 2);
    await attendre(2000);
    // Remplie la case
    fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 2, 400);
    await attendre(2000);
    console.log("achat");
  }
  // Appuie sur open long
  click_button(".component_shortBtn__s8HK4", 0);
  await attendre(2000);
  console.log("ordre réalisé");
}

async function close_short(){
  click_button(".handle_vInner__IXFRx",0,true);
  await attendre(2000);
  click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 1);
  await attendre(2000);
  fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 1, 100000000);
  await attendre(2000);
  click_button(".component_longBtn__BBkFR", 1);
  await attendre(2000);
  console.log("ordre réalisé");
}

async function close_long(){
  click_button(".handle_vInner__IXFRx",0,true);
  await attendre(2000);
  click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 1);
  await attendre(2000);
  fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 1, 100000000);
  await attendre(2000);
  click_button(".component_shortBtn__s8HK4", 1);
  await attendre(2000);
  console.log("ordre réalisé");
}

async function buy(valeur,stopLoss=0,takeProfit=0,long=true){
  //Clique sur ouvrir
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button("#mexc_contract_v_open_position .ant-input", 1);
  await attendre(1000);
  fillButton("#mexc_contract_v_open_position .ant-input", 1, valeur);
  if(stopLoss > 0 || takeProfit>0){
    console.log("SL/TP")
    // Coche la case long Sl
    long ?click_button(".ant-checkbox-input", 2):click_button(".ant-checkbox-input", 3);
    await attendre(1000);
    if (stopLoss>0){
      // Clique sur la case du stoploss
      click_button(".InputNumberExtend_wrapper__qxkpD", 4);
      await attendre(1000);
      // Remplie la case
      fillButton(".InputNumberExtend_wrapper__qxkpD", 4, stopLoss);
      await attendre(1000);
      console.log("achat");
    }
    if(takeProfit>0){
      // Clique sur la case du takeprofit
      click_button(".InputNumberExtend_wrapper__qxkpD", 3);
      await attendre(1000);
      // Remplie la case
      fillButton(".InputNumberExtend_wrapper__qxkpD", 3, takeProfit);
      await attendre(1000);
      console.log("achat");
    }

  }
  // Appuie sur open long/shirt
  long ? click_button(".component_longBtn__BBkFR", 0):click_button(".component_shortBtn__s8HK4", 0);
  console.log("ordre réalisé");
}

async function searchCrypto(actif){
  click_button(".contractDetail_contractNameBox__IcVlT", 0);
  await attendre(1000);
  click_button(".ant-input", 2);
  await attendre(1000);
  fillButton(".ant-input", 2, actif);
  await attendre(1000);
  click_button(".Pairs_row__XKonK", 1);
  await attendre(2000);
  //click_button(".contractDetail_contractNameBox__IcVlT", 0);
  await attendre(1000);
}

function attendre(ms) { 
  return new Promise(resolve => setTimeout(resolve, ms));
}

function closeTrade(crypto,long){//crypto: les deux ou trois lettre majuscules qui définissent une crypto ex: BTC, ETH etc
  //Long c'est simplement un bouléen qui va nous indiquer quel type de position doit être fermé
  crypto=crypto+"USDT";
  console.log(crypto);
  class_component=".ant-table-row-level-0";
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;
      

      // Injecter un script pour modifier l'URL de la page
      chrome.scripting.executeScript({
        target: { tabId: currentTab.id },
        func: (crypto,class_component,long) => {
          const listElements = document.querySelectorAll(class_component);
          //console.log("liste elements :",listElements);
          /*element=listElements[numero_component];*/
          
          if (listElements.length==0){
              //alert("Aucun trade ouvert n'a été trouvé dans l'interfafe grahique !");
              console.log("Aucun trade ouvert n'a été trouvé dans l'interfafe grahique !");
          }
          else{
            const matchingElements = Array.from(listElements).filter((element) =>
              element.textContent.trim().toLowerCase().includes(crypto.toLowerCase()));
            const nbMatchingElements=matchingElements.length;
            if (nbMatchingElements==1){
              const bouton=(matchingElements[0].querySelectorAll(`.FastClose_closeBtn__ze4z7`))[0];
              bouton.click();
            }
            else if(nbMatchingElements>1){
              console.log(nbMatchingElements," éléments correponsdants ont été détectés");
              const matchingElements2=Array.from(matchingElements).filter((element) =>
                element.textContent.trim().toLowerCase().includes(long ? "long" : "short"));
              console.log("Nombre de nouveaux éléments correspndants: ",matchingElements2.length);

              if(matchingElements2.length==1){                
                const bouton=(matchingElements2[0].querySelectorAll(`.FastClose_closeBtn__ze4z7`))[0];
                bouton.click()
              }
              else{
                console.log("Trop d'éléments correspondants. Abandon");
              }
            } 
          }
        },
        args: [crypto,class_component,long]  // Passer les arguments ici
      });
    }
  });
}

  