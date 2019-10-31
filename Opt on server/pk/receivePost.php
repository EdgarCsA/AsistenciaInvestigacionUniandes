<?php
/**
 * http://www.lawebdelprogramador.com
 * Codigo que recibe un archivo denominado file y lo guarda en la carpeta donde
 * se ejecuta el codigo.
 * Forma parte del ejemplo de subir archivos von python
 *
 * Poner este archivo en nuestro servidor web
 */
if($_FILES["file"])
{
    # revisamos que podamos escribir en la carpeta donde nos encontramos
    # el punto hace referencia a la carpeta donde nos encontramos (con un
    # servidor Linux funciona correctamente)
    if(is_writable("."))
    {
        # guardamos el archivo
        if (!copy($_FILES["file"]["tmp_name"], $_FILES["file"]["name"]))
        {
            echo "ERROR: Error al guardar el archivo\n";
        }
    }else{
        echo "ERROR: No disponemos de derechos para escribir en la carpeta\n";
    }
}

$ou=shell_exec("./program.x file.txt 1 1 3 4 1");

//echo $ou;

$fp = fopen("Sol200000.txt", "r");
while (!feof($fp))
{
echo fgets($fp);
}
fclose($fp);


?>
