<!doctype html>
<!--  
index.php
 - insert Json data that recorded gpio setting to Mysql .
 - It's a UI. 
-->
<html>
   <head>
   </head>
   <body style="margin:0px;padding:0px;overflow:hidden">
	
   GPIO 4 (pin 7)<br>
   裝置名稱<input id="Device1" type="text" value="風扇"></input>
   消耗瓦數<input id="Cost1" type="text" value="50"></input>
   	<br><br>
   GPIO 17 (pin 11)<br>
   裝置名稱<input id="Device2" type="text" value="null"></input>
   消耗瓦數<input id="Cost2" type="text" value="null"></input>
   	<br><br>
   GPIO 18 (pin 12)<br>
   裝置名稱<input id="Device3" type="text" value="null"></input>
   消耗瓦數<input id="Cost3" type="text" value="null"></input>
   	<br><br>
   GPIO 21 (pin 13)<br>
   裝置名稱<input id="Device4" type="text" value="null"></input>
   消耗瓦數<input id="Cost4" type="text" value="null"></input>
   	<br><br>
   GPIO 22 (pin 15)<br>
   裝置名稱<input id="Device5" type="text" value="null"></input>
   消耗瓦數<input id="Cost5" type="text" value="null"></input>
   	<br><br>
   GPIO 23 (pin 16)<br>
   裝置名稱<input id="Device6" type="text" value="null"></input>
   消耗瓦數<input id="Cost6" type="text" value="null"></input>
   	<br><br>
   GPIO 24 (pin 18)<br>
   裝置名稱<input id="Device7" type="text" value="null"></input>
   消耗瓦數<input id="Cost7" type="text" value="null"></input>
   	<br><br>
   GPIO 10 (pin 19)<br>
   裝置名稱<input id="Device8" type="text" value="null"></input>
   消耗瓦數<input id="Cost8" type="text" value="null"></input>
   	<br><br>
   GPIO 9 (pin 21)<br>
   裝置名稱<input id="Device9" type="text" value="null"></input>
   消耗瓦數<input id="Cost9" type="text" value="null"></input>
   	<br><br>
   GPIO 11 (pin 23)<br>
   裝置名稱<input id="Device10" type="text" value="null"></input>
   消耗瓦數<input id="Cost10" type="text" value="null"></input>
   	<br><br>
   GPIO 8 (pin 24)<br>
   裝置名稱<input id="Device11" type="text" value="null"></input>
   消耗瓦數<input id="Cost11" type="text" value="null"></input>
   	<br><br>
   GPIO 7 (pin 26)<br>
   裝置名稱<input id="Device12" type="text" value="null"></input>
   消耗瓦數<input id="Cost12" type="text" value="null"></input>
   	

   
   <button onclick="changeSrc()">go</button>
   <div id="div1"><h2></h2></div>
   
   </body>
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
   <script type="text/javascript">
	var GetInsterPhpUrl = "";
    function changeSrc()
	  {
	  
	  var Setting1 = '{"id":"0","pin":"7","GPIO":"4","Cost":"'+document.getElementById("Cost1").value+'","Device":"'+document.getElementById("Device1").value+'"}';
	  var Setting2 = '{"id":"1","pin":"11","GPIO":"17","Cost":"'+document.getElementById("Cost2").value+'","Device":"'+document.getElementById("Device2").value+'"}';
	  var Setting3 = '{"id":"2","pin":"12","GPIO":"18","Cost":"'+document.getElementById("Cost3").value+'","Device":"'+document.getElementById("Device3").value+'"}';
	  var Setting4 = '{"id":"3","pin":"13","GPIO":"21","Cost":"'+document.getElementById("Cost4").value+'","Device":"'+document.getElementById("Device4").value+'"}';
	  var Setting5 = '{"id":"4","pin":"15","GPIO":"22","Cost":"'+document.getElementById("Cost5").value+'","Device":"'+document.getElementById("Device5").value+'"}';
	  var Setting6 = '{"id":"5","pin":"16","GPIO":"23","Cost":"'+document.getElementById("Cost6").value+'","Device":"'+document.getElementById("Device6").value+'"}';
	  var Setting7 = '{"id":"6","pin":"18","GPIO":"24","Cost":"'+document.getElementById("Cost7").value+'","Device":"'+document.getElementById("Device7").value+'"}';
	  var Setting8 = '{"id":"7","pin":"19","GPIO":"10","Cost":"'+document.getElementById("Cost8").value+'","Device":"'+document.getElementById("Device8").value+'"}';
	  var Setting9 = '{"id":"8","pin":"21","GPIO":"9","Cost":"'+document.getElementById("Cost9").value+'","Device":"'+document.getElementById("Device9").value+'"}';
	  var Setting10 = '{"id":"9","pin":"23","GPIO":"11","Cost":"'+document.getElementById("Cost10").value+'","Device":"'+document.getElementById("Device10").value+'"}';
	  var Setting11 = '{"id":"10","pin":"24","GPIO":"8","Cost":"'+document.getElementById("Cost11").value+'","Device":"'+document.getElementById("Device11").value+'"}';
	  var Setting12 = '{"id":"11","pin":"26","GPIO":"7","Cost":"'+document.getElementById("Cost12").value+'","Device":"'+document.getElementById("Device12").value+'"}';
     	  var JsonData = "["+Setting1+","+Setting2+","+Setting3+","+Setting4+","+Setting5+","+Setting6+","+Setting7+","+Setting8+","+Setting9+","+Setting10+","+Setting11+","+Setting12+"]";
          // Note-(DB config) : edit web-server IP address
	  var dbname="gpio";
	  var hostIP="127.0.0.1";
	  var user="theta";
	  var password="theta";
	

	  // ajax target  https://github.com/Chunshan-Theta/SQLCmdUsingPHP/blob/master/GET_Insert.php
	  
	  $.ajax({type: 'GET',url: "./GET_Insert.php?dbname="+dbname+"&hostIP="+hostIP+"&user="+user+"&password="+password+"&c=INSERT INTO `config` (`id`, `time`, `setting`) VALUES (NULL, CURRENT_TIMESTAMP,%27"+JsonData+"%27);", 
			success: function(result){
				$("#div1").html("<h1>傳輸成功</h1><br>Json:<br><h5>"+JsonData);
			},
			error:function(xhr, ajaxOptions, thrownError){ 
                    /* alert(xhr.status); 
                    alert(thrownError);  */
					$("#div1").html("<h1>傳輸失敗<h1><br>"+xhr.status+","+thrownError);
			} 
	  });
	   
	  
	  }

		
	</script>
</html>
