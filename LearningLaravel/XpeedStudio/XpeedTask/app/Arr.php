<?php
///Task-1

namespace App;

use Illuminate\Support\Arr;

Arr::macro('findJitu', function ($array) {

    return $array['jitu'] ?? null;
    $target_key = 'jitu';
    foreach ($array as $key => $value) {
        if ($key == $target_key) {
            return $value;
        }
    }
    return null;
});

Arr::macro('findAny', function ($key, $array) {

    $target_key = $key;
    foreach ($array as $key => $value) {
        if ($key == $target_key) {
            return $value;
        }
    }
    return null;
});

// class Arr
// {
//     //public $array = ['jitu' => 'fixit', 'one' => 'none', 'help' => 'noone'];
//     public static function findJitu($array)
//     {
//         $target_key = 'jitu';
//         foreach ($array as $key => $value) {
//             if ($key == $target_key) {
//                 return $value;
//             }
//         }
//         return null;
//     }

//     public static function findAny($key, $array)
//     {
//         $target_key = $key;
//         foreach ($array as $key => $value) {
//             if ($key == $target_key) {
//                 return $value;
//             }
//         }
//         return null;
//     }
// }
