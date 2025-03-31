<?php require 'config.php'; ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP MySQL CRUD</title>
    <link rel="stylesheet" href="assets/style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

    <div class="container">
        <h2>PHP MySQL CRUD App</h2>

        <form id="addForm">
            <input type="text" id="name" placeholder="Enter Name" required>
            <input type="email" id="email" placeholder="Enter Email" required>
            <button type="submit">Add User</button>
        </form>

        <h3>Users List</h3>
        <table>
            <thead>
                <tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>
            </thead>
            <tbody id="userTable"></tbody>
        </table>
    </div>

    <script src="assets/script.js"></script>
</body>
</html>

