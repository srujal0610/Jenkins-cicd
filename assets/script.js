$(document).ready(function() {
    fetchUsers();

    $("#addForm").submit(function(event) {
        event.preventDefault();
        let name = $("#name").val();
        let email = $("#email").val();

        $.post("add.php", { name: name, email: email }, function() {
            fetchUsers();
        });
    });

    function fetchUsers() {
        $.getJSON("fetch.php", function(data) {
            let rows = "";
            $.each(data, function(i, user) {
                rows += `<tr>
                    <td>${user.id}</td>
                    <td>${user.name}</td>
                    <td>${user.email}</td>
                    <td>
                        <button onclick="deleteUser(${user.id})">Delete</button>
                    </td>
                </tr>`;
            });
            $("#userTable").html(rows);
        });
    }

    window.deleteUser = function(id) {
        $.post("delete.php", { id: id }, function() {
            fetchUsers();
        });
    };
});

