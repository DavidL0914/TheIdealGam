---
toc: false
layout: post
hide: true
title: Racing Gam
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Racing Game</title>

  <style>
    /* General styling for the page */
    body {
      background-color: #111;
      color: #fff;
      font-family: 'Arial', sans-serif;
    }

    /* Styling for buttons */
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

    /* Styling for selects */
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

    /* Styling for the game board container */
    #game-board {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }

    /* Styling for hidden elements */
    .hidden {
      display: none;
    }

    /* Car selection styles */
    #car-selection {
      background-color: #333;
      padding: 20px;
      border-radius: 10px;
      margin-top: 20px;
    }

    /* Car preview styles */
    .car-preview {
      width: 64px;
      height: 76.8px;
      background-size: contain;
      margin-bottom: 10px;
      background-repeat: no-repeat;
    }

    /* Racetrack styles */
    #racetrack {
      position: relative;
      height: 200px;
      background-color: #001f3f;
      margin-top: 20px;
    }

    /* Finish line styles */
    #finish-line {
      position: absolute;
      top: 0;
      left: calc(100% - 20px);
      width: 20px;
      height: 100%;
      background: linear-gradient(45deg, #000 25%, #fff 25%, #fff 50%, #000 50%, #000 75%, #fff 75%, #fff 100%);
      background-size: 20px 20px;
    }

    /* Car styles */
    .car {
      position: absolute;
      width: 12%;
      height: 24%;
      background-size: cover;
      background-repeat: no-repeat;
      margin-bottom: 10px;
      transform: rotate(90deg);
      margin-left: 10px;
    }

    /* Game status and information styles */
    #game-status,
    #car-position,
    #target-number {
      color: #fff;
      font-size: 18px;
      margin-bottom: 10px;
    }

    /* User input styles */
    #user-input {
      background-color: #000;
      color: #fff;
      border: 2px solid #333;
      padding: 10px;
      margin-right: 10px;
      font-size: 16px;
      border-radius: 5px;
    }

    /* Submit button styles */
    #submit-button {
      background-color: #4d4dff;
      color: #fff;
      border: 2px solid #333;
      padding: 10px 15px;
      cursor: pointer;
      border-radius: 5px;
      font-size: 16px;
    }

    #submit-button:hover {
      background-color: #1a1aff;
    }

    /* Message popup styles */
    #message-popup {
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background-color: #ff0000;
      color: #fff;
      padding: 15px;
      border-radius: 10px;
      text-align: center;
      display: none;
    }

    /* Winning animation styles */
    @keyframes winningAnimation {
      0% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.2);
      }
      100% {
        transform: scale(1);
      }
    }
  </style>
</head>

<body>
  <div id="game-board">
    <!-- Start Game button -->
    <button id="start-game" onclick="showCarSelection()">Start Game</button>
    <!-- Car Selection section -->
    <div id="car-selection" class="hidden">
      <p>Player 1, select your car:</p>
      <select id="player1-car" onchange="previewCarImage('player1-preview', this.value)">
        <option value="https://files.catbox.moe/lwpg7l.png">Car 1</option>
        <option value="https://files.catbox.moe/yrrydx.png">Car 2</option>
        <option value="https://files.catbox.moe/l67b2k.png">Car 3</option>
        <option value="https://files.catbox.moe/u4l0m2.png">Car 4</option>
      </select>
      <div id="player1-preview" class="car-preview"></div>

      <p>Player 2, select your car:</p>
      <select id="player2-car" onchange="previewCarImage('player2-preview', this.value)">
        <option value="https://files.catbox.moe/zgi62v.png">Car 1</option>
        <option value="https://files.catbox.moe/427n2v.png">Car 2</option>
        <option value="https://files.catbox.moe/v787s8.png">Car 3</option>
        <option value="https://files.catbox.moe/x2tjyv.png">Car 4</option>
      </select>
      <div id="player2-preview" class="car-preview"></div>

      <!-- Start Game button within Car Selection section -->
      <button onclick="showGameElements()">Start Game</button>
    </div>

    <!-- Game Status, Racetrack, and related information -->
    <div id="game-status" class="hidden">Binary Racing Game! Press "Start Game" to begin.</div>
    <div id="racetrack" class="hidden">
      <div id="finish-line"></div>
      <div id="car1" class="car" style="bottom: 0;"></div>
      <div id="car2" class="car" style="top: 0;"></div>
    </div>
    <div id="car-position" class="hidden">Player 1 Position: 0 | Player 2 Position: 0</div>
    <div id="target-number" class="hidden">Target Decimal Number: -</div>
    <input type="text" id="user-input" class="hidden" placeholder="Enter binary number">
    <button id="submit-button" onclick="submitGuess()" class="hidden">Submit Guess</button>
  </div>

  <!-- Message popup for correct/incorrect answers -->
  <div id="message-popup" class="hidden"></div>

<script>
  // Global variables
  let boardSize = 10;
  let currentPlayer = 1;
  let playerPositions = { 1: 0, 2: 0 };
  let currentTargetDecimalNumber;
  let player1Car, player2Car;
  let gameStarted = false;

  // Function to preview Car 1 on page load
  function previewCar1OnLoad() {
    const car1Url = "https://files.catbox.moe/l8nuox.png";
    previewCarImage('player1-preview', car1Url);
    const car2Url = "https://files.catbox.moe/zgi62v.png";
    previewCarImage('player2-preview', car2Url);
  }

  // Initialize car preview on page load
  window.onload = previewCar1OnLoad;

  // Show car selection and start the game
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

  // Display a message for a wrong answer
  function showWrongAnswerMessage() {
    const messagePopup = document.getElementById('message-popup');
    messagePopup.innerText = `Player ${currentPlayer} got the answer wrong!`;
    messagePopup.style.backgroundColor = '#ff0000';
    messagePopup.style.display = 'block';

    // Hide the message after a brief delay
    setTimeout(function () {
      messagePopup.style.display = 'none';
    }, 2000);
  }

  // Display a message for a correct answer
  function showCorrectAnswerMessage() {
    const messagePopup = document.getElementById('message-popup');
    messagePopup.innerText = `Player ${currentPlayer} got the answer right!`;
    messagePopup.style.backgroundColor = '#00ff00';
    messagePopup.style.display = 'block';

    // Hide the message after a brief delay
    setTimeout(function () {
      messagePopup.style.display = 'none';
    }, 2000);
  }

  // Update game status on the board
  function updateGameStatus() {
    document.getElementById('car-position').innerText = `Player 1 Position: ${playerPositions[1]} | Player 2 Position: ${playerPositions[2]}`;
    document.getElementById('car1').style.left = `${(playerPositions[1] / boardSize) * 100}%`;
    document.getElementById('car2').style.left = `${(playerPositions[2] / boardSize) * 100}%`;
  }

  // Update the target decimal number on the board
  function updateTargetNumber(targetDecimalNumber) {
    document.getElementById('target-number').innerText = `Target Decimal Number: ${targetDecimalNumber}`;
  }

  // Switch to the next player's turn
  function switchPlayer() {
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    document.getElementById('game-status').innerText = `It's Player ${currentPlayer}'s turn.`;
  }

  // Check if a player has won
  function checkWinner() {
    if (playerPositions[1] === boardSize) {
      playWinningAnimation(1);
      announceWinner(1);
      return true;
    } else if (playerPositions[2] === boardSize) {
      playWinningAnimation(2);
      announceWinner(2);
      return true;
    }
    return false;
  }

  // Generate a random number for the game loop
  function generateRandomNumber() {
    return Math.floor(Math.random() * 101);
  }

  // Main game loop
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

  // Submit player's guess
  function submitGuess() {
    const userInput = document.getElementById('user-input').value;
    try {
      const guessDecimal = parseInt(userInput, 2);
      if (guessDecimal === currentTargetDecimalNumber) {
        console.log(`Player ${currentPlayer} is correct! Their car moves forward by 1 space.`);
        showCorrectAnswerMessage();
        playerPositions[currentPlayer] += 1;
        switchPlayer();
        gameLoop();
      } else {
        console.log(`Player ${currentPlayer} is incorrect. The correct decimal number was ${currentTargetDecimalNumber}.`);
        showWrongAnswerMessage();
        switchPlayer();
      }
    } catch (error) {
      console.log("Invalid input. Please enter a valid binary number.");
    }
    document.getElementById('user-input').value = '';
  }

  // Show car selection section
  function showCarSelection() {
    document.getElementById('start-game').style.display = 'none';
    document.getElementById('car-selection').style.display = 'block';
  }

  // Preview car image for car selection
  function previewCarImage(playerPreviewId, imageUrl) {
    document.getElementById(playerPreviewId).style.backgroundImage = `url('${imageUrl}')`;
    document.getElementById(playerPreviewId).style.backgroundSize = 'contain';
  }

  // Start the game
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

  // Play winning animation for a player
  function playWinningAnimation(player) {
    const carElement = document.getElementById(`car${player}`);
    carElement.style.animation = 'winningAnimation 2s ease-in-out';
    setTimeout(() => {
      carElement.style.animation = '';
    }, 2000);
  }

  // Announce the winner
  function announceWinner(player) {
    console.log(`Player ${player} wins!`);
    const messagePopup = document.getElementById('message-popup');
    messagePopup.innerText = `Player ${player} wins!`;
    messagePopup.style.backgroundColor = '#00ff00';
    messagePopup.style.display = 'block';

    // Hide the message after a brief delay
    setTimeout(function () {
      messagePopup.style.display = 'none';
    }, 3000);
  }
</script>
</body>
</html>

