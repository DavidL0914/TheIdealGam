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
            width: 50px; /* Adjust the width as needed */
            height: 30px; /* Adjust the height as needed */
            position: absolute;
            transition: left 0.5s ease;
            margin-top: 10px;
            background-size: cover;
        }
        /* Styling for the car preview */
        .car-preview {
            width: 100px;
            height: 50px;
            background-size: cover;
            margin-top: 10px;
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
        <!-- Start game button -->
        <button id="start-game" onclick="showCarSelection()">Start Game</button>
        
        <!-- Car selection screen -->
        <div id="car-selection" style="display: none;">
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

            <button onclick="startGame()">Start Game</button>
        </div>

        <!-- Game status display -->
        <div id="game-status">Binary Racing Game! Press "Start Game" to begin.</div>
        
        <!-- Racetrack with cars -->
        <div id="racetrack">
            <div id="car1" class="car" style="bottom: 0;"></div>
            <div id="car2" class="car" style="top: 0;"></div>
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
        let player1Car, player2Car;
        
        // Flag to check if the game has started
        let gameStarted = false;

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
            if (!checkWinner() && gameStarted) {
                currentTargetDecimalNumber = generateRandomNumber();
                const targetBinaryNumber = currentTargetDecimalNumber.toString(2);
                updateTargetNumber(currentTargetDecimalNumber);
                updateGameStatus();
            } else if (gameStarted) {
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

        // Function to show car selection screen
        function showCarSelection() {
            document.getElementById('start-game').style.display = 'none';
            document.getElementById('car-selection').style.display = 'block';
        }

        // Function to preview selected car image
        function previewCarImage(previewElementId, imageUrl) {
            document.getElementById(previewElementId).style.backgroundImage = `url('${imageUrl}')`;
        }

        // Function to start the game
        function startGame() {
            if (!gameStarted) {
                // Get selected car images
                player1Car = document.getElementById('player1-car').value;
                player2Car = document.getElementById('player2-car').value;

                // Hide car selection screen
                document.getElementById('car-selection').style.display = 'none';

                // Set car images and initial positions
                document.getElementById('car1').style.backgroundImage = `url('${player1Car}')`;
                document.getElementById('car2').style.backgroundImage = `url('${player2Car}')`;
                document.getElementById('car1').style.bottom = '0';
                document.getElementById('car2').style.top = '0';

                // Enable/disable start game button
                document.getElementById('start-game').disabled = true;
                gameStarted = true;

                // Start the game loop
                gameLoop();
            }
        }
    </script>
</body>
</html>