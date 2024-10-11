<?php

namespace App\Http\Controllers;

use App\Models\Employee;
use Illuminate\Http\Request;

class EmployeeApiController extends Controller
{
    //define a function for viewing data 
    public function view()
    {

        //add some data to the table
        // Employee::create([
        //     'emp_id' => 201,
        //     'name'    => 'Tutul',
        //     'email'     => 'tutul@gmail.com',
        //     'password'     => '1234',
        //     'gender'    => 'M',
        //     'address'    => 'Dhaka',
        //     'doj'    => '2024-10-08',
        //     'status' => true
        // ]);

        //display the data
        // echo "<pre>";
        // $data = Employee::all();
        // print_r($data->toArray());

        // 
        $data = Employee::all();
        return response()->json($data); //table er data guli json akare response e niye return koro
    }

    //define a function for inserting data 
    //now go to postman and insert the data using this $request->ja ache
    public function create(Request $request)
    {
        //insert the data
        $employee = new Employee();
        $employee->emp_id = $request->emp_id;
        $employee->name = $request->name;
        $employee->email = $request->email;
        $employee->password = $request->password;
        $employee->address = $request->address;
        $employee->doj = $request->doj;
        $employee->gender = $request->gender;
        $employee->status = $request->status;
        $employee->save();
    }

    //define a function for updating data 
    //now go to postman and update the data using this find()
    public function update(Request $request)
    {
        //update the data
        $employee = Employee::find($request->id);
        $employee->name = $request->name;
        $employee->email = $request->email;
        $employee->password = $request->password;
        $employee->address = $request->address;
        $employee->doj = $request->doj;
        $employee->gender = $request->gender;
        $employee->status = $request->status;
        $employee->save();
    }

    //define a function for deleting data 
    //now go to postman and delete the data using this find()
    public function delete(Request $request)
    {
        //delete the data
        Employee::find($request->id)->delete();
    }
}
