<?php
require 'config.php';

if(isset($_POST['id'])) {
    $id = $_POST['id'];
    $sql = "DELETE FROM users WHERE id=$id";

    if($conn->query($sql)) {
        echo "User deleted!";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

