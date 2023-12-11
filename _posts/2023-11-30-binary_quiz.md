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
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
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
     // Update the distance bars
        updateDistanceBar(userDecimalGuess);

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
