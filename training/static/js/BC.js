var data = [{index: 0, value: 10},
    {index: 1, value: 12},
    {index: 2, value: 14},
    {index: 3, value: 16},
    {index: 4, value: 14},
    {index: 5, value: 12},
    {index: 6, value: 10}
];


//--------------- VERTICAL --------------------

var margin = {top: 20, right: 40, bottom: 20, left: 40},
    widthY = 700 - margin.left - margin.right,
    heightY = 500 - margin.top - margin.bottom,
    delim = 10;

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
    .attr("height", heightY +10)
    .append('g');

svgY
    .append('rect')
    .attr('x', 0)
    .attr('y', 0)
    .style('stroke', 'black')
    .style('fill', 'white')
    .attr('width', widthY+5)
    .attr('height', heightY+5);

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
    };
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