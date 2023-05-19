<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <form action="home.php" method="post">
        <p>
            <label for="name">Name: </label>
            <input type="text" name="name" id="name" required>
        </p>
        <p>
            <label for="age">Age: </label>
            <input type="number" name="age" id="age" required>
        </p>
        <p>
            <input id="submit" type="submit" value="Submit">
        </p>

    </form>
</body>

</html>