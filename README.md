# Prelim_Study
 
Running app.py runs the complete study on localhost 

The Static folder holds all the css, image, and JavaScript files. Each webpage calls a different JavaScript file in the static folder.
-- the script for each bar chart is in the js folder. They are organized by chart density.

There are 5 blueprints for routing in app.py. 'training' routes through the training pages which passes to 'first_set,' 'second_set,' and 'third_set,' which route through 3 different stimuli each (observation, mask, response). Finally 'SpAb' routes through the paper folding exercise which passes back to app.py for the final pages.