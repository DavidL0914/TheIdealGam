---
toc: false
layout: post
hide: true
title: 2 Player Racing Gam(e)
description: Rules are under Binary Gam(e) | Racing Game in the Overview blog
courses: { compsci: {week: 14 } } 
type: tangibles
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Race Game</title>
    <style>
        /* Styling for the game board */
        #game-board {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }
        /* Styling for the racetrack */
        #racetrack {
            width: 80%;
            height: 100px;
            border: 2px solid #000;
            position: relative;
            margin-bottom: 20px;
        }
        /* Styling for the cars */
        .car {
            width: 30px;
            height: 20px;
            position: absolute;
            transition: left 0.5s ease;
            margin-left: 5px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        /* Styling for Player 1's car */
        #car1 {
            background-color: #00f;
            top: 0;
        }
        /* Styling for Player 2's car */
        #car2 {
            background-color: #f00;
            bottom: 0;
        }
        /* Styling for game status */
        #game-status {
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
    <script src="script.js"></script>
</head>

<body>
    <div id="game-board">
        <!-- Game status display -->
        <div id="game-status">Binary Racing Game! It's Player 1's turn.</div>
        <!-- Racetrack with cars -->
        <div id="racetrack">
            <div id="car1" class="car"></div>
            <div id="car2" class="car"></div>
        </div>
        <!-- Display player positions -->
        <div id="car-position">Player 1 Position: 0 | Player 2 Position: 0</div>
        <!-- Display target decimal number -->
        <div id="target-number">Target Decimal Number: -</div>
        <!-- User input for binary guess -->
        <input type="text" id="user-input" placeholder="Enter binary number">
        <!-- Button to submit guess -->
        <button onclick="submitGuess()">Submit Guess</button>
    </div>
    <script>
        // Game configuration variables
        let boardSize = 10;
        let currentPlayer = 1;
        let playerPositions = { 1: 0, 2: 0 };
        let currentTargetDecimalNumber;
        // Function to update game status display
        function updateGameStatus() {
            document.getElementById('car-position').innerText = `Player 1 Position: ${playerPositions[1]} | Player 2 Position: ${playerPositions[2]}`;
            document.getElementById('car1').style.left = `${(playerPositions[1] / boardSize) * 100}%`;
            document.getElementById('car2').style.left = `${(playerPositions[2] / boardSize) * 100}%`;
        }
        // Function to update target decimal number display
        function updateTargetNumber(targetDecimalNumber) {
            document.getElementById('target-number').innerText = `Target Decimal Number: ${targetDecimalNumber}`;
        }
        // Function to switch player turns
        function switchPlayer() {
            currentPlayer = currentPlayer === 1 ? 2 : 1;
            document.getElementById('game-status').innerText = `It's Player ${currentPlayer}'s turn.`;
        }
        // Function to check for a winner
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
        // Function to generate a random target number
        function generateRandomNumber() {
            return Math.floor(Math.random() * 101); // Generate a number between 0 and 100
        }
        // Main game loop
        function gameLoop() {
            if (!checkWinner()) {
                currentTargetDecimalNumber = generateRandomNumber();
                const targetBinaryNumber = currentTargetDecimalNumber.toString(2);
                updateTargetNumber(currentTargetDecimalNumber);
                updateGameStatus();
            } else {
                console.log("Game over!");
            }
        }
        // Function to handle user's guess submission
        function submitGuess() {
            const userInput = document.getElementById('user-input').value;
            try {
                const guessDecimal = parseInt(userInput, 2);
                if (guessDecimal === currentTargetDecimalNumber) {
                    console.log(`Player ${currentPlayer} is correct! Their car moves forward by 1 space.`);
                    playerPositions[currentPlayer] += 1;
                    switchPlayer();
                    gameLoop(); // Continue the game loop
                } else {
                    console.log(`Player ${currentPlayer} is incorrect. The correct decimal number was ${currentTargetDecimalNumber}.`);
                    switchPlayer();
                }
            } catch (error) {
                console.log("Invalid input. Please enter a valid binary number.");
            }
            document.getElementById('user-input').value = ''; // Clear the input field
        }
        // Start the game loop
        gameLoop();
    </script>
</body>
</html>