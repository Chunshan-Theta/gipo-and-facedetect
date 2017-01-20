<?php
	// Output GPIO setting from sql 
	// source: https://github.com/Chunshan-Theta/SQLCmdUsingPHP/blob/master/GET_SearchData.php 
	$dbname = "gpio";
	$hostIP = "127.0.0.1";
	$user = "theta";
	$password = "theta";
	//SQL command
	$c = "SELECT * FROM `config` ORDER BY `config`.`id` DESC LIMIT 1";
	
	if($password==null){
		echo "no password";
	}
	else if($dbname==null){
		echo "no dbname";
	}
	else if($hostIP==null){
		echo "no hostIP";
	}
	else if($user==null){
		echo "no user";
	}
	else if($c==null){
		echo "no SQL command";
	}
	else{
		$result = Search_mysqlQuery($c,$dbname,$hostIP,$user,$password);

		#$result = json_encode($result);
		echo json_encode(json_decode($result["0"]->setting));

		
	}
	
	
	
	
	

	
	function Search_mysqlQuery($sql,$dbname,$hostIP,$user,$password) {
		/* Connect to a MySQL database using driver invocation 
		$dbname='';
		$hostIP='';
		$user = '';
		$password = '';
		*/
		$dsn = 'mysql:dbname='.$dbname.';host='.$hostIP;
		$result = null;
		try {
			$dbh = new PDO($dsn, $user, $password);
			$result = $dbh->query($sql)->fetchAll(PDO::FETCH_OBJ);	
		} catch (PDOException $e) {
			echo 'Connection failed: '.$e->getMessage();
		}
		return $result;
	}
	//SELECT * FROM `main` WHERE `Surl` = 'zEGK33FBdE8' ORDER BY `id` DESC LIMIT 1

?>
