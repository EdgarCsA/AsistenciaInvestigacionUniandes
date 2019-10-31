<?php


$ou=shell_exec("./program.x file.txt 1 1 3 4 1");

$command = '/home1/ingtextc/public_html/anaconda3/bin/python /home1/ingtextc/public_html/ur/pk/prefile2.py';
$output = shell_exec($command);


$fp = fopen("Sol200000.txt", "rb");



while (!feof($fp))
{
echo fgets($fp)."<br />";
}
fclose($fp);

?>
