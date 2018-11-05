function searchFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("itemlist");
    a = div.getElementsByTagName("a");
    $("#itemlist").empty();
    console.log(input.value);
    id = "";
    $body = $("body");
    $.ajax({
        url: ("transaction.php")
        , success: function (data) {
            
            id = data;
            $.ajax({
                url: ("service.php/?expression="+input.value + "&tr_id="+id),
                success: function (data) {
                    
                },beforeSend: function(){
                    $(".modal").show();
                },
                complete: function(data){
                    $(".modal").hide();
                    json_response = JSON.parse(data.responseText.split("\n")[2].replace("[","").replace("]","").replace(/"/g,"").replace(/'/g,"\""))
                    console.log(json_response.pos)
                    percentChange(json_response.pos*100)
                }
            });
        }
    });
    
    /*(function poll() {
            $.ajax({
                url: ("polling.php/?tr_id="+id), success: function (data) {
                    if(data!=null){
                        text  ="";
                        for(i = 0;i<data.length;i++){
                            text += data[i];
                        };
                        $("<a>" + text + "</a>").appendTo(div);
                    }
                },
                type: "GET",
                success: function(data) {
                    console.log("polling");
                },
                dataType: "json",
                complete: setTimeout(function() {poll()}, 5000),
                timeout: 2000
            })
        })();*/
       
    


}

function percentChange(newPercent){
    $(".circliful").remove();
    $("#test-circle").circliful({
        percent: newPercent
    });
}

var input = document.getElementById("myInput");
function process(e) {
    var code = (e.keyCode ? e.keyCode : e.which);
    if (code == 13) {
        searchFunction();
    }
}

