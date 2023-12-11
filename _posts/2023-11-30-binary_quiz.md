---
toc: false
layout: post
title: Binary Quiz
courses: { compsci: {week: 14 } } 
type: tangibles
hide: true
---
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

<script>
    // Generate a random decimal number between 0 and 255

    // Function to convert decimal to binary with leading zeroes
    function decimalToBinary(decimal) {
        // Use toString(2) to convert to binary and padStart to add leading zeroes
        return decimal.toString(2).padStart(8, '0');
    }

    // Convert the decimal number to binary

    // Function to check the user's input
    function checkGuess() {
        // Get the user's input
        const correctDecimal = Math.floor(Math.random() * 256);
        const correctBinary = decimalToBinary(correctDecimal);
        const userDecimalGuess = parseInt(prompt(`Convert ${correctBinary} to decimal and enter the decimal value:`));

        // Check if the guess is correct
        if (userDecimalGuess === correctDecimal) {
            alert('Congratulations! You guessed the correct decimal value.');
        } else {
            alert(`Sorry, the correct decimal value was ${correctDecimal}. Try again!`);
        }m

    }   
         // Check if the guess is correct
        const resultElement = document.getElementById('result');
        if (userDecimalGuess === correctDecimal) {
            resultElement.textContent = 'Congratulations! You guessed the correct decimal value.';
        } else {
            resultElement.textContent = `Sorry, the correct decimal value was ${correctDecimal}. Try again!`;
        }

        // Update the distance bars
        updateDistanceBar(userDecimalGuess); {
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

<h1>Binary Number Guessing Game</h1>
<p>Convert the following binary number to decimal and enter the decimal value:</p>

<!-- Button to trigger the guessing function -->
<button onclick="checkGuess()">Guess Now</button>

</body>
</html>
