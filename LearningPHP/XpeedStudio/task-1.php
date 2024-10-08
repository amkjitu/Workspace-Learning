<?php
///A Static function which finds jitu in an arran
//Use case:
/*
Arr::findJitu($array) returns the value where jitu is the key
where $array=['jitu'=>'fixit', 'one' => 'none'];
*/
class Arr
{
    //public $array = ['jitu' => 'fixit', 'one' => 'none', 'help' => 'noone'];
    public static function findJitu($array)
    {
        $target_key = 'jitu';
        foreach ($array as $key => $value) {
            if ($key == $target_key) {
                return $value;
            }
        }
        return null;
    }

    public static function findAny($key, $array)
    {
        $target_key = $key;
        foreach ($array as $key => $value) {
            if ($key == $target_key) {
                return $value;
            }
        }
        return null;
    }
}

//Find only jitu Arr::findJitu();
$array = ['jitu' => 'fixit', 'one' => 'none', 'help' => 'everyone'];

$result = Arr::findJitu($array);
echo $result;

//Find anything Arr::findAny();
// $search = 'help';
// $result = Arr::findAny($search, $array);
// echo $result;
