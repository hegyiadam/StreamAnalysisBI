<?php
include 'database_connection.php'; 


function selectArticles($exp) {
    $db = connectToDb();
    
    //Delete all the previous corpus
    $general_cursor = pg_query($db, "DELETE FROM selected_articles");

    //Select every corpus that includes the expression
    $exp = "%" . $exp ."%";
    $sql ='SELECT data FROM corpus WHERE data ILIKE $1;';
    $select_corpus_cursor = pg_query_params($db, $sql,array($exp));

    if(!$select_corpus_cursor) {
        dbErrorHandler($db);
        exit;
    } 
    
    //Upload the found corpuses    
    while($row = pg_fetch_row($select_corpus_cursor)) {
        $sql = 'INSERT INTO selected_articles (article) VALUES ($1)';
        $general_cursor=pg_query_params($db, $sql , array($row[0]));
        
        if(!$general_cursor) {
            dbErrorHandler($db);
            exit;
        } 
    }

    pg_close($db);
}

?>

