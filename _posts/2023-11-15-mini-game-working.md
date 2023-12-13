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
        var words = ["David", "Kayden", "Matthew", "Binary", "Coding", "Andrew", "Ascii"];
        return words[Math.floor(Math.random() * words.length)];
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
    function WordToAscii() {
        var randomWord = getRandomWord();
        var randomChar = getRandomChar(randomWord);
        var asciiValue = randomChar.charCodeAt(0);

        var userGuess = prompt("Guess the ASCII value of the character '" + randomChar + "':");

        if (parseInt(userGuess) === asciiValue) {
            alert("Congratulations! You guessed the ASCII value correctly.");
        } else {
            alert("Sorry, that's incorrect. The ASCII value of '" + randomChar + "' is " + asciiValue + ".");
        }
    }

    function getRandomChar(word) {
        return word.charAt(Math.floor(Math.random() * word.length));
    }

  function WordToBinary() {
        var randomWord = getRandomWord();
        var binaryValues = convertWordToBinary(randomWord);

        var userGuess = prompt("Guess the binary representation of the word '" + randomWord + "':");

        if (userGuess === binaryValues.join(' ')) {
            alert("Congratulations! You guessed the binary representation correctly.");
        } else {
            alert("Sorry, that's incorrect. The correct binary representation is: " + binaryValues.join(' '));
        }
    }

    function getRandomWord() {
        var words = ["apple", "banana", "orange", "python", "coding", "gpt", "programming"];
        return words[Math.floor(Math.random() * words.length)];
    }

    function convertWordToBinary(word) {
        var binaryValues = [];
        for (var i = 0; i < word.length; i++) {
            var asciiValue = word.charCodeAt(i);
            var binaryValue = (asciiValue >>> 0).toString(2);
            binaryValues.push(binaryValue);
        }
        return binaryValues;
    }
function playGame() {
        var randomWord = getRandomWord();
        var randomChar = getRandomChar(randomWord);

        var userAsciiGuess = prompt("Enter the ASCII value for the character '" + randomChar + "':");
        var asciiValue = randomChar.charCodeAt(0);

        if (parseInt(userAsciiGuess) === asciiValue) {
            alert("Correct! ASCII value is: " + asciiValue);

            var userBinaryGuess = prompt("Now, enter the binary representation of the ASCII value:");
            var binaryValue = asciiValue.toString(2);

            if (userBinaryGuess === binaryValue) {
                alert("Congratulations! You guessed the binary representation correctly.");
            } else {
                alert("Sorry, that's incorrect. The correct binary representation is: " + binaryValue);
            }
        } else {
            alert("Sorry, that's incorrect. The ASCII value of '" + randomChar + "' is " + asciiValue + ".");
        }
    }

    

    function getRandomChar(word) {
        return word.charAt(Math.floor(Math.random() * word.length));
    }


     function playBinaryToAscii() {
        var randomAsciiValue = getRandomAsciiValue();
        var userBinaryGuess = prompt("Guess the binary representation of the ASCII value " + randomAsciiValue + ":");

        var binaryValue = convertToBinary(randomAsciiValue);

        if (userBinaryGuess === binaryValue) {
            alert("Congratulations! You guessed the binary representation correctly.");
        } else {
            alert("Sorry, that's incorrect. The correct binary representation is: " + binaryValue);
        }
    }

    function getRandomAsciiValue() {
        return Math.floor(Math.random() * 128); // Generates a random ASCII value between 0 and 127
    }

    function convertToBinary(asciiValue) {
        return (asciiValue >>> 0).toString(2); // Convert ASCII value to binary
    }
</script>

<h1>Binary/Ascii Word Guessing Game</h1>
<p>In order to convert text into binary, you must first convert each letter into its ASCII value. For example, A is 65. You must then convert this decmimal value into binary. Here are short mini games to help you through the process.</p>

<!-- Button to trigger the guessing function -->
<button onclick="WordToAscii()">Word to Ascii</button>
<button onclick="playBinaryToAscii()">Ascii to Binary</button>
<button onclick="WordToBinary()">Binary to Word</button>
<button onclick="playGame()">Start ASCII Binary Guessing Game</button>
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flinuxhint.com%2Fwp-content%2Fuploads%2F2022%2F02%2Fword-image-536.png&f=1&nofb=1&ipt=deb50b410b804e66a199ffb703b6a6ba87940452a40c6c598ca402f2ff2dce1c&ipo=images" alt=" Ascii Image">
</body>
</html>