<?php
include 'config.php';

header('Content-Type: application/json');

$name = $_POST['name'] ?? '';
$email = $_POST['email'] ?? '';

if (empty($name) || empty($email)) {
    echo json_encode(["status" => "error", "message" => "Missing fields"]);
    exit;
}

$sql = "INSERT INTO users (name, email) VALUES ('$name', '$email')";

if ($conn->query($sql) === TRUE) {
    echo json_encode(["status" => "success", "message" => "User added"]);
} else {
    echo json_encode(["status" => "error", "message" => $conn->error]);
}

