<?php
///1. PHP and HTML
/*
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

*/

// /*
// #echo VS print
// *echo and print are more or less the same. They are both used to output data to the screen.

// The differences are small: echo has no return value while print has a return value of 1 so it can be used in expressions. echo can take multiple parameters (although such usage is rare) while print can take one argument. echo is marginally faster than print.
// */

// print "Hello"." Print"."\n"; // \n dont works
// echo "Hello"." Echo <br>";   // <br> works
// echo "Hello";

// /*
// #single quote VS double quote
// Strings are surrounded by quotes, but there is a difference between single and double quotes in PHP. When using double quotes, variables can be inserted to the string as in the example above.

// When using single quotes, variables have to be inserted using the . operator, like this:
// */
// $name = 'Jitu';
// echo '<p>Hello '.$name.'</p>';
// echo "<p>Hello $name</p>";

?>
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
///4. GET and POST method
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

 <?php
 $count = $_POST['count'];
 for($i=1; $i<=$count; $i++){
    echo "{$i} <br>";
 }
 ?>