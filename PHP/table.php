<?php
$place = [['siteName' => '네이버', 'url'=>'naver.com'],['siteName' => '구글', 'url'=>'google.com'],['siteName' => '다음', 'url'=>'daum.net']];
?>
<table border="1">
   <tr>
      <th>사이트명</th>
      <th>URL</th>
   </tr>
   <?
   for($i = 0 ; $i < sizeof($place) ; $i++) {
      echo "<tr><td>".$place[$i]['siteName']."</td><td>".$place[$i]['url']."</td></tr>";
   }
   ?>
</table>