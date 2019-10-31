<?php
$filename = "file.txt";
$gestor = fopen($filename, "rb");
$contenido = fread($gestor, filesize($filename));
echo($contenido);
fclose($gestor);
?>