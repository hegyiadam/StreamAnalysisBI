//Monitor the input
var input = document.getElementById("sentimentalWordInput");
function sentimentalSearch(e) {
    var code = (e.keyCode ? e.keyCode : e.which);
    if (code == 13) {
        searchFunction();
    }
}

//Get percent of the expression using service.php
function searchFunction() {
    input = document.getElementById("sentimentalWordInput");
    $body = $("body");
    $.ajax({
        url: ("service.php/?expression="+input.value),
        beforeSend: function(){
            $("#loadingModal").show();
        },
        complete: function(data){
            $("#loadingModal").hide();
            var json_response = parseResponse(data.responseText);
            var positivePercent = json_response.pos*100;
            var negativePercent = json_response.neg*100;
            changePositivePercent(positivePercent);
        }
    });
}

function parseResponse(resp){
    var relevantLine= resp.split("\n")[2];
    // relevantLine IS LIKE   "[ pureJsonString INCLUDES (') INSTEAD OF (") ]"
    var pureJsonString = relevantLine.replace("[","").replace("]","").replace(/"/g,"").replace(/'/g,"\"");
    return JSON.parse(pureJsonString);
}

function newTextColor(newPercent){
    if(newPercent<33)
        return '#990000';
    if(newPercent<66)
        return '#eaac00';
    return '#00cc66'
}

function changePositivePercent(newPercent){
    $(".circliful").remove();
    $("#circle-diagram").circliful({
        animation: 1,
        animationStep: 5,
        animateInView: true,
        foregroundBorderWidth: 15,
        backgroundBorderWidth: 15,
        percentageY: 108,
        percentageX: 102,
        textSize: 28,
        textStyle: 'font-size: 12px;',
        percent: newPercent,
        fontColor: newTextColor(newPercent)
    });
}



