<?php
/*
API Routes
---------------------------------------------------------------------
Here is where you can register API routes for your application. These
routes are loaded by the RouteServiceProvider and all of them will
be assigned to the "api" middleware group. Make something great!
*/

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\EmployeeApiController;
use App\Http\Controllers\UserApiController;


///First Of All add below line to the bootstrap/app.php:
//api: __DIR__ . '/../routes/api.php',
//eta korlei api kaj korbe 

///1.Employee API
//'EmployeeApiController' will use to share data
Route::get('share-data/emp', [EmployeeApiController::class, 'view']);
//see EmployeeApiController kivabe baki kaj hocche
//Insert Data: 'EmployeeApiController' will use to insert data
Route::get('share-data/emp/create', [EmployeeApiController::class, 'create']);
//Insert Data: 'EmployeeApiController' will use to insert data
Route::get('share-data/emp/update', [EmployeeApiController::class, 'update']);
//Insert Data: 'EmployeeApiController' will use to insert data
Route::get('share-data/emp/delete', [EmployeeApiController::class, 'delete']);

///2.User API
//'UserApiController' will use to share data
Route::get('share-data/usr', [UserApiController::class, 'view']);
//see UserApiController kivabe baki kaj hocche