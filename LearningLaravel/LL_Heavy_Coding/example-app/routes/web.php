<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\DemoController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\EmployeeApiController;

///* Learning Routes and Views *///

// Route::get('/', function () {
//     return view('welcome');
// });

// Route::get('homebar', function () {
//     return "home";
// });

Route::get('homebar', function () {
  return view('home');
});

// ///1. Route
// Route::view('homebar', 'home');
// Route::view('aboutbar', '/about');
// Route::view('/aboutbar/abt', '/about');

///2.Parameterised Route
//a. does not handle null parameter
// Route::get('proutebar/{id}', function ($id) {
//     return 'provided parameter: ' . $id;
// });

//b. handles null parameter
// Route::get('proutebar/{id?}', function ($id = null) {
//     return 'provided parameter: ' . $id;
// });

//c. validates a specific parameter provided with only number
// Route::get('proutebar/{id?}', function ($id = '') {
//     return $id;
// })->whereNumber('id');

//d. validates a specific parameter provided with a specific string
// Route::get('proutebar/{name?}', function ($name = '') {
//     return $name;
// })->whereIn('name', ['Jitu', 'Hasan']);

//e. validates a specific parameter provided with a specific regular expression
// for example a-z,A-Z only
// Route::get('proutebar/{regex?}', function ($regex = null) {
//     return 'The regular expression: ' . $regex;
// })->where('regex', '[a-zA-Z]+');

///3. Named Routes
//For named routing we must use blade.php
//this is useful for SEO
//that is urls can be changed easily and dynamically here:
// get('route_name')->name('named_route'); route name is passed by the 'name_route'
// to the blade view page. 
//view page holds the named route like below format:
//  <a href="{{route('intro')}}">   home introduction</a> 

// //a. 'homebar/introduction' is url 
// Route::get('homebar/introduction', function () {
//     return view('home');
// })->name('intro');

// //b. 'homebar/about' is url
// Route::get('homebar/about', function () {
//     return view('home');
// })->name('about');

// //c. 'homebar/homebar-nijei-abar' is url
// Route::get('homebar/homebar-nijei-abar', function () {
//     return view('home');
// })->name('home');

///4. Grouped Route
//Have a look of the 3 Routes above; this have 3 routes in which 3 routes are in the a common route called homebar.
//So we can group these 3 routes to the single homebar route as a prefix

// //A. 'homebar/
// Route::prefix('homebar')->group(function () {

//     //a. 'homebar/introduction' is url
//     Route::get('introduction', function () {
//         return view('home');
//     })->name('intro');

//     //b. 'homebar/about' is url
//     Route::get('about', function () {
//         return view('home');
//     })->name('about');

//     //c. 'homebar/homebar-nijei-abar' is url
//     Route::get('homebar-nijei-abar', function () {
//         return view('home');
//     })->name('home');
// });

///* Learning Blade.php *///
//Create a layouts folder inside views folder
//create header.blade.php
//create footer.blade.php
//create master.blade.php

// here master.blade.php combines all the layout files.
// structure of master:
//@include('layouts.header')
//@yield('main-body') //this file is from the the main page. 
//@include('layouts.footer')

//create a route for the main page called 'welcome'
//in welcome page there may have section which will be named.
//this section name will use the master.php to push all the files in itself

// Route::get('/{value?}', function ($value = null) {
//   return view('welcome')->with(['value' => $value]);
// });

///* Learning Controller *///
//create a new controller: php artisan make:controller DemoController

//1. no value passed with the controller route
Route::get('home', [DemoController::class, 'index']);
// this line means that in home url there is a controller named 'DemoController'.
// and there is a function called 'index'
// so there must be an implementation of index at the DemoController class

// //2. value passed with the controller route and send it to a view also
// Route::get('home/{value?}', [HomeController::class, 'show']);

//3. advanced controller
// will learn later

///* Database Configuration and Migration *///

//  * .env file contains all the configuration of the app including:
//      -app
//      -database
//      -encryption
//      -sessions
//      -mails
//      -aws
//      and so on
//  * database folder contains migration folder where all migrations are executed by php code. For example table creation, drop, rollback etc.

///* How to create table using Migration *///
// cmd: php artisan make:migration table_name
// this command creates a migration file in the 
//  -> dataabse -> migrations -> timestamp_crate_table_name.php
// now set the table attributes and constrains as required:
//for example:
/* public function up(): void
    {
        Schema::create('employee', function (Blueprint $table) {
            $table->id();
            $table->string('emp_id', 65);
            $table->string('email', 65);
            $table->text('address', 150);
            $table->date('doj');
            $table->boolean('status')->default(0);
            $table->timestamps();
        });
    }
  */
// now migrate the table using the cmd: php artisan migrate

/// Some useful migration command:
/*
1. php artisan migrate:rollback 
-undo last migration

2. php artisan migrate:reset
-undo all the migration happened
*/



///* Learning Middleware *///
//create a new Middleware: php artisan make:middleware Check

/*
Laravel includes a middleware that verifies the user of your application is authenticated. 
If the user is not authenticated, the middleware will redirect the user to your application's login screen. 
However, if the user is authenticated, the middleware will allow the request to proceed further into the application.
1.Global Middleware: for all Routes 
2.Route Middleware: for a specific Route
To assign middleware to specific routes, invoke the middleware method when defining the route:
*/

// use \App\Http\Middleware\Check;

// Route::get('/{value?}', function ($value = null) {
//   return view('welcome')->with(['value' => $value]);
// })->middleware(Check::class);



///* Learning APIs in Laravel *///
///Use Case: Lets say ekta application 2/more technology te banano ekhon kivabe data use korbo?
///Solution: Through API amra data share korbo
///Mutolo API guli 'web' e thake na borong 'api' e thake
///What we will see
///0. how to share data
///1. create API
///2. update
///3. delete

///Steps:
//1. create a controller : php artisan make:controller EmployeeApiController
//2. create api: php artisan install:api
//now see 'routes' er 'api'
