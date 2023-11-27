<?
header('Content-Type: text/html; charset=UTF-8');

include "dbconnect.php";

extract($_POST);
extract($_GET);
if($name == "") {
    echo "이름을 입력하세요";
    exit;
}

if($id == "") {
    echo "아이디를 입력하세요";
    exit;
}
if($password == "") {
    echo "비밀번호를 입력하세요";
    exit;
}

$now = date("Y-m-d");

$sql = "select uid from member where id='".$id."'";
$result = mysqli_query($conn, $sql) or die ("ERROR : ".$sql);

$msg1 = "이미 등록된 사용자입니다";


if(mysqli_num_rows($result) > 0) backGo($msg1);

if($uid) {
    $sql = "update member set name='".$name."', id='".$id."', password=".$password." where uid=".$uid;
} else {
    $sql = "insert into member (name,id,password,registDate) values ('$name', '$id', $password, '$now')";
}

$result = mysqli_query($conn, $sql) or die ("ERROR : ".$sql);

// 수정쿼리
// update member set name='$name', id='$id' where uid='$uid;


function backGo($msg) {
    echo "<script>";
    echo "alert('".$msg."');";
    echo "history.go(-1);";
    echo "</script>";
}
?>