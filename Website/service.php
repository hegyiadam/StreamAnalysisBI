<?php
include 'database_reader.php'; 
set_time_limit(0);
header('Content-type:application/json;charset=utf-8');

$exp = $_GET['expression'];
$id = $_GET['tr_id'];
selectArticles($exp);
$result = array();

$res="";
$opinion = array();
//while($res == ""){
$res = exec("\"dist/service/service.exe\"", $res); 
var_dump($res);
parse_str($res,$output);
array_push($opinion,$res);
//}
echo json_encode($opinion) ;


//$opinion = {"pos": $res["pos"],"neg": $res["neg"]}
/*$opinion = [ $res["pos"], $res["neg"]];


$db = connectToDb();


$ret2=pg_query($db, "UPDATE opinions SET positive = '{$res["pos"]}', negative ='{$res["neg"]}', filled = true WHERE transaction_code = '{$tr_id}')");

if(!$ret2) {
    array_push($errs,pg_last_error($db));
    exit;
} 


pg_close($db);

*/


//$op = array("<a>" . exec('python service.py', $res) . "</a>");
//echo json_encode($opinion);

?>