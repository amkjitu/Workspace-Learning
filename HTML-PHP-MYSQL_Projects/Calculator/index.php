<!DOCTYPE html>
<html>

<head>
    <title>Cal</title>
</head>

<body>

    <form action="action.php" method="POST">
        <p>A simple Calculator built with php oop</p>
        <label>First Number</label><br>
        <input type="number" name="num1" placeholder="First Oparend"><br>
        <label>Operation</label><br>
        <select name="sign" id="">
            <option value="addition">Add</option>
            <option value="subtraction">Subtract</option>
            <option value="multiplication">Multiply</option>
            <option value="division">Divide</option>
        </select><br>
        <label>Second Number</label><br>
        <input type="number" name="num2" placeholder="Second Oparend"><br><br>
        <button type="submit" name="submit">Calculate</button>
    </form>

</body>

</html>