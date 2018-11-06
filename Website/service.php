<?php
include 'database_reader.php'; 
set_time_limit(0);
header('Content-type:application/json;charset=utf-8');

$exp = $_GET['expression'];
selectArticles($exp);


$res = exec("\"service/service.exe\""); 
var_dump($res);
parse_str($res,$output);

echo json_encode(array($res)) ;
?>