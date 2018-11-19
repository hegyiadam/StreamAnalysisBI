<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>News Analizer</title>
    <link rel="shortcut icon" type="image/x-icon" href="img/sentimental_icon.ico" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div id="background-image">
        <div class="container centered">
            <div class="row">
                <div id="row-position" class="col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
                    <h1 class="upper-title">News Analizer</h1>
                    <div id="circle-diagram" class="svg-container"></div>
                    <input type="text" placeholder="Search" id="sentimentalWordInput" onkeypress="return sentimentalSearch(event, this)"> 
                </div>
            </div>
        </div>
        <div id="link_list_wrapper" class="container centered">
            <div id="link_list_box" class="col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
                
                    <div class="panel-body">
                        <ul id="article-list" class="list-group">
                        </ul>
                    </div>
            </div>
        </div>
        <div class="bottom_space align-text-bottom"></div>
        <div id="loadingModal"></div>
        <div id="icons">
            <div id="stats-icon" class="icon">
                <div id="stat-bubble" class="caption-bubble">
                    <p>Top searched expressions</p>
                </div>
                <br>
                <span class="glyphicon glyphicon-stats"></span>
            </div>
            <div id="help-icon" class="icon">
                <div id="help-bubble" class="caption-bubble">
                    <p>Help</p>
                </div>
                <br>
                <span class="glyphicon glyphicon-question-sign"></span>
            </div>
        </div>
    </div>
    <div id="help-modal" class="modal">
        <div id="modal-background"></div>
        <div class="modal-container">

                <div class="container centered">
                    <div class="modal-box row col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
                        <div class="glyphicon glyphicon-remove modal-close"></div>
                        <h1>
                            News Analizer Help
                        </h1>
                        <div class="scroll-container">

                            <div class="scrollable">
                                <p>
                                    In the business world, customer feedback is highly important. Some companies provide a feedback system for the customers, but only a small amount of the customers actually uses this practical opportunity. The real feedback comes from the news and from online streams. These are either written by, or for the customers. These are usually the main sources for the companies. Some bigger companies order statistics and summaries from analyzer companies. These companies collect, clean and analyze the data that comes from online streams and news sources.
                                </p>
                                <p>
                                    This website helps you out with informations about semantic meaning of words. After you type in the word the site shows you the percent of positiveness of the word according to the news.
                                </p>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    

    <div id="stats-modal" class="modal">
        <div id="modal-background"></div>
        <div class="modal-container">
                <div class="container centered">
                    <div id="stats-layout-container" class="modal-box row col-lg-8 col-lg-offset-2 col-md-8 col-md-offset-2 col-sm-8 col-sm-offset-2">
                        <div class="glyphicon glyphicon-remove modal-close"></div>
                        <h1>Top searched words</h1>
                        <div id="word-cloud-container">
                            <div id="word-cloud"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="js/d3.layout.cloud.js"></script>
    <script src="js/main.js"></script>
    <script src="js/jquery.circliful.js"></script>
    <script src="js/circliful.js"></script>
</body>

</html>