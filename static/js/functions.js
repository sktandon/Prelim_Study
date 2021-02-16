function datafrompost(nextpage, qNumber) {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            
            window.location = nextpage
        }
    }
    var parameters = ""
    parameters += "qNumber="+qNumber
    parameters += "&FinalValues="+JSON.stringify(arrowData)
    parameters += "&StimulusClicks="+stimulusclicks
    parameters += "&ResponseTime="+(Date.now()-StartTime)

    //update database
    xhttp.open("POST", "/datafrompost", true);
    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.send(parameters);   
}

