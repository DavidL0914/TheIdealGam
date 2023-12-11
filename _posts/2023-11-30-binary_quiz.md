---
toc: false
layout: post
title: Binary Quiz
courses: { compsci: {week: 14 } } 
type: tangibles
hide: true
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Number Guessing Game</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin: 50px;
            background-color: #f7f7f7;
        }

        h1 {
            color: #333;
        }

        p {
            color: #555;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #3498db;
            color: #fff;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #2980b9;
        }

        #result {
            margin-top: 20px;
            font-size: 18px;
        }

        #binaryDisplay {
            font-size: 24px;
            margin-bottom: 20px;
        }

        #decimalRange {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }

        .distanceBar {
            width: 100%;
            height: 20px;
            position: relative;
            margin-top: 20px;
            background-color: #ecf0f1;
        }

        .distanceFill {
            height: 100%;
            position: absolute;
        }

        .distanceText {
            position: absolute;
            bottom: -20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 12px;
            color: #333;
        }

        #actualDistanceBar {
            margin-bottom: 10px;
        }

        #actualDistanceFill {
            background-color: #2ecc71;
        }

        #guessedDistanceFill {
            background-color: #e74c3c;
        }
    </style>
</head>
<body>

<h1>Binary Number Guessing Game</h1>
<p>Convert the following binary number to decimal and enter the decimal value:</p>

<!-- Display the binary version on the screen -->
<div id="binaryDisplay"></div>

<!-- Provide an input field for the user's guess -->
<label for="userGuess">Enter your guess in decimal:</label>
<input type="text" id="userGuess">
<button onclick="checkGuess()">Guess Now</button>
<button onclick="reload()">Try Again</button>

<!-- Display the result on the page -->
<div id="result"></div>

<!-- Display the decimal range -->
<div id="decimalRange">
    <span>0</span>
    <span>255</span>
</div>

<!-- Display the distance bars -->
<div class="distanceBar" id="actualDistanceBar">
    <div class="distanceFill" id="actualDistanceFill"></div>
    <span class="distanceText">Actual Value</span>
</div>

<div class="distanceBar" id="guessedDistanceBar">
    <div class="distanceFill" id="guessedDistanceFill"></div>
    <span class="distanceText">Guessed Value</span>
</div>

<script>
    function reload() {
        location.reload()
    }
    // Function to convert decimal to binary with leading zeroes
    function decimalToBinary(decimal) {
        // Use toString(2) to convert to binary and padStart to add leading zeroes
        return decimal.toString(2).padStart(8, '0');
    }

    // Generate a random decimal number between 0 and 255
    const correctDecimal = Math.floor(Math.random() * 256);

    // Convert the decimal number to binary
    const correctBinary = decimalToBinary(correctDecimal);

    // Display the binary version on the screen after the page has loaded
    document.getElementById('binaryDisplay').textContent = `Binary: ${correctBinary}`;

    // Function to check the user's input
    function checkGuess() {
        // Get the user's input
        const userDecimalGuess = parseInt(document.getElementById('userGuess').value);

        // Check if the guess is correct
        const resultElement = document.getElementById('result');
        if (userDecimalGuess === correctDecimal) {
            resultElement.textContent = 'Congratulations! You guessed the correct decimal value.';
        } else {
            resultElement.textContent = `Sorry, the correct decimal value was ${correctDecimal}. Try again!`;
        }

        // Update the distance bars
        updateDistanceBar(userDecimalGuess);
    }

    // Function to update the distance bars
    function updateDistanceBar(userDecimalGuess) {
        const maxDistance = 255;
        const actualDistancePercentage = (correctDecimal / maxDistance) * 100;
        const guessedDistancePercentage = (userDecimalGuess / maxDistance) * 100;

        // Update the width of the distance fills in the bars
        document.getElementById('actualDistanceFill').style.width = `${actualDistancePercentage}%`;
        document.getElementById('guessedDistanceFill').style.width = `${guessedDistancePercentage}%`;
    }
</script>

</body>
</html