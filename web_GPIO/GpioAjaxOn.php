<?php
$n = isset($_GET["n"])?$_GET["n"]:null;

if($n==null){
		echo "no pin Num";
	}
else{
	echo "works ";
	echo "sudo python /var/www/html/web_GPIO/on.py ".$n;
	//Note—(python command) :connect to on.py
	$cmd = "sudo python /var/www/html/web_GPIO/on.py ".$n;
	system($cmd);
}


?>
