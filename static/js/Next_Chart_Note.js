var notes = ["Great Job! Let's try another chart, and don't forget to play the game!", 
"Awesome job!",
"Let's do another chart. Keep playing the game!",
"Fantastic! Keep going!",
"You're doing great - let's do another one.",
"Almost time for another chart!",
"Make sure you're playing the game while looking at the chart!",
"You're doing so well! Keep going!",
"Let's do another one! You know the drill.",
"Don't forget to play the game!",
"Fabulous work!",
"Keep going, we're cheering you on!!",
"Great work - ready for another?"]

document.getElementById("noteDisplay").innerHTML = "<h1>" + 
                                                    notes[Math.floor(Math.random()* notes.length)] + "</h1>";