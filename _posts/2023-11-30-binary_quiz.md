---
toc: false
layout: post
hide: true
title: Binary Quiz
courses: { compsci: {week: 14 } } 
type: tangibles
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
</script>

<h1>Binary Number Guessing Game</h1>
<p>Convert the following binary number to decimal and enter the decimal value:</p>
<p><strong>${correctBinary}</strong> is: <strong>${correctDecimal}</strong> (in decimal)</p>

<!-- Button to trigger the guessing function -->
<button onclick="checkGuess()">Guess Now</button>

</body>
</html>
