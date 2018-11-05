<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>News Analizer</title>
    <link rel="shortcut icon" type="image/x-icon" href="img/book_icon.ico" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
    <script src="js/main.js"></script>
</head>

<body>
    
<div class="bgimg-1">
    <div class="container centered">
        <div class="row">
            <div id="row-position" class="col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
                <div id="myDropdown" class="dropdown-content">
                    <h1 class="upper-title">News Analizer</h1>
                    <div id="test-circle" class="svg-container">
                        <!--<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 194 186" class="circliful"><circle cx="100" cy="100" r="57" class="border" fill="none" stroke="#ccc" stroke-width="15" stroke-dasharray="360" transform="rotate(-90,100,100)"></circle><circle class="circle" cx="100" cy="100" r="57" fill="none" stroke="#3498DB" stroke-width="15" stroke-dasharray="136.8, 20000" transform="rotate(-90,100,100)"></circle>
                        <circle cx="100" cy="100" r="28.5" fill="none"></circle>
                        <text class="timer" text-anchor="middle" x="100" y="113" style="font-size: 22px; undefined;" fill="#aaa">
                            <tspan class="number">38</tspan>
                            <tspan class="percent">%</tspan>
                        </text>
                        </svg>-->
                    </div>
                    <input type="text" placeholder="Search" id="myInput" onkeypress="process(event, this)">
                    
                    <div id="itemlist" class="dropdown-items">
                    </div>
                </div>

            </div>
            
        </div>
    </div>
    <div class="modal"><!-- Place at bottom of page --></div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>
        <script src="js/jquery.circliful.js"></script>
<script>
    $( document ).ready(function() { // 6,32 5,38 2,34
        $("#test-circle").circliful({
            animation: 1,
            animationStep: 5,
            animateInView: true,
            foregroundBorderWidth: 15,
            backgroundBorderWidth: 15,
            percent: 0,
            textSize: 28,
            textStyle: 'font-size: 12px;',
            textColor: '#666',
        });
       
    });
</script>
</div>
</body>

</html>