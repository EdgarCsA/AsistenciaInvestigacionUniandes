<?php


$ou=shell_exec("./program.x file.txt 1 1 3 4 1");

//echo $ou;

//$fp = fopen("Sol200000.txt", "rb");

$command = '/home1/ingtextc/public_html/anaconda3/bin/python /home1/ingtextc/public_html/ur/pk/prefile2.py';
$output = shell_exec($command);

$archivo = file_get_contents("Sol200000.txt");

//$archivo=substr($archivo,0,-2);

echo $archivo;

//$datos = fread($fp);

//$echo $datos;

//while (!feof($fp))
//{
//echo fgets($fp)."<br />";
//}
fclose($fp);

?>
