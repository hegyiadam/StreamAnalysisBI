<?php
include 'database_connection.php'; 
set_time_limit(0);
header('Content-type:application/json;charset=utf-8');

$db = connectToDb();

$list_of_words =[];
$top = pg_query($db, "SELECT expression FROM result_cache ORDER BY searched_times");
if($top){
    while($row = pg_fetch_row($top)){
        array_push($list_of_words,$row[0]);
    }
    echo json_encode($list_of_words);
    pg_close($db);
    exit;
}else{
    echo json_encode('Top searched words cannot be loaded!');
    http_response_code(405);
    exit;
}

?>