<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DemoController extends Controller
{
    // Implementation of 'index' at the DemoController class
    public function index($value = 9)
    {
        return $value;
    }
}
