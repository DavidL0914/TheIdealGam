---
toc: False
layout: default
hide: True
title: Binary Gam(e) | Binary Puzzle
courses: {'compsci': {'week': 14}}
type: tangibles
---
<html>
{% assign BITS = 8 %}

<style>
    td {
        text-align: center;
        vertical-align: middle;
    }
</style>
<div id = "display">hi</div>    
<table>
    <thead>
        <tr class="header" id="table">
            <th class = "th">Double</th>
            <th class = "th">Binary</th>
            <th class = "th">Halve</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><div class='button' id ='leftshift' onclick='leftShift()'>*2</div></td>
            <td id="binary">00000000</td>
            <td><div class='button' id ='rightshift' onclick='rightShift()'>/2</div></td>
        </tr>
    </tbody>
</table>

{% comment %}
Liquid for loop includes last number, thus the Minus
{% endcomment %}
{% assign bits = BITS | minus: 1 %} 

<table>
    <thead>
        <tr>
            {% comment %}
            Build many bits
            {% endcomment %}
            {% for i in (0..bits) %}
            <th><img class = "onoff" id="tree{{ i }}" src="{{site.baseurl}}/images/off.png" alt="" width="70" height="Auto">
                <div class="button" id="lit{{ i }}" onclick="javascript:toggleBit({{ i }})">Turn on</div>
            </th>
            {% endfor %}
        </tr>
    </thead>
    <tbody> 
        <tr>
            {% comment %}
            Value of bit
            {% endcomment %}
            {% for i in (0..bits) %}
            <td><input type='text' id="digit{{ i }}" Value="0" size="1" readonly></td>
            {% endfor %}
        </tr>
    </tbody>
</table>
<div id = "result"></div>
<script>
    let changes = 0
    const BITS = {{ BITS }};
    const MAX = 2 ** BITS - 1;
    const MSG_ON = "Turn on";
    const IMAGE_ON = "{{site.baseurl}}/images/on.png";
    const MSG_OFF = "Turn off";
    const IMAGE_OFF = "{{site.baseurl}}/images/off.png"
    function checkChanges() {
    const currentBinary = getBits();
    console.log(currentBinary)
    if (changes === result.steps) {
        if (currentBinary === targetBinary) {
            console.log(targetBinary)
            console.log("You've successfully completed the game!");
            document.getElementById("result").innerHTML = "Congratulations! You've successfully completed the game!";
            changes = 0;
            displayResults();
        }
        else {
            console.log("Too many changes! Try again.");
            document.getElementById("result").innerHTML = "Womp womp... Too many changes! Try Again.";
            changes = 0;
            displayResults();
    }
}
}
    // return string with current value of each bit
    function getBits() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
            bits = bits + document.getElementById('digit' + i).value;
        }
        return bits;
    }
    // setter for Document Object Model (DOM) values
    function setConversions(binary) {
        document.getElementById('binary').innerHTML = binary;
        // Decimal conversion
    }
    // convert decimal to base 2 using modulo with divide method
    function decimal_2_base(decimal, base) {
        let conversion = "";
        // loop to convert to base
        do {
            let digit = decimal % base;           // obtain right most digit
            conversion = "" + digit + conversion; // what does this do? inserts digit to front of string
            decimal = ~~(decimal / base);         // what does this do? divides by base what is ~~? force whole number
        } while (decimal > 0);                    // why while at the end? 0 pads front of binary number
            // loop to pad with zeros
            if (base === 2) {                     // only pad for binary conversions
                for (let i = 0; conversion.length < BITS; i++) {
                    conversion = "0" + conversion;
            }
        }
        return conversion;
    }
    // toggle selected bit and recalculate
    function toggleBit(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digit' + i);
        const image = document.getElementById('tree' + i);
        const lit = document.getElementById('lit' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
            dig.value = 0;
            image.src = IMAGE_OFF;
            lit.innerHTML = MSG_ON;
            changes++;
            checkChanges();
        } else {
            dig.value = 1;  
            image.src = IMAGE_ON;
            lit.innerHTML = MSG_OFF;
            changes++;
            checkChanges();
        }
        // Binary numbers
        const binary = getBits();
        setConversions(binary);
    }
    // Function for left shift
    function leftShift() {
        let binary = getBits();
        binary = binary.slice(1) + '0';  // Shift all bits to the left and add a '0' at the end
        updateBinary(binary);
        changes++;
        checkChanges()
    }

    // Function for right shift
    function rightShift() {
        let binary = getBits();
        binary = '0' + binary.slice(0, -1);  // Add a '0' at the beginning and remove the last bit
        updateBinary(binary);
        changes++;
        checkChanges()
    }

    // Helper function to update the binary representation and visuals
    function updateBinary(binary) {
        setConversions(binary);
        for (let i = 0; i < binary.length; i++) {
            let digit = binary.substr(i, 1);
            document.getElementById('digit' + i).value = digit;
            if (digit === "1") {
                document.getElementById('tree' + i).src = IMAGE_ON;
                document.getElementById('lit' + i).innerHTML = MSG_OFF;
            } else {
                document.getElementById('tree' + i).src = IMAGE_OFF;
                document.getElementById('lit' + i).innerHTML = MSG_ON;
            }
        }
    }
function minActionsToTransformBinary(start, target) {
    const queue = [{ current: start, actions: [], steps: 0 }];
    const visited = new Set([start]);

    while (queue.length > 0) {
        const { current, actions, steps } = queue.shift();

        if (current === target) {
            return { actions, steps };
        }

        for (let i = 0; i < current.length; i++) {
            const newBinary = current.slice(0, i) + (current[i] === '1' ? '0' : '1') + current.slice(i + 1);
            if (!visited.has(newBinary)) {
                visited.add(newBinary);
                queue.push({ current: newBinary, actions: actions.concat(`Swap bit at position ${i}`), steps: steps + 1 });
            }
        }

        if (current.length === target.length) {
            const leftShift = current.slice(1) + '0';
            if (!visited.has(leftShift)) {
                visited.add(leftShift);
                queue.push({ current: leftShift, actions: actions.concat('Left shift'), steps: steps + 1 });
            }
        }

        if (current.length === target.length) {
            const rightShift = '0' + current.slice(0, -1);
            if (!visited.has(rightShift)) {
                visited.add(rightShift);
                queue.push({ current: rightShift, actions: actions.concat('Right shift'), steps: steps + 1 });
            }
        }
    }

    return null; // If transformation is not possible
}

  function displayResults() {
    startBinary = generateRandomBinary();
    targetBinary = generateRandomBinary();
    result = minActionsToTransformBinary(startBinary, targetBinary);

    console.log(`Actions to transform ${startBinary} to ${targetBinary}:`);
    if (result) {
      result.actions.forEach((action, index) => {
        console.log(`${index + 1}. ${action}`);
      });
      console.log(`Number of steps: ${result.steps}`);
    } else {
      console.log("Transformation not possible.");
    }

    document.getElementById("display").innerHTML = "Goal: Transform " + startBinary + " to " + targetBinary + " in " + result.steps + " steps";
    updateBinary(startBinary)
  }

function generateRandomBinary() {
    let binaryNumber = '';
    for (let i = 0; i < 8; i++) {
        // Generate a random bit (0 or 1)
        const randomBit = Math.round(Math.random());
        binaryNumber += randomBit;
        }
    console.log(binaryNumber)
    return binaryNumber;
}
displayResults();
</script>
</html>