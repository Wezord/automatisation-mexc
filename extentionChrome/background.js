chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installée !");
});

chrome.action.onClicked.addListener((tab) => {
  // Vérifie si un onglet actif est disponible
  if (tab.url) {
    console.log(`L'extension a été cliquée sur l'onglet : ${tab.url}`);
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ["content.js"]
    });
  }
});

function attendre(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function direbonjour(){
  alert("bonjour");
}
function alerteOngletActif(){
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
        const activeTabId = tabs[0].id;

        // Injecte et exécute le script
        chrome.scripting.executeScript(
            {
              target: { tabId: activeTabId },
              func: async () => {
                  // Ce code est exécuté dans l'onglet
                  //await attendre(5000);
                  alert("Code exécuté dans l'onglet actif !");
                  direbonjour();
                  changeCompte(69356848);
              },
            },
            () => {
                if (chrome.runtime.lastError) {
                    console.error("Erreur :", chrome.runtime.lastError.message);
                } else {
                    console.log("Code exécuté avec succès dans l'onglet actif.");
                }
            }
        );  
    }
});
}

function changeUser(stratSelect){
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs.length > 0) {
        const activeTabId = tabs[0].id;

        // Injecte et exécute le script
        chrome.scripting.executeScript(
          {
            target: { tabId: activeTabId },
            func: (stratSelect) => {
              console.log("Script injecté dans le nouvel onglet, stratSelect :", stratSelect);
    
              alert("Bonjour, script injecté !");
              const attendreElement = (selector, timeout = 5000) => {
                return new Promise((resolve, reject) => {
                  const interval = 100; // Vérifie toutes les 100 ms
                  let timeElapsed = 0;
                  const timer = setInterval(() => {
                    const element = document.evaluate(
                      `//*[contains(text(), '${selector}')]`,
                      document,
                      null,
                      XPathResult.FIRST_ORDERED_NODE_TYPE,
                      null
                    ).singleNodeValue;
    
                    if (element) {
                      clearInterval(timer);
                      resolve(element);
                    } else if ((timeElapsed += interval) >= timeout) {
                      clearInterval(timer);
                      reject(new Error("Élément non trouvé"));
                    }
                  }, interval);
                });
              };
    
              attendreElement(stratSelect, 5000)
                .then((element) => {
                  console.log("Élément trouvé :", element);
                  alert("Élément trouvé !");
                  element.click();
                })
                .catch((err) => {
                  console.log(err.message);
                  alert(err.message);
                });
            },
            args: [stratSelect], // Passe stratSelect au nouvel onglet
          },
          (results) => {
            console.log("Code injecté dans le nouvel onglet.", results);
          }
        );
    }
});
}



chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "changeUser") {
    changeUser(69261661);
    // Exemple : traitement d'une donnée
    const processedData = `Données traitées : ${message.data}`;
    
    // Réponse envoyée au script d'appel
    sendResponse({ result: processedData });
}
  else if (message.type === "GREETING") {
    console.log("Message reçu depuis content.js :", message.text);
    sendResponse({ response: "Bonjour depuis background.js !" });
  }
});

function changeCompte(stratSelect){
  console.log("Script injecté dans le nouvel onglet, stratSelect :", stratSelect);

  alert("Bonjour, script injecté !");
  const attendreElement = (selector, timeout = 5000) => {
    return new Promise((resolve, reject) => {
      const interval = 100; // Vérifie toutes les 100 ms
      let timeElapsed = 0;
      const timer = setInterval(() => {
        const element = document.evaluate(
          `//*[contains(text(), '${selector}')]`,
          document,
          null,
          XPathResult.FIRST_ORDERED_NODE_TYPE,
          null
        ).singleNodeValue;

        if (element) {
          clearInterval(timer);
          resolve(element);
        } else if ((timeElapsed += interval) >= timeout) {
          clearInterval(timer);
          reject(new Error("Élément non trouvé"));
        }
      }, interval);
    });
  };

  attendreElement(stratSelect, 5000)
    .then((element) => {
      console.log("Élément trouvé :", element);
      alert("Élément trouvé !");
      element.click();
    })
    .catch((err) => {
      console.log(err.message);
      alert(err.message);
    });
}



