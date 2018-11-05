<?php
include 'database_connection.php'; 


function selectArticles($exp) {

    $exp = "%" . $exp ."%";

    $db = connectToDb();

    $sql ="SELECT data FROM corpus WHERE data LIKE '{$exp}';";
    $errs = array();
    array_push($errs,$exp);
    $result = array();
    $ret = pg_query($db, $sql);

    if(!$ret) {
        array_push($errs,pg_last_error($db));
        exit;
    } 

    
    array_push($result,$sql);
    $ret2=pg_query($db, "DELETE FROM selected_articles");
    while($row = pg_fetch_row($ret)) {
        array_push($result,$row[0]);
        $ret2=pg_query($db, "INSERT INTO selected_articles (article) VALUES ('{$row[0]}')");
        
        if(!$ret2) {
            array_push($errs,pg_last_error($db));
            exit;
        } 
    }

    pg_close($db);
    //echo json_encode($result);
}


?>

