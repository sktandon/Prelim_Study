const radius = 30;
const gap = 10;
var magicNumber;
var numRight = 0;
var numWrong = 0;

var canvas;
var ctx;

var components = [];

(function repeat() {
    magicNumber = Math.floor(Math.random()*8)+1;
    setTimeout(repeat, 7000);
})();

function start() {
    canvas = document.getElementById('canvas');
    ctx = canvas.getContext('2d');

    canvas.addEventListener('click', (e) => {
        mousePoint = getCursorPosition(e);
        components.forEach(circle => {
            if (isIntersect(mousePoint, circle)) {
                var correctText = ":)";
                var incorrectText = ":(";
                if (circle.text == magicNumber.toString())
                {
                    circle.text = correctText;
                    circle.color = "rgb(100,255,100)"; //green
                    numRight++;
                    console.log("num right: " + numRight + ", num wrong: " + numWrong);
                }
                else if (circle.text != correctText && circle.text != incorrectText)
                {
                    circle.text = incorrectText;
                    circle.color = "rgb(255,100,100)"; //red
                    numWrong++;
                    console.log("num right: " + numRight + ", num wrong: " + numWrong);
                }
            }
        });
    });

    setInterval(updateGame, 25);
}

function component(x, y, text, color) {
    this.radius = radius;
    this.text = text;
    this.x = x;
    this.y = y;
    this.origY = y;
    this.color = color;
    this.yVelocity = 1;
    this.move = function() {
        this.x = this.x + 2;
        this.y += this.yVelocity;
        if (this.y > this.origY + 5 || this.y < this.origY - 5)
        {
            this.yVelocity = this.yVelocity * -1; //bouncy bouncy
        }
    }
    this.draw = function() {
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
        ctx.fill();
        ctx.fillStyle = "black";
        ctx.stroke();
        ctx.font = "20px Arial";
        ctx.fillText(this.text, this.x-5, this.y+5)
    }
}

function updateComponentList() {
    //add new components if there's room
    var lowestX = Number.MAX_VALUE;

    components.forEach(component => {
        lowestX = Math.min(lowestX, component.x);
    });

    if (lowestX > radius + gap)
    {
        var randInt = Math.floor(Math.random() * 3) + magicNumber - 1; //If magicNumber is 3, random is from 2 to 4
        components.push(new component(-1*radius, 50, randInt.toString(), "rgb(242,228,219)"));
    }

    //remove components that have fallen off the edge already
    components = components.filter(component => component.x < canvas.getBoundingClientRect().right + radius)
}

function updateGame() {
    clear();
    components.forEach(component => {
        component.move();
        component.draw();
    });
    updateComponentList();
}

function clear() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    ctx.font = "20px Arial";
    ctx.fillText("Click all the "+magicNumber+"s!",130,145);
}

function isIntersect(point, circle) {
    return Math.sqrt((point.x-circle.x) ** 2 + (point.y - circle.y) ** 2) < circle.radius;
}

function getCursorPosition(event) {
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left
    const y = event.clientY - rect.top
    return {x: x, y: y};
}

