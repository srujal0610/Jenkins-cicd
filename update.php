<?php
require 'config.php';

if(isset($_POST['id']) && isset($_POST['name']) && isset($_POST['email'])) {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $email = $_POST['email'];

    $sql = "UPDATE users SET name='$name', email='$email' WHERE id=$id";

    if($conn->query($sql)) {
        echo "User updated!";
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

