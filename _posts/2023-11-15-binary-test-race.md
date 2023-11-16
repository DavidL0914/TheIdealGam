---
toc: false
layout: post
hide: true
title: Racing game - DEMO!
description: The Racing Game!
courses: { compsci: {week: 15 } }
type: hacks
---

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Binary Race Game</title>
  <script src="script.js"></script>
</head>

<body>
  <!-- You can add HTML content or leave it empty for a simple game -->
</body>

<script>
    function playBinaryRaceGame() {
    console.log("Welcome to the Binary Race Game!");
    console.log("Type in binary numbers to match the given decimal number and move your car forward.");
  
    const boardSize = 10;
    let carPosition = 0;
  
    while (carPosition < boardSize) {
        // Generate a new random decimal number for the user to match
        const targetDecimalNumber = Math.floor(Math.random() * 256);
  
        // Convert the decimal number to binary
        const targetBinaryNumber = targetDecimalNumber.toString(2);
  
        // Get user's guess
        const userGuess = prompt(`Your car is at position ${carPosition}. Match this number (in binary): ${targetDecimalNumber}`);
  
        try {
            // Convert the user's binary input to decimal
            const guessDecimal = parseInt(userGuess, 2);
  
            // Check if the guess is correct
            if (guessDecimal === targetDecimalNumber) {
                console.log("Correct! Your car moves forward by 1 space.");
                carPosition += 1;
            } else {
                console.log(`Incorrect guess. The correct decimal number was ${targetDecimalNumber}.`);
            }
  
        } catch (error) {
            console.log("Invalid input. Please enter a valid binary number.");
        }
    }
  
    console.log("Congratulations! You crossed the finish line and won the game!");
  }
  
  // Start the game
  playBinaryRaceGame();
    </script>
</html>
