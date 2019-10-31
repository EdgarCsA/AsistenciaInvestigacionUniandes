<?php

$command = '/home1/ingtextc/public_html/anaconda3/bin/python /home1/ingtextc/public_html/ur/prueba.py';

$output = shell_exec($command);

echo $output.'/n';

//$coma="./program.x ceschia_CS2000.txt 1 1 3 4 1";
//$coma='./hello';
$ou=shell_exec("./program.x ceschia_CS2000.txt 1 1 3 4 1");

echo $ou;

?>
