<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    // Getting post info
    /// Constant 
    define("NAME", $_POST["name"]);
    // Variable
    $age = $_POST["age"];

    $_SESSION["id"] = NAME . "$age";

    function showName () {
        global $NAME;
        echo "<h1>Welcome " . NAME . "</h1>";
    }

    showName();

    if ($age >= 18) {
        echo "<h3>You can read interesting books</h3>";
    } else {
        echo "<h3>Too young to see the content</h3>";
    }

    // foreach ($_SERVER as $key => $value) {
    //     echo "<p>$key -> $value</p>";
    // }

    ?>

</body>

</html>