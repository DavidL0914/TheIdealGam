---
toc: false
layout: post
hide: true
title: Binary Gam(e) | Binary RPG
description: Overview of how we will develop a binary RPG game using Binary to reinforce binary memorization.
courses: { compsci: {week: 15 } }
type: blogs
---

{% include nav.html %}


**In this game the player will be forced to memorize the binary alphabet in order to solve quests and receive awards**
- Players must embark on quests and use the binary form of words to fight monsters and complete tasks.
- Players will be given a certain number of turns to complete a task. 
- Different regions can be unlocked which can provide access to harder words as well as powerups that allow you to skip certain words to receive assitance. 

The user must turn the starting binary into a word which can be found on their screen in the number of actions.

**The user will be able to:**
- Type out certain sections of binary
- If the binary is incorrect, it will show which values are incorrect and return which values are correct. 
- The user will be able to complete tasks based on this idea. 

**This will:**
- Challenge the user to really think about binary, and how the binary alphabet works

**How will we accomplish this?**
- Provide tasks that gradually become more difficult. I.E if there is a wall, the player must type out wall in binary in order to scale the wall
- Algorithm that compares the given value to the actual value. 
- Take the numbers that display the wrong values using list operations.

**What will we use?**
- JavaScript, HTML & a bit of CSS
- List operations
- Use variable/set to keep track of already checked combinations
![Screenshot 2023-11-15 at 11.51.01 PM.png](<attachment:Screenshot 2023-11-15 at 11.51.01 PM.png>)

![Screenshot 2023-11-16 at 9.53.23 AM.png](<attachment:Screenshot 2023-11-16 at 9.53.23 AM.png>)


```javascript
%%javascript
function compareBinary(int) {
    var userArray= Array(5);
  
    const digits = String(int) // converts user input into a string
      .split('')  // splits up the string into seperate values
      .map(Number); // maps the split string onto the array.
      
    for(let x =0; x<int; x++) { 
       // compares the value of user array  
    }
}