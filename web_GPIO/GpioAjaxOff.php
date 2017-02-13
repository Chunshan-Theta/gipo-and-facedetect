<?php
$n = isset($_GET["n"])?$_GET["n"]:null;

if($n==null){
		echo "no pin Num";
	}
else{
	//Note—(python command) :connect to off.py
	$cmd = "sudo python /var/www/html/web_GPIO/off.py ".$n;
	system($cmd);
}


?>
