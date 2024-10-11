<!-- https://www.youtube.com/watch?v=zZ6vybT1HQs&ab_channel=BroCode -->
<!--
///1. PHP and HTML

What is PHP?
------------
PHP is an acronym for "PHP: Hypertext Preprocessor"
PHP is a widely-used, open source scripting language
PHP scripts are executed on the server
PHP is free to download and use
PHP is an amazing and popular language!

It is powerful enough to be at the core of the biggest blogging system on the web (WordPress)!
It is deep enough to run large social networks!
It is also easy enough to be a beginner's first server side language!

What is a PHP File?
-------------------
PHP files can contain text, HTML, CSS, JavaScript, and PHP code
PHP code is executed on the server, and the result is returned to the browser as plain HTML
PHP files have extension ".php"

What Can PHP Do?
---------------
PHP can generate dynamic page content
PHP can create, open, read, write, delete, and close files on the server
PHP can collect form data
PHP can send and receive cookies
PHP can add, delete, modify data in your database
PHP can be used to control user-access
PHP can encrypt data
With PHP you are not limited to output HTML. You can output images or PDF files. You can also output any text, such as XHTML and XML.

Why PHP?
--------
PHP runs on various platforms (Windows, Linux, Unix, Mac OS X, etc.)
PHP is compatible with almost all servers used today (Apache, IIS, etc.)
PHP supports a wide range of databases
PHP is free. Download it from the official PHP resource: www.php.net
PHP is easy to learn and runs efficiently on the server side
-->

<?php
// #echo VS print
// *echo and print are more or less the same. They are both used to output data to the screen.

// The differences are small: echo has no return value while print has a return value of 1 so it can be used in expressions. echo can take multiple parameters (although such usage is rare) while print can take one argument. echo is marginally faster than print.

// print "Hello"." Print"."\n"; // \n dont works
// echo "Hello"." Echo <br>";   // <br> works
// echo "Hello";

// #single quote VS double quote
// Strings are surrounded by quotes, but there is a difference between single and double quotes in PHP. When using double quotes, variables can be inserted to the string as in the example above.

// When using single quotes, variables have to be inserted using the . operator, like this:
// $name = 'Jitu';
// echo '<p>Hello '.$name.'</p>';
// echo "<p>Hello $name</p>";
?>

<!-- html code php file-->
<!--
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Learning PHP</h1>
    <br>
    <button>Okay</button>
    <br>
</body>
</html>
-->

<?php
///2. Syntax and Variable
/*
#PHP Case Sensitivity: A partial case sensitive language
* keywords (e.g. if, else, while, echo, etc.), classes, functions, and user-defined functions are not case-sensitive.
* variables are case sensitive
// or # is single line comment

#PHP is a Loosely Typed Language:
* PHP automatically associates a data type to the variable, depending on its value. Since the data types are not set in a strict sense, you can do things like adding a string to an integer without causing an error.

* In PHP 7, type declarations were added. This gives an option to specify the data type expected when declaring a function, and by enabling the strict requirement, it will throw a "Fatal Error" on a type mismatch.

*You will learn more about 'strict' and 'non-strict' requirements, and data type declarations in the PHP Functions chapter.
*/

// //String
// $name = "Jitu";
// $food = "Pizza";
// echo "<br>{$name} likes {$food} <br>";

// //integer
// $age = 21;
// //floating point
// $gpa = 2.5;
// $price = 10;
// echo "I am {$age} years old with gpa {$gpa} having \${$price} <br>";

// //boolean
// $online = true;
// echo "Online status {$online}";

?>

<?php
//3. Operators -->

//Arithmetic operators
// + - * / ** %


//Increment/decrement operators
//++ --

//Operator Precedence: () ** * / % + -

?>


<!-- 4. GET and POST method -->
<!DOCTYPE html>
<br lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- GET 
    <form action="index.php" method="get">
        <label>Username</label> </br>
        <input type="text" name="username"> </br>
        <label>Password</label> </br>
        <input type="password" name="password">
        <input type="submit" value="login">
    </form>
    -->

    <!-- POST 
    <form action="index.php" method="post">
        <label>Username</label> </br>
        <input type="text" name="username"> </br>
        <label>Password</label> </br>
        <input type="password" name="password">
        <input type="submit" value="login">
    </form>

 </body>
 </html>
 -->

    <?php
    ///4. GET and POST method PHP part
    //GET
    /*
Data is appended to the url
NOT SECURE
char limit
Bookmark is possible w/ values
GET requests can be cached
Better for a search pagel
*/

    //echo "{$_GET["username"]} <br>";
    //echo "{$_GET["password"]} <br>";

    //POST
    /*
Data is packaged inside the body of the HTTP request
MORE SECURE
No data limit
Cannot bookmark
GET requests are not cached
Better for submitting credentials
*/
    //echo "{$_POST["username"]} <br>";
    //echo "{$_POST["password"]} <br>";
    ?>

    <!-- 9. For Loop -->
    <!-- 
<!DOCTYPE html>
 <html lang="en">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
 </head>
 <body>
    <form action="index.php" method="post">
    <label>Enter a number</label> <br>
    <input type="text" name="count">
    <input type="submit" value="start">
    </form>
 </body>
 </html>
 -->

    <!-- 9. For Loop PHP part-->
    <?php
    //  $count = $_POST['count'];
    //  for($i=1; $i<=$count; $i++){
    //     echo "{$i} <br>";
    //  }
    ?>

    <!-- 11. Arrays -->
    <?php
    ///There are two ways to define an array
    //1. using []
    $numbers = [1, 2, 'amir', ['a', 'b']];
    //2. using array() function call
    $numbers1 = array(1, 2, 'amir', ['a', 'b']);

    //How to print an array
    //using echo or print; note: they converts everything into string and then outputs
    //echo $numbers; //will cause the element of 0 index
    //echo $numbers[0]; //will print the
    //but can print the array element one by one linear array using forloop or foreachloop
    //but this number array has 2d array in index 3 so index 3 cannot be printed so we -2
    // for ($i = 0; $i < count($numbers) - 2; $i++) {
    //     echo $numbers[$i] . '<br>';
    // }
    // foreach ($numbers as $number) {
    //     echo $number . '<br>'; //will cauase error because index has multiple elements
    // }


    //using print_r whole array can be printed 
    //print_r($number);

    //using print_r whole array can be printed with more details; i.e. type of each element 
    //var_dump($number)

    ///Types of array
    //I. Indexed Array: when all the indexes are integers
    // //only array of int
    // $intarray = [1, 2, 3, 4, 5];
    // print_r($intarray);
    // //insert at the end
    // array_push($intarray, 6, 7);
    // print_r($intarray);
    // //remove from the front
    // array_pop($intarray);
    // print_r($intarray);
    // //remove from the rear
    // array_shift($intarray);
    // print_r($intarray);
    // //reverse array using reverse() it returns a reversed array. it must be assigned to something
    // $revarray = array_reverse($intarray);
    // print_r($revarray);


    // //only array of int but index is not continuous
    // $arr1 = [0 => 10, 2 => 11, 3 => 12];
    // print_r($arr1);

    // $arr2 = [0 => 100, 1 => 'a', 2 => 'hamja', 3 => true];
    // print_r($arr2);

    //II. Associative Array: when all the indexes are not integers. It is an array of key=>value pairs.

    $capitals = array("USA" => "NWY", "BD" => "Dhaka", "India" => "Delhi");

    // //print the value with the key
    // echo $capitals["USA"];

    // //add new key value pair to the array
    // $capitals["Nepal"] = "Kathmondu";

    // //add a new value without defining key, and this is interesting the key will be the +1 of existing any integer key. 
    // $capitals[] = "Lima"; //0=Lima

    // //delete the rear element
    // array_pop($capitals);

    // //delete the front element
    // array_shift($capitals);

    // //print the whole array using key by foreach loop
    // foreach ($capitals as $key => $value) {
    //     echo "{$key} = {$value} <br>";
    // }

    //extracting the keys from the associative array. syntex: array_keys($array) returns a array of keys.
    // $keys = array_keys($capitals);
    // for ($i = 0; $i < count($keys); $i++) {
    //     echo $keys[$i] . '<br>';
    // }
    // foreach ($keys as $key) {
    //     echo $key . '<br>';
    // }

    // //extracting the values from the associative array. syntex: array_values($array) returns a array of values.
    // $values = array_values($capitals);
    // for ($i = 0; $i < count($values); $i++) {
    //     echo $values[$i] . '<br>';
    // }
    // foreach ($values as $values) {
    //     echo $values . '<br>';
    // }

    // ///How to exchange the key,value pair:
    // // Syntex: array_flip($name_array) it returns an array
    // $capitals = array_flip($capitals);
    // foreach ($capitals as $key => $value) {
    //     echo "{$key} = {$value} <br>";
    // }

    //III. Combineds Array: 
    $student = [0 => '2', 'a' => 1, 'name' => 'amir'];
    foreach ($student as $key => $value) {
        echo "{$key} = {$value} <br>";
    }


    ?>