 
<?php

 

if ($_POST)
{

    if ( isset ($_POST['action']) )
    {

        if($_POST['action'] === 'level upload')
        {

            if(!isset($_FILES))
            {
               $_FILES = $HTTP_POST_FILES;
            }//if
               
            if ($_FILES['file']['error'] === UPLOAD_ERR_OK)
            {

                if ($_FILES['file']['name'] !== "")
                {
                    
                    if ($_FILES['file']['type'] === 'text/xml')
                    {

                        $uploadfile =  '/home1/ingtextc/public_html/ur/pk/' . $_FILES['file']['name'];
                        move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile);              
                    }//if
                           
                }//if
                   
            }//if
   
        }//if
       
    }//if  
   
}//if


$command = '/home1/ingtextc/public_html/anaconda3/bin/python /home1/ingtextc/public_html/ur/pk/prefile.py';
$output = shell_exec($command);
?>
 
 