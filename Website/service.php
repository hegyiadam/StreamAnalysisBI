<?php
include 'database_connection.php'; 
set_time_limit(0);
header('Content-type:application/json;charset=utf-8');

$exp = $_GET['expression'];
$exp = strtolower($exp);

$db = connectToDb();

//Search for a cached result
$pos_cache = pg_query_params($db, "SELECT positive_percent, searched_times FROM result_cache WHERE expression = $1",array($exp));
if($pos_cache){
    while($row = pg_fetch_row($pos_cache)){
        $pos = intval($row[0]);
        $times = intval($row[1]);
        $times += 1;
        $sql = 'UPDATE result_cache SET searched_times = $1 WHERE expression = $2';
        $general_cursor=pg_query_params($db, $sql , array($times,$exp));
        echo json_encode($pos);
        exit;
    }
}
    
//Prepare corpus for sentimental analysis
$general_cursor = pg_query($db, "DELETE FROM searched_expression");
$general_cursor = pg_query($db, "DELETE FROM selected_articles");

$sql = 'INSERT INTO searched_expression (expression) VALUES ($1)';
$general_cursor=pg_query_params($db, $sql , array($exp));
if(!$general_cursor){
    http_response_code(500);
    exit;
}
$res = exec("\"prepare_corpus/prepare_corpus.exe\""); 
    
//Handle not found error
$count = pg_query($db, "SELECT count(*) FROM selected_articles");
$row = pg_fetch_row($count);
if ($row[0] == "0"){
    echo json_encode('Expression is not found in the news!');
    http_response_code(405);
    exit;
}    

//Sentimental analysis
$res = exec("\"service/service.exe\""); 
$json_result =json_decode(str_replace("'","\"",str_replace("\"","",$res)),true);
parse_str($res,$output);


$pos =$json_result['pos']*100;
$sql = 'INSERT INTO result_cache (expression,positive_percent,searched_times) VALUES ($1,$2,1)';
$general_cursor=pg_query_params($db, $sql , array($exp,$pos));

echo json_encode($pos);
pg_close($db);
?>