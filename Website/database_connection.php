<?php
function connectToDb(){

    $db_config = simplexml_load_file("dbconnection.config");

    $host        = "host = " . $db_config->host;
    $port        = "port = " . $db_config->port;
    $dbname      = "dbname = " . $db_config->dbname;
    $credentials = "user = ". $db_config->credentials_user . " password=" . $db_config->credentials_pass;

    $db = pg_connect( "$host $port $dbname $credentials"  ) or die();
    return $db;
}

function dbErrorHandler($db){
    $errs = array();
    array_push($errs,pg_last_error($db));
    echo json_encode($errs);
}
?>