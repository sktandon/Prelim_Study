var notes = ["Great Job! Let's try another chart, click Next when you're ready and don't forget to play the game!", 
"Awesome - click next when you're ready!",
"Let's do another chart. Keep playing the game!",
"Fantastic! Keep going!",
"You're doing great - let's do another one.",
"Click next when you're ready to do another chart!",
"Make sure you're playing the game while looking at the chart!",
"You're doing so well! Keep going!",
"Let's do another one! You know the drill.",
"Don't forget to play the game! Click Next when you're ready"]

document.getElementById("noteDisplay").innerHTML = "<h1>" + 
                                                    notes[Math.floor(Math.random()* notes.length)] + "</h1>";