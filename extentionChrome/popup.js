// Variables
var dicStrats = {
};

const ngrokURL = "https://idrfrance.ngrok.app"

var varStratSelect;
var selectStrat;
var selectQuantite = 0;
var timeCoeff;
var timeAdjustableCoeff = 1;

var isAutoReinvest = true;
var isDifferentReinvest = false;

var countOpenOrder;

async function infiniteTrade(strat_to_use = "alert") {
  console.log(strategies);
  
  while(!(false)==true){
    console.log(strategies, Object.keys(strategies).length);
    if(Object.keys(strategies).length > 1){
      console.log("process data");
      await process_alert(strategies);
      /// CHECK IF DOUBLON
      await attendre(500);
      console.log("process data");
      if(!isDifferentReinvest) {
        await attendre(500);
        console.log("process data");
        strategies = await checkDoublon();
        await process_alert(strategies);
      }
      strategies = []
    }
    else {
      console.log("get new data");
      try {
        const response = await fetch(ngrokURL + "/get_alert?strategy=" + strat_to_use, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (!response.ok) {
          throw new Error(`Erreur HTTP : ${response.status}`);
        }
        const data = await response.json();
        console.log("Réponse :", data);
        // Envoie le json des stratégies à process 
        strategies = data;
        timeCoeff = data["time_coeff"];
      } 
      catch (error) {
        console.error("Erreur :", error);
      }
    await attendre(20000);
    }
  }
}

// Clique sur démarrer le Bot
var strategies = [];
document.getElementById("sendRequest").addEventListener("click", async () => {
  
  click_button(".quickTrading_closeIcon__pRcJ5",0);

  //preventDefault(); // Empêcher le rechargement de la page
  // Récupérer la clé sélectionnée

  const selectedKey = selectElement.value;
  selectStrat = selectedKey;
  timeAdjustableCoeff = timeCoeffElement.value;
  console.log("Démarrage du Bot")

  if(isAutoReinvest) {console.log("invest"); await reinvest();}

  // Trouver la valeur correspondante dans le dictionnaire
  const value = dicStrats[selectedKey];
  varStratSelect=value;

  // Afficher la valeur dans l'élément <p>
  resultElement.textContent = `Valeur sélectionnée : ${value}`;


  infiniteTrade(selectStrat);
});

document.getElementById("inputQuantiteCheckbox").addEventListener("change", async () => {
  if (document.getElementById("inputQuantiteCheckbox").checked) {

    isAutoReinvest = false;
    const selectedKey = inputQuantieElement.value;
    if(!selectedKey) { alert("Pas de quantité rentrée !"); document.getElementById("inputQuantiteCheckbox").click(); return;}
    selectQuantite=selectedKey;
    console.log(selectedKey)


    console.log("Changement de quantité manuellement")
    /** 
    const data = {
      quantite: parseInt(selectedKey),
      strategy: selectStrat
    };
    try {
      const response = await fetch(ngrokURL + "/set_highest_reach", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error(`Erreur HTTP : ${response.status}`);
      }

      const datas = await response.json();
      console.log("Réponse :", datas);
      selectQuantite = datas["quantite"];
    } catch (error) {
      console.error("Erreur :", error);
    }
      */
  }
  else {
    isAutoReinvest = true;
    await reinvest(); 
    console.log("Activation de l'auto invest")
  }
});

document.getElementById("timeCoeffButton").addEventListener("click", async () => {
  const selectedKey = timeCoeffElement.value;
  timeAdjustableCoeff=selectedKey;
  console.log("Nouveau time coeff", selectedKey)
  if(!selectedKey) { alert("Pas de coeff rentrée !"); return;}
});

///////////////////////////////////////////////////
/////Code pour le changement de compte/////////////
///////////////////////////////////////////////////
// Références aux éléments HTML
const selectElement = document.getElementById("choixStrategies");
const resultElement = document.getElementById("choixStratResult");
const formElement = document.getElementById("strategiesForm");
const inputQuantieElement = document.getElementById("inputQuantite");
const timeCoeffElement = document.getElementById("timeCoeff");

// Remplir la liste déroulante avec les clés du dictionnaire

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

async function populateSelectOptions() {
  try {
    const response = await fetch(ngrokURL + "/config", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`Erreur HTTP : ${response.status}`);
    }
    const data = await response.json();
    console.log("Réponse :", data);
    // Envoie le json des stratégies à process
    dicStrats = data["strategies"];
  } 
  catch (error) {
    console.error("Erreur :", error);
  }
  for (strat in dicStrats) {
    const option = document.createElement("option");
    option.value = dicStrats[strat]; // La valeur de l'option sera la clé
    option.textContent = dicStrats[strat]; // Le texte affiché sera la clé
    selectElement.appendChild(option);
  }
}
populateSelectOptions();

/////////////////////////////////////////////////////////////////
//////////////FIN CHANGEMENT COMPTE//////////////////////////////


// Fonction principale
async function process_alert(alerte){
  if(alerte["strategies"].length > 0){
    // Selectionne le bon montant
    // Parcours les alertes
    for (const element of alerte["strategies"]) {

      console.log(timeCoeff);
      // Récupère uniquement la mention qui nous intéresse car Trading View envoie l'actif AAVEUSDT.P et MEXC prends AAVE_USDT
      const nomActif = element["actif"].split(".")[0];
      const position = element.position;
      const type = element.type;
      const stopLoss = parseInt(element.stop_loss, 10);
      const takeProfit = parseInt(element.take_profit, 10);
      const is_different_reinvest = element.is_different_reinvest
      let valueStopLoss = 0;
      let valueTakeProfit = 0;

      if (is_different_reinvest != null && is_different_reinvest == 1) {
        isAutoReinvest = false;
        selectQuantite = element.alert_message.split(" QTY :")[1]
        isDifferentReinvest = true;
      }
      else {
        isDifferentReinvest = false;
      }

      console.log(element.alert_message.split("SL :"))
      if(stopLoss == 1 && element.alert_message.split("SL :").length > 1){
        valueStopLoss = parseFloat(element.alert_message.split("SL :")[1].split(" TP :")[0], 10);
      }

      console.log(element.alert_message.split("TP :"))
      if(takeProfit == 1 && element.alert_message.split("TP :").length > 1){
        valueTakeProfit = parseFloat(element.alert_message.split("TP :")[1].split(" QTY :")[0], 10);
      }
      
      console.log(nomActif + " " + position + " " + type +" "  + element.strategy_order_name + " " + stopLoss + " " + valueStopLoss  + " " + takeProfit + " " + valueTakeProfit);

      await delete_alert(element);

      // Achete au long
      if(type == "buy"){
        if(position == "short")
        {
          timeCoeff = timeCoeff + 1;
          await searchCrypto(nomActif);
          await attendre(1000 + 2000*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
          await buy(selectQuantite, long = false, stopLoss, valueStopLoss, takeProfit, valueTakeProfit);
        }
        else
        {
          timeCoeff = timeCoeff + 1;
          await searchCrypto(nomActif);
          await attendre(2000 + 3000*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
          await buy(selectQuantite, long = true, stopLoss, valueStopLoss, takeProfit, valueTakeProfit);
        }
      }
      else {
        if (position == "short"){
          await attendre(500 + 1000*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
          await closeTrade(nomActif, false);
          await attendre(1000 +1500*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
        }
        else {
          await attendre(500 + 1000*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
          await closeTrade(nomActif, true);
          await attendre(1000 + 1500*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
        }
      }
      // Supprime l'alerte
      await attendre(500);
    }
    if (isAutoReinvest) {await reinvest();}
  }
  else {
    console.log("Pas de donnée à process")
  }
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

function click_button(class_component, numero_component, option = "") {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
      const currentTab = tabs[0];
      const currentUrl = currentTab.url;

      // Injecter un script pour vérifier l'état de la case à cocher avant de cliquer
      chrome.scripting.executeScript({
        target: { tabId: currentTab.id },
        func: (class_component, numero_component, option) => {
          var listElements= document.querySelectorAll(class_component);
          var element = listElements[numero_component];
          
          var acliquer=1

          if (!element) {
            console.log("Aucun élément avec la classe voulue trouvé dans l'élément recherché.");
          } else {
            if (element.type === "checkbox"){
              if (element.checked) {
                console.log("La case à cocher est déjà cochée. Aucun clic effectué.");
                ///////////////////////////////////////////////////////////////////
                //EN CAS DE BUG AVEC LA VERIFICATION DE CASE, SUPPRIMER CETTE LIGNE
                //acliquer=0;
              }
            }
            if (acliquer){           
             // Si elle n'est pas cochée, effectuer le clic
            element.click();

            // Optionnel : Simuler un événement 'change' si nécessaire
            const changeEvent = new Event("change", { bubbles: true });
            element.dispatchEvent(changeEvent);

            console.log("Case à cocher cliquée et cochée.");
            }
          }
        },
        args: [class_component, numero_component, option] // Passer les arguments ici
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

async function buy(valeur, long=true, stopLoss=0, valueStopLoss =0, takeProfit = 0, valueTakeProfit = 0 ){
  //Clique sur ouvrir
  click_button("#mexc_contract_v_open_position .ant-input", 0);
  await attendre(500);
  fillButton("#mexc_contract_v_open_position .ant-input", 0, valeur);
  if(stopLoss > 0 || takeProfit>0){
    console.log("SL/TP")
    // Coche la case long Sl
    await attendre(500);
    long ?click_button(".component_checkBoxView__DsRmy .ant-checkbox-wrapper .component_checkText__mHuZJ", 0):click_button(".component_checkBoxView__DsRmy .ant-checkbox-wrapper .component_checkText__mHuZJ", 1);
    await attendre(500);
    if (stopLoss>0){
      // Clique sur la case du stoploss
      click_button(".InputNumberExtendV2_inputWrapper__TgHac .ant-input", 1);
      await attendre(500);
      // Remplie la case
      fillButton(".InputNumberExtendV2_inputWrapper__TgHac .ant-input", 1, valueStopLoss);
      await attendre(500);
      console.log("sl");
    }
    if(takeProfit>0){
      // Clique sur la case du takeprofit
      click_button(".InputNumberExtendV2_inputWrapper__TgHac .ant-input", 0);
      await attendre(500);
      // Remplie la case
      fillButton(".InputNumberExtendV2_inputWrapper__TgHac .ant-input", 0, valueTakeProfit);
      await attendre(500);
      console.log("tp");
    }
  }
  // Appuie sur open long/shirt
  await attendre(1000 + 1500*excecutionTime(1.38, 0.37, 20, timeCoeff / 40));
  long ? click_button(".component_longBtn__BBkFR", 0):click_button(".component_shortBtn__s8HK4", 0);
  await attendre(500);
  if (stopLoss > 0){long ?click_button(".component_checkBoxView__DsRmy .ant-checkbox-wrapper .component_checkText__mHuZJ", 0):click_button(".component_checkBoxView__DsRmy .ant-checkbox-wrapper .component_checkText__mHuZJ", 1);}
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
  var doitOuvrir=true;
  click_button(".contractDetail_contractNameBox__IcVlT", 0);
  await attendre(500* timeAdjustableCoeff + 500/7 * timeCoeff);
  click_button(".Pairs_searchSelect__i_dbG .ant-input", 0);
  await attendre(500);
  fillButton(".Pairs_searchSelect__i_dbG .ant-input", 0, actif);
  await attendre(500);
  // A changer en fonction de la langue
  click_button("[title='"+ actif + " Perpétuel'" + "]", 0);
  await attendre(1000* timeAdjustableCoeff + 500/7 * timeCoeff);
  await doitOuvrirRecherche().then((doitOuvrir) => {
    if (doitOuvrir) {
      {}
    } else {
      click_button(".contractDetail_contractNameBox__IcVlT", 0);
      console.log("Fermeture manuelle de la boite de recherche.");
    }
  });
}

function attendre(ms) { 
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function closeTrade(crypto,long){//crypto: les deux ou trois lettre majuscules qui définissent une crypto ex: BTC, ETH etc
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
              element.textContent.trim().toLowerCase().split("usdt")[0] === crypto.toLowerCase().split("usdt")[0]);
            const nbMatchingElements=matchingElements.length;
            console.log(nbMatchingElements," éléments correponsdants ont été détectés");
            const matchingElements2=Array.from(matchingElements).filter((element) =>
              element.textContent.trim().toLowerCase().includes(long ? "long" : "short"));
            console.log("Nombre de nouveaux éléments correspndants: ",matchingElements2.length);
              if(matchingElements2.length==1){                
                const bouton=(matchingElements2[0].querySelectorAll(`button`))[0];
                bouton.click()
              }
              else{
                console.log("Trop d'éléments correspondants. Abandon");
              }
          }
        },
        args: [crypto,class_component,long]  // Passer les arguments ici
      });
    }
  });
}

async function reinvest() {
  console.log("appel");
  let actualQuantite = 0;

  // Attendre que chrome.tabs.query termine et renvoie le tab actif
  const tabs = await new Promise((resolve) => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      resolve(tabs);
    });
  });

  if (tabs.length > 0) {
    const currentTab = tabs[0];

    // Injecter un script dans l'onglet actif pour récupérer la quantité
    actualQuantite = await new Promise((resolve) => {
      chrome.scripting.executeScript(
        {
          target: { tabId: currentTab.id },
          func: () => {
            // Script exécuté dans la page pour obtenir la quantité
            var element = document.querySelectorAll(".AssetsItem_num__akJcs")[0];
            if (!element) {
              console.log("Aucun élément avec la classe voulue trouvé.");
              return null; // Retourner null si l'élément est introuvable
            } else {
              // Récupérer la quantité de l'élément
              const quantityText = element.innerHTML.split(" ")[0].split(",");
              const actualQuantite = quantityText[0] + quantityText[1];
              console.log("Quantité récupérée :", actualQuantite);
              return actualQuantite; // Retourner la quantité
            }
          }
        },
        (result) => {
          // Ici, nous récupérons le résultat renvoyé par le script injecté
          resolve(result[0]?.result); // Resolve la promesse avec la quantité récupérée
        }
      );
    });

    // Vérifier si actualQuantite a une valeur valide
    if (!actualQuantite) {
      console.log("Aucune quantité récupérée, terminaison de la fonction.");
      return; // Si aucune quantité n'est récupérée, arrêtez l'exécution
    }

    // Utiliser la quantité récupérée pour effectuer la requête
    const data = {
      action: "compare",
      quantite: actualQuantite,
      strategy: selectStrat
    };

    try {
      const response = await fetch(ngrokURL + "/highest_reach", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error(`Erreur HTTP : ${response.status}`);
      }

      const datas = await response.json();
      console.log("Réponse :", datas);
      selectQuantite = datas["quantite"];
    } catch (error) {
      console.error("Erreur :", error);
    }
  }

  console.log("La quantité finale est ", selectQuantite);
}

function excecutionTime(a,b,c,x){
  return (a*(x-b)**4)*Math.log(x) + x /c
}
async function checkDoublon(){
  const data = {
    action : "checkDoublon",
    strategy : selectStrat,
    quantite : selectQuantite
  }
  try {
    const response = await fetch(ngrokURL + "/check_doublon", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      throw new Error(`Erreur HTTP : ${response.status}`);
    }
    const datas = await response.json();
    console.log("Réponse :", datas);
    strategies = datas;
  } 
  catch (error) {
    console.error("Erreur :", error);
  }

  return strategies;
}