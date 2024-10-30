document.addEventListener("DOMContentLoaded", () => {
  const betInput = document.getElementById("bet");
  const betButton = document.querySelector(".bn632-hover.bn25");
  const resetButton = document.getElementById("reset");
  const automationButton = document.querySelector(".bn633-hover.bn22");

  // Function to place a bet
  function placeBet(betAmount) {
    fetch(`https://roulettemartingale.herokuapp.com/spin/${betAmount}/black`)
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
        document.querySelector("output").innerText = data;
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
    fetch(`https://roulettemartingale.herokuapp.com/stop`)
      .then((response) => response.text())
      .then((data) => {
        console.log("Reset Success:", data);
        document.querySelector("output").innerText = data;
      })
      .catch((error) => console.error("Error:", error));
  }

  resetButton.addEventListener("click", (event) => {
    event.preventDefault();
    resetBalance();
  });

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
      resetButton.addEventListener("click", () =>
        clearInterval(automationInterval)
      );
    }, 2000);
  });
});
