<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;

class UserApiController extends Controller
{
    //
    public function view()
    {
        $data = User::all();
        return response()->json($data);
    }
}
