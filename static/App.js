document.addEventListener("DOMContentLoaded", () => {
  const betInput = document.getElementById("bet");
  const betButton = document.querySelector(".bn632-hover.bn25"); // Bet button
  const resetButton = document.getElementById("reset"); // Reset button
  const automationButton = document.querySelector(".bn633-hover.bn22"); // Automate button

  // Function to place a bet
  function placeBet(betAmount) {
    const request = new Request(`/spin/${betAmount}/black`, {
      headers: {
        Authorization: "authKey",
      },
    });

    fetch(request)
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        document.querySelector("output").innerText = data.message;
      })
      .catch((error) => console.log(`Error: ${error}`));
  }

  // Bet button event listener
  betButton.addEventListener("click", (event) => {
    event.preventDefault();
    const bet = betInput.value;
    if (!bet) {
      alert("Please enter a bet amount.");
      return;
    }
    placeBet(bet);
  });

  // Function to reset balance
  function resetBalance() {
    fetch("/stop")
      .then((response) => response.json())
      .then((data) => {
        console.log("Reset Success:", data);
        document.querySelector("output").innerText = data; // Display reset message
      })
      .catch((error) => console.error("Error:", error));
  }

  // Reset button event listener
  resetButton.addEventListener("click", (event) => {
    event.preventDefault();
    resetBalance();
  });

  // Automation button event listener
  automationButton.addEventListener("click", (event) => {
    event.preventDefault();
    const automationInterval = setInterval(() => {
      const bet = betInput.value;

      if (!bet) {
        alert("Please enter a bet amount.");
        clearInterval(automationInterval);
        return;
      }

      placeBet(bet);

      resetButton.addEventListener("click", () => {
        clearInterval(automationInterval);
        console.log("Automation stopped.");
      });
    }, 2000); // Automates every 2 seconds
  });
});
