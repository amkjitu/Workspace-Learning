<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    // Implementation of 'show' at the DemoController class
    public function show($value = null)
    {
        //return 'controller passed: ' . $value; //only prints the value coming from route
        return view('welcome')->with(['value' => $value]); // send the value coming from the route to the view name 'welcome.blade.php'
    }
}
