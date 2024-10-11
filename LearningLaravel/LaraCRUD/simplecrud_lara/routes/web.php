<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostController;
use App\Models\Post;

///Ei route e view ache, abong ei view te model er data o dea hoyeche
// Route::get('/', function () {
//     return view('welcome', ['posts' => Post::all()]);
// })->name('home');

///Ei route e view ach with pagenation, abong ei view te model er data o dea hoyeche 
Route::get('/', function () {
    return view('welcome', ['posts' => Post::paginate(5)]);
})->name('home');

Route::get('/create', [PostController::class, 'create']);
Route::post('/store', [PostController::class, 'store_data'])->name('store');

Route::get('/edit/{id}', [PostController::class, 'edit_data'])->name('edit');

Route::post('/update/{id}', [PostController::class, 'update_data'])->name('update');

Route::get('/delete/{id}', [PostController::class, 'delete_data'])->name('delete');

Route::get('/search', [PostController::class, 'search_data'])->name('search');
