<?php
include 'database_connection.php'; 
set_time_limit(0);
header('Content-type:application/json;charset=utf-8');

$exp = $_GET['expression'];
$exp = strtolower($exp);

$db = connectToDb();

$ilike_exp = "%".$exp."%";
$article_list = [];
//Search for a cached result
$corpus = pg_query_params($db, 'SELECT article_id FROM corpus WHERE data ILIKE $1;',array($ilike_exp));
if($corpus){
    while($row = pg_fetch_row($corpus)){
        $id = intval($row[0]);
        $article_info = pg_query_params($db, 'SELECT title,url FROM articles WHERE id = $1;',array($id));
        if($article_info){
            while($article = pg_fetch_row($article_info)){
                array_push($article_list,array("title"=>$article[0],"url"=>$article[1]));
            }
        }
    }
}
echo json_encode($article_list);
exit;
    /*
//Prepare corpus for sentimental analysis
$general_cursor = pg_query($db, "DELETE FROM searched_expression");
$general_cursor = pg_query($db, "DELETE FROM selected_articles");

$sql = 'INSERT INTO searched_expression (expression) VALUES ($1)';
$general_cursor=pg_query_params($db, $sql , array($exp));
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

//Cache and return the result
$pos =$json_result['pos']*100;
$sql = 'INSERT INTO result_cache (expression,positive_percent) VALUES ($1,$2)';
$general_cursor=pg_query_params($db, $sql , array($exp,$pos));

echo json_encode($pos) ;*/
?>