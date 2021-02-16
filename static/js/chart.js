

//--------------- VERTICAL --------------------

var margin = {top: 20, right: 40, bottom: 20, left: 40},
    widthY = 700 - margin.left - margin.right,
    heightY = 500 - margin.top - margin.bottom,
    delim = 10;

var stimulusclicks = 0;

var maxy = d3.max(data, function(d) { return d.value; });

var scaleY = d3.scaleLinear()
    .domain([0, maxy+0.5])
    .rangeRound([heightY, 0]);

var x = d3.scaleLinear()
    .domain([0, data.length])
    .rangeRound([0, widthY]);

var svgY = d3.select('#mycard')
    .append("svg")
    .attr("width", widthY +10)
    .attr("height", heightY +40)
    .append('g');

/*svgY
    .on("end", function(){
        stimulusclicks++
    })*/


svgY
    .append('rect')
    .attr('x', 0)
    .attr('y', 0)
    .style('stroke', 'black')
    .style('fill', 'white')
    .attr('width', widthY+5)
    .attr('height', heightY+5);


// Arrows
svgY
.append('defs').append("marker")
.attr("id", "arrow")
.attr("refX", 6)
.attr("refY", 6)
.attr("markerWidth", 30)
.attr("markerHeight", 30)
//.attr("markerUnits","userSpaceonUse")
.attr("orient", "auto")
.append("path")
.attr("class", "marker")
.attr("d", "M 0 0 12 6 0 12 3 6")
.style("fill", "red");

//filter to only 0.5 values
arrowData = data.filter(x=>(x.value==0.5 || x.value==0.2))
//loop through each one
for (i=0; i<arrowData.length; i++)
{
//get the width of the entire svg
width = d3.select("#mycard").select("svg").attr("width")
//width/datalength*index is the left side
arrowXLeft = width/data.length*arrowData[i]['index'];
//add in half the width of one bar. don't forget delimeter
arrowX = arrowXLeft + (width/data.length - delim)/2

//use our calculated arrowX to draw
svgY
    .append("line")
    .attr("x1", arrowX)
    .attr("x2", arrowX)
    .attr("y1", 500) //I'm assuming Y is the same for all
    .attr("y2", 472)
    .attr("stroke-width", 1.6)
    .attr("stroke","red")
    .attr("marker-end", "url(#arrow)");
}


// Moveable barChart

var brushY = d3.brushY()
    .extent(function (d, i) {
        return [[x(i)+ delim/2, 0],
            [x(i) + x(1) - delim/2, heightY]];})
    .on("brush", brushmoveY)
    .on("end", brushendY);

var svgbrushY = svgY
    .selectAll('.brush')
    .data(data)
    .enter()
    .append('g')
    .attr('class', 'brush')
    .append('g')
    .call(brushY)
    .call(brushY.move, function (d){return [d.value, 0].map(scaleY);});


function brushendY(){
    if (!d3.event.sourceEvent) return;
    if (d3.event.sourceEvent.type === "brush") return;
    if (!d3.event.selection) { // just in case of click with no move
        svgbrushY
            .call(brushY.move, function (d){
                return [d.value, 0].map(scaleY);})
    
            }
    stimulusclicks++;
}

function brushmoveY() {
    if (!d3.event.sourceEvent) return;
    if (d3.event.sourceEvent.type === "brush") return;
    if (!d3.event.selection) return;

    var d0 = d3.event.selection.map(scaleY.invert);
    var d = d3.select(this).select('.selection');

    d.datum().value= d0[0]; // Change the value of the original data

    update();
}

//---------UPDATE VERTICAL and HORIZONTAL

function update(){
    svgbrushY
        .call(brushY.move, function (d){
            return [d.value, 0].map(scaleY);})
        .selectAll('text')
        .attr('y', function (d){return scaleY(d.value) + 25;})
        .text(function (d) {return d3.format('.2')(d.value);});
}

var StartTime = Date.now()