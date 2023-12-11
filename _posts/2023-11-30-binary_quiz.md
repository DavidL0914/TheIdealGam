<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Number Guessing Game</title>
    <style>
        /* Your CSS styles here */
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
    // Declare correctDecimal outside the checkGuess function
    let correctDecimal;

    // Generate a random decimal number between 0 and 255
    function generateRandomDecimal() {
        return Math.floor(Math.random() * 256);
    }

    // Function to convert decimal to binary with leading zeroes
    function decimalToBinary(decimal) {
        // Your implementation here
    }

    // Convert the decimal number to binary

    // Function to check the user's input
    function checkGuess() {
        // Get the user's input
        correctDecimal = generateRandomDecimal();
        const correctBinary = decimalToBinary(correctDecimal);
        const userDecimalGuess = parseInt(prompt(`Convert ${correctBinary} to decimal and enter the decimal value:`));

        // Check if the guess is correct
        if (userDecimalGuess === correctDecimal) {
            alert('Congratulations! You guessed the correct decimal value.');
        } else {
            alert(`Sorry, the correct decimal value was ${correctDecimal}. Try again!`);
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
</html>
