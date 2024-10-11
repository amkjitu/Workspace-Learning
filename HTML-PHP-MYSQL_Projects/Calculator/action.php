<?php
include 'class.php';

$num1 = $_POST['num1'];
$sign = $_POST['sign'];
$num2 = $_POST['num2'];

$data = new Calc($num1, $sign, $num2);
echo $data->Calculate();
