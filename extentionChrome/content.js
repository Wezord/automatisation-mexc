// Ce script s'exécute sur les pages correspondant au pattern défini dans manifest.json

console.log("content.js chargé avec succès !");

// Ajout d'une bordure rouge à tous les éléments <p> de la page
document.querySelectorAll("p").forEach((p) => {
  p.style.border = "2px solid red";
});

// Envoyer un message au fichier background.js
chrome.runtime.sendMessage(
  { type: "CONTENT_SCRIPT_LOADED", text: "content.js actif !" },
  (response) => {
    console.log("Réponse reçue de background.js :", response.response);
  }
);