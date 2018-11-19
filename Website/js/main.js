

$("#help-modal").hide();
$("#stats-modal").hide();

//Monitor the input
var input = document.getElementById("sentimentalWordInput");
function sentimentalSearch(e) {
    var code = (e.keyCode ? e.keyCode : e.which);
    if (code == 13) {
        searchFunction();
        
    }
    if (event.keyCode == 32) {
        alert('Only words are accepted for search!');
        return false;
    }
    return true;
}

//Get percent of the expression using service.php
function searchFunction() {
    input = document.getElementById("sentimentalWordInput");
    $body = $("body");
    $("#article-list").empty();
    $.ajax({
        url: ("service.php/?expression="+input.value),
        beforeSend: function(){
            $("#loadingModal").show();
        },
        complete: function(data){
            $("#loadingModal").hide();
            var positivePercent = data.responseText;
            if (data.status!=405){
                changePositivePercent(positivePercent);
                load_articles();
            }
        },
        error: function(e){
            
            $("#loadingModal").hide();
            
            var errorMessage = e.responseText.replace(/"/g,"").replace(/'/g,"\"");
            if (e.status==405){
                alert(errorMessage);
                changePositivePercent(0);
            }
        }
    });
}

//Load articles link list for those articles that includes the searched expression
function load_articles(){
    $.ajax({
        url: ("article_loader.php/?expression="+input.value),
        complete: function(data){
            var results = JSON.parse(data.responseText);
            results.forEach(function(article) {
                add_article_to_list(article["title"],article["url"]);
            });
        }
    });
}

function add_article_to_list(title,link){
    $('#link_list_box > div > ul').append(
        $('<li>').attr('class','list-group-item').append(
            $('<a>').attr('href',link).append(title)
    ));
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

function load_top_word(){
    $.ajax({
        url: ("topsearches.php"),
        beforeSend: function(){
            $("#loadingModal").show();
        },
        complete: function(data){
            $("#loadingModal").hide();
            var top_words_list = data.responseText;
            if (data.status!=405){
                word_list = JSON.parse(top_words_list);
            }
        },
        error: function(e){
            
            $("#loadingModal").hide();
            
            var errorMessage = e.responseText.replace(/"/g,"").replace(/'/g,"\"");
            if (e.status==405){
                alert(errorMessage);
                changePositivePercent(0);
            }
        }
    });
}

document.addEventListener("touchstart", function(){}, true)
$(".glyphicon-question-sign").hover(function(){
    $("#help-bubble").css("opacity",1);
},function(){
    $("#help-bubble").css("opacity",0);
}).click(function(){
    $("#help-modal").show();
});

$(".glyphicon-stats").hover(function(){
    $("#stat-bubble").css("opacity",1);
},function(){
    $("#stat-bubble").css("opacity",0);
}).click(function(){
    
    $("#stats-modal").show();
    $("#word-cloud").empty();
    var width = $("#stats-layout-container").width() ,
    height = $("#stats-layout-container").width() * 0.60;
    $("#word-cloud-container").css("width",width).css("height",height);
    drawWordCloud(height,width);
    
});;

$(".modal-close").click(function(){
    $(".modal").hide();
}).hover(function(){
    $(".modal-close").css("color","black");
},function(){
    $(".modal-close").css("color","white");
});


$(window).resize(function() {
    if($("#stats-modal").hasClass('in')){
        $(document).ready(function(){
            $("#word-cloud").empty();
            var width = $("#stats-layout-container").width() ,
            height = $("#stats-layout-container").width() * 0.60;
            $("#word-cloud-container").css("width",width).css("height",height);
            drawWordCloud(height,width);
        });
    }
});

var word_list = [];
$(document).ready(function(){
    var word_list = load_top_word();
});


function drawWordCloud(layout_height,layout_width){
    
    var fill = d3.scale.category20();
    var layout = d3.layout.cloud()
        .size([ Math.floor(layout_width),  Math.floor(layout_height)])
        .words(word_list.map(function(d) {
        return {text: d, size: 10 + Math.random() * 90, test: "haha"};
        }))
        .padding(5)
        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw);
    layout.start();
    function draw(words) {
    d3.select("#word-cloud").append("svg")
        .attr("width", layout.size()[0])
        .attr("height", layout.size()[1])
        .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
    }
}