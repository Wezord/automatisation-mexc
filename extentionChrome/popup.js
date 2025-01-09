document.getElementById("changeUrlButton").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: () => {
            // Modifier l'URL de la page
            window.location.href = "https://www.google.com";
          }
        });
      }
    });
  });
