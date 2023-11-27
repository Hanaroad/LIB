<?
header('Content-Type: text/html; charset=UTF-8');

include "dbconnect.php";

extract($_POST);



$sql = "delete from member where uid=".$_GET['uid'];
$result = mysqli_query($conn, $sql) or die ("ERROR : ".$sql);

backGo('삭제되었습니다');

function backGo($msg) {
    echo "<script>";
    echo "alert('".$msg."');";
    echo "history.go(-1);";
    echo "</script>";
}

?>