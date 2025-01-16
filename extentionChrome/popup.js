// Variables
const dicStrats = {
  "x3" : 1,
  "rsi": 2,
  "bollinger" : 3,
  "moving" : 4,
  "X3-test": 69356848,
  "Bollinge-Test": 69261661
};
const ngrokURL = "https://073a-83-202-127-170.ngrok-free.app"

var varStratSelect;
var selectStrat;
var selectQuantite;

// Boucle récursive pour récupérer les alertes
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
  await attendre(30000);
  infiniteTrade(strat);
}

// Clique sur démarrer le Bot
let strategies = [];
document.getElementById("sendRequest").addEventListener("click", async () => {

  //preventDefault(); // Empêcher le rechargement de la page
  // Récupérer la clé sélectionnée
  const selectedKey = selectElement.value;
  selectStrat = selectedKey;
  selectQuantite = inputElement.value;

  // Trouver la valeur correspondante dans le dictionnaire
  const value = dicStrats[selectedKey];
  varStratSelect=value;

  // Afficher la valeur dans l'élément <p>
  resultElement.textContent = `Valeur sélectionnée : ${value}`;

  infiniteTrade(selectStrat);
});

///////////////////////////////////////////////////
/////Code pour le changement de compte/////////////
///////////////////////////////////////////////////
// Références aux éléments HTML
const selectElement = document.getElementById("choixStrategies");
const resultElement = document.getElementById("choixStratResult");
const formElement = document.getElementById("strategiesForm");
const inputElement = document.getElementById("inputQuantite");

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
/*async function demandeChangementUtilisateur(stratSelect) {
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
  }
}*/

// Initialiser la liste déroulante
populateSelectOptions();

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
      const stopLoss = parseInt(element.stop_loss, 10);
      const valueStopLoss = parseFloat(element.alert_message, 10);
      console.log(nomActif + " " + position + " " + type +" "  + element.strategy_order_name + " " + stopLoss + " " + valueStopLoss  + " ");
      // Change l'url
      delete_alert(element);
      //changementURL2("https://futures.mexc.com/fr-FR/exchange/" + nomActif + "_USDT?type=linear_swap");
      await attendre(3000);
      // Achete au long
      if(position == "short" && type == "buy"){
        await searchCrypto(nomActif);
        await attendre(500);
        await buy(selectQuantite, long = false, stopLoss, valueStopLoss);
      }
      else if (position == "long" && type == "buy"){
        await searchCrypto(nomActif);
        await attendre(500);
        await buy(selectQuantite, long = true, stopLoss, valueStopLoss);
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

function click_button(class_component, numero_component, isHandler = false) {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour vérifier l'état de la case à cocher avant de cliquer
      chrome.scripting.executeScript({
        target: { tabId: currentTab.id },
        func: (class_component, numero_component, isHandler) => {
          const listElements = document.querySelectorAll(class_component);
          let element = listElements[numero_component];
          if (isHandler) {
            element = element.children[1];
          }

          if (!element) {
            console.log("Aucun élément avec la classe voulue trouvé dans l'élément recherché.");
          } else {
            // Vérifier si la case à cocher est déjà cochée
            if (element.type === "checkbox") {
              if (element.checked) {
                console.log("La case à cocher est déjà cochée. Aucun clic effectué.");
              } else {
                // Si elle n'est pas cochée, effectuer le clic
                element.click();

                // Optionnel : Simuler un événement 'change' si nécessaire
                const changeEvent = new Event("change", { bubbles: true });
                element.dispatchEvent(changeEvent);

                console.log("Case à cocher cliquée et cochée.");
              }
            } else {
              element.click();
            }
          }
        },
        args: [class_component, numero_component, isHandler] // Passer les arguments ici
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

async function buy(valeur, long=true, stopLoss=0, valueStopLoss =0, takeProfit=0){
  //Clique sur ouvrir
  click_button(".handle_active__EaFtQ", 0);
  await attendre(2000);
  click_button("#mexc_contract_v_open_position .ant-input", 0);
  await attendre(1000);
  fillButton("#mexc_contract_v_open_position .ant-input", 0, valeur);
  if(stopLoss > 0 || takeProfit>0){
    console.log("SL/TP")
    // Coche la case long Sl
    long ?click_button(".ant-checkbox-input", 2):click_button(".ant-checkbox-input", 3);
    await attendre(1000);
    if (stopLoss>0){
      // Clique sur la case du stoploss
      click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 2);
      await attendre(1000);
      // Remplie la case
      fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 2, valueStopLoss);
      await attendre(1000);
      console.log("achat");
    }
    if(takeProfit>0){
      // Clique sur la case du takeprofit
      click_button(".InputNumberExtend_wrapper__qxkpD .ant-input", 1);
      await attendre(1000);
      // Remplie la case
      fillButton(".InputNumberExtend_wrapper__qxkpD .ant-input", 1, takeProfit);
      await attendre(1000);
      console.log("achat");
    }
  }
  // Appuie sur open long/shirt
  long ? click_button(".component_longBtn__BBkFR", 0):click_button(".component_shortBtn__s8HK4", 0);
  console.log("ordre réalisé");
}

function doitOuvrirRecherche() {
  return new Promise((resolve, reject) => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        const currentTab = tabs[0];

        chrome.scripting.executeScript({
          target: { tabId: currentTab.id },
          func: () => {
            const listElements = document.querySelectorAll(".ResizableWrapper_resizableWrapper__Z_aE5");
            console.log("coucou je suis appelé");
            console.log(listElements);
            // Retourne true si aucun élément trouvé
            return listElements.length === 0;
          }
        }, (results) => {
          // `results` contient les valeurs retournées par le script injecté
          if (chrome.runtime.lastError) {
            console.error(chrome.runtime.lastError.message);
            reject(false);
          } else {
            // Récupérer le résultat du script injecté
            const result = results[0]?.result;
            resolve(result);
          }
        });
      } else {
        reject(false);
      }
    });
  });
} 

async function searchCrypto(actif){
  // ResizableWrapper_resizableWrapper__Z_aE5
  var doitOuvrir;
  doitOuvrirRecherche().then((doitOuvrir) => {
    if (doitOuvrir) {
      click_button(".contractDetail_contractNameBox__IcVlT", 0);
    } else {
      console.log("La recherche n'a pas besoin d'être ouverte.");
    }
  });
  await attendre(1000);
  click_button(".ant-input", 3);
  await attendre(500);
  fillButton(".ant-input", 3, actif);
  await attendre(1000);
  click_button(".Pairs_row__XKonK", 1);
  await attendre(2000);
}

function attendre(ms) { 
  return new Promise(resolve => setTimeout(resolve, ms));
}

function closeTrade(crypto,long){//crypto: les deux ou trois lettre majuscules qui définissent une crypto ex: BTC, ETH etc
  //Long c'est simplement un bouléen qui va nous indiquer quel type de position doit être fermé
  //crypto=crypto+"USDT";
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

  