<?php
$host = "mysql";
$user = "phpuser";  // Change if needed
$password = "Srujal7#5!4";  // Change if needed
$database = "php_crud";

$conn = new mysqli($host, $user, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>

