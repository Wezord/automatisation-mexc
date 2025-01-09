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

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "GREETING") {
    console.log("Message reçu depuis content.js :", message.text);
    sendResponse({ response: "Bonjour depuis background.js !" });
  }
});