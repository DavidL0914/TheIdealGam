---
toc: false
layout: post
hide: true
title: Racing Gam
---

<head>
  <style>
    body {
      background-color: #111;
      color: #fff;
      font-family: 'Arial', sans-serif;
    }

    button {
      background-color: #363636;
      color: #fff;
      border: 2px solid #4d4d4d;
      padding: 10px 15px;
      margin: 5px;
      cursor: pointer;
      border-radius: 5px;
      font-size: 16px;
    }

    button:hover {
      background-color: #595959;
    }

    select {
      background-color: #363636;
      color: #fff;
      border: 2px solid #4d4d4d;
      padding: 5px;
      margin: 5px;
      cursor: pointer;
      border-radius: 5px;
    }

    select:hover {
      background-color: #595959;
    }

    #game-board {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }

    .hidden {
      display: none;
    }

    /* Add these styles to your existing CSS */

#car-selection {
  background-color: #333;
  padding: 20px;
  border-radius: 10px;
  margin-top: 20px;
}

.car-preview {
  width: 100px;
  height: 60px;
  background-size: cover;
  margin-bottom: 10px;
}

#player1-car,
#player2-car {
  width: 100%;
  padding: 8px;
  font-size: 16px;
}

#player1-preview,
#player2-preview {
  width: 100px;
  height: 60px;
  background-size: cover;
  margin-top: 10px;
}


    #car-selection button {
      background-color: #363636;
      color: #fff;
      border: 2px solid #4d4d4d;
      padding: 10px 15px;
      margin: 5px;
      cursor: pointer;
      border-radius: 5px;
      font-size: 16px;
    }

    #car-selection button:hover {
      background-color: #595959;
    }


  </style>
</head>

<body>
  <div id="game-board">
    <button id="start-game" onclick="showCarSelection()">Start Game</button>
    <div id="car-selection" class="hidden">
      <p>Player 1, select your car:</p>
      <select id="player1-car" onchange="previewCarImage('player1-preview', this.value)">
        <option value="https://files.catbox.moe/zgt1ir.png">Car 1</option>
        <option value="https://files.catbox.moe/vfvqch.png">Car 2</option>
        <option value="https://files.catbox.moe/h20zxw.png">Car 3</option>
        <option value="https://files.catbox.moe/zzvbpr.png">Car 4</option>
        <option value="https://files.catbox.moe/2ciphb.png">Car 5</option>
      </select>
      <div id="player1-preview" class="car-preview"></div>

      <p>Player 2, select your car:</p>
      <select id="player2-car" onchange="previewCarImage('player2-preview', this.value)">
        <option value="https://files.catbox.moe/zgt1ir.png">Car 1</option>
        <option value="https://files.catbox.moe/vfvqch.png">Car 2</option>
        <option value="https://files.catbox.moe/h20zxw.png">Car 3</option>
        <option value="https://files.catbox.moe/zzvbpr.png">Car 4</option>
        <option value="https://files.catbox.moe/2ciphb.png">Car 5</option>
      </select>
      <div id="player2-preview" class="car-preview"></div>

      <button onclick="showGameElements()">Start Game</button>
    </div>

    <div id="game-status" class="hidden">Binary Racing Game! Press "Start Game" to begin.</div>
    <div id="racetrack" class="hidden">
      <div id="car1" class="car" style="bottom: 0;"></div>
      <div id="car2" class="car" style="top: 0;"></div>
    </div>
    <div id="car-position" class="hidden">Player 1 Position: 0 | Player 2 Position: 0</div>
    <div id="target-number" class="hidden">Target Decimal Number: -</div>
    <input type="text" id="user-input" class="hidden" placeholder="Enter binary number">
    <button id="submit-button" onclick="submitGuess()" class="hidden">Submit Guess</button>

  </div>
  <script>
    function showGameElements() {
      document.getElementById('start-game').classList.add('hidden');
      document.getElementById('car-selection').classList.add('hidden');
      document.getElementById('game-status').classList.remove('hidden');
      document.getElementById('racetrack').classList.remove('hidden');
      document.getElementById('car-position').classList.remove('hidden');
      document.getElementById('target-number').classList.remove('hidden');
      document.getElementById('user-input').classList.remove('hidden');
      document.getElementById('user-input').focus();
      document.getElementById('submit-button').classList.remove('hidden');
      startGame();
    }

    let boardSize = 10;
    let currentPlayer = 1;
    let playerPositions = { 1: 0, 2: 0 };
    let currentTargetDecimalNumber;
    let player1Car, player2Car;
    let gameStarted = false;

    function updateGameStatus() {
      document.getElementById('car-position').innerText = `Player 1 Position: ${playerPositions[1]} | Player 2 Position: ${playerPositions[2]}`;
      document.getElementById('car1').style.left = `${(playerPositions[1] / boardSize) * 100}%`;
      document.getElementById('car2').style.left = `${(playerPositions[2] / boardSize) * 100}%`;
    }

    function updateTargetNumber(targetDecimalNumber) {
      document.getElementById('target-number').innerText = `Target Decimal Number: ${targetDecimalNumber}`;
    }

    function switchPlayer() {
      currentPlayer = currentPlayer === 1 ? 2 : 1;
      document.getElementById('game-status').innerText = `It's Player ${currentPlayer}'s turn.`;
    }

    function checkWinner() {
      if (playerPositions[1] === boardSize) {
        console.log("Player 1 wins!");
        return true;
      } else if (playerPositions[2] === boardSize) {
        console.log("Player 2 wins!");
        return true;
      }
      return false;
    }

    function generateRandomNumber() {
      return Math.floor(Math.random() * 101);
    }

    function gameLoop() {
      if (!checkWinner() && gameStarted) {
        currentTargetDecimalNumber = generateRandomNumber();
        const targetBinaryNumber = currentTargetDecimalNumber.toString(2);
        updateTargetNumber(currentTargetDecimalNumber);
        updateGameStatus();
      } else if (gameStarted) {
        console.log("Game over!");
      }
    }

    function submitGuess() {
      const userInput = document.getElementById('user-input').value;
      try {
        const guessDecimal = parseInt(userInput, 2);
        if (guessDecimal === currentTargetDecimalNumber) {
          console.log(`Player ${currentPlayer} is correct! Their car moves forward by 1 space.`);
          playerPositions[currentPlayer] += 1;
          switchPlayer();
          gameLoop();
        } else {
          console.log(`Player ${currentPlayer} is incorrect. The correct decimal number was ${currentTargetDecimalNumber}.`);
          switchPlayer();
        }
      } catch (error) {
        console.log("Invalid input. Please enter a valid binary number.");
      }
      document.getElementById('user-input').value = '';
    }

    function showCarSelection() {
      document.getElementById('start-game').style.display = 'none';
      document.getElementById('car-selection').style.display = 'block';
    }

    function previewCarImage(previewElementId, imageUrl) {
      document.getElementById(previewElementId).style.backgroundImage = `url('${imageUrl}')`;
    }

    function startGame() {
      if (!gameStarted) {
        player1Car = document.getElementById('player1-car').value;
        player2Car = document.getElementById('player2-car').value;
        document.getElementById('car-selection').style.display = 'none';
        document.getElementById('car1').style.backgroundImage = `url('${player1Car}')`;
        document.getElementById('car2').style.backgroundImage = `url('${player2Car}')`;
        document.getElementById('car1').style.bottom = '0';
        document.getElementById('car2').style.top = '0';
        document.getElementById('start-game').disabled = true;
        gameStarted = true;
        gameLoop();
      }
    }
  </script>
</body>
