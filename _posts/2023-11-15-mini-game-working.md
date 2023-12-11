---
toc: False
layout: post
title: Binary Word Game
description: The Word Game!
courses: {'compsci': {'week': 14}}
type: tangibles
hide: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Word Guessing Game</title>
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
function getRandomWord() {
    const words = ["david", "kayden", "matthew", "developer", "coding", "binary"];
    const randomIndex = Math.floor(Math.random() * words.length);
    return words[randomIndex];
  }
  
  function wordToBinary(word) {
    return Array.from(word).map(char => char.charCodeAt(0).toString(2)).join(' ');
  }
  
  function playBinaryWordGuessingGame() {
    const secretWord = getRandomWord();
    const binaryRepresentation = wordToBinary(secretWord);
    const wordLength = secretWord.length;
    let attempts = 0;
  
    alert("Welcome to the Binary Word Guessing Game!");
    alert(`Try to guess the binary representation of the word: ${secretWord}`);
  
    function makeGuess() {
      const playerGuess = prompt("Enter your binary word guess:");
  
      if (playerGuess !== binaryRepresentation) {
        alert(`Incorrect guess. For tester purposes the correct binary representation is: ${binaryRepresentation}`);
        attempts++;
        makeGuess();
      } else {
        alert(`Congratulations! You guessed the correct binary representation "${binaryRepresentation}" of the word "${secretWord}" in ${attempts} attempts.`);
        askToPlayAgain();
      }
    }
  
    function askToPlayAgain() {
      const playAgain = confirm("Do you want to play again?");
      if (playAgain) {
        playBinaryWordGuessingGame();
      } else {
        alert("Thanks for playing! Goodbye.");
      }
    }
  
    makeGuess();
  } 

  function getRandomBinarySequence(length) {
  let binarySequence = '';
  for (let i = 0; i < length; i++) {
    binarySequence += Math.round(Math.random());
  }
  return binarySequence;
}

function binaryToAscii(binarySequence) {
  const binaryArray = binarySequence.match(/.{1,8}/g); // Split binary into groups of 8 bits
  const asciiChars = binaryArray.map(binary => String.fromCharCode(parseInt(binary, 2)));
  return asciiChars.join('');
}

function playBinaryToAsciiGuessingGame() {
  const binaryLength = 32; // You can adjust the length as desired
  const secretBinarySequence = getRandomBinarySequence(binaryLength);
  const asciiRepresentation = binaryToAscii(secretBinarySequence);
  let attempts = 0;

  alert("Welcome to the Binary to ASCII Guessing Game!");
  alert(`Try to guess the ASCII representation of the binary sequence: ${secretBinarySequence}`);

  function makeGuess() {
    const playerGuess = prompt("Enter your ASCII guess:");

    if (playerGuess !== asciiRepresentation) {
      alert(`Incorrect guess. The correct ASCII representation is: ${asciiRepresentation}`);
      attempts++;
      makeGuess();
    } else {
      alert(`Congratulations! You guessed the correct ASCII representation "${asciiRepresentation}" of the binary sequence "${secretBinarySequence}" in ${attempts} attempts.`);
      askToPlayAgain();
    }
  }

  function askToPlayAgain() {
    const playAgain = confirm("Do you want to play again?");
    if (playAgain) {
      playBinaryToAsciiGuessingGame();
    } else {
      alert("Thanks for playing! Goodbye.");
    }
  }

  makeGuess();
}
function wordToAscii(word) {
  return Array.from(word).map(char => char.charCodeAt(0)).join(' ');
}

function playWordToAsciiGuessingGame() {
  const secretWord = getRandomWord();
  const asciiRepresentation = wordToAscii(secretWord);
  let attempts = 0;

  alert("Welcome to the Word to ASCII Guessing Game!");
  alert(`Try to guess the ASCII representation of the word: ${secretWord}`);

  function makeGuess() {
    const playerGuess = prompt("Enter your ASCII guess:");

    if (playerGuess !== asciiRepresentation) {
      alert(`Incorrect guess. The correct ASCII representation is: ${asciiRepresentation}`);
      attempts++;
      makeGuess();
    } else {
      alert(`Congratulations! You guessed the correct ASCII representation "${asciiRepresentation}" of the word "${secretWord}" in ${attempts} attempts.`);
      askToPlayAgain();
    }
  }

  function askToPlayAgain() {
    const playAgain = confirm("Do you want to play again?");
    if (playAgain) {
      playWordToAsciiGuessingGame();
    } else {
      alert("Thanks for playing! Goodbye.");
    }
  }

  makeGuess();
}

function playRandomGame() {
      const randomIndex = Math.floor(Math.random() * 3); // Choose a number between 0 and 2
      switch (randomIndex) {
        case 0:
          playBinaryWordGuessingGame();
          break;
        case 1:
          playBinaryToAsciiGuessingGame();
          break;
        case 2:
          playWordToAsciiGuessingGame();
          break;
        default:
          alert("Error: Unknown game.");
      }
}

</script>

<h1>Binary/Ascii Word Guessing Game</h1>
<p>In order to convert text into binary, you must first convert each letter into its ASCII value. For example, A is 65. You must then convert this decmimal value into binary.
   For example 
    H has an ASCII value of 72, which in binary is 01001000.
    E has an ASCII value of 69, which in binary is 01000101.
    L has an ASCII value of 76, which in binary is 01001100.
    L has an ASCII value of 76, which in binary is 01001100.
    O has an ASCII value of 79, which in binary is 01001111.
</p>
<!-- Button to trigger the guessing function -->
<button onclick="playWordToAsciiGuessingGame()">Word to Ascii</button>
<button onclick="playBinaryToAsciiGuessingGame()">Binary to Ascii</button>
<button onclick="playBinaryWordGuessingGame()">Binary to Word</button>

<button onclick="playRandomGame()">CHALLENGE</button>



</body>
</html>