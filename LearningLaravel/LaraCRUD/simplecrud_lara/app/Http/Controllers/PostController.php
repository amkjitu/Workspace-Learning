<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;

class PostController extends Controller
{
    //For Viewing
    public function create()
    {
        return view('create');
    }

    ///For Model
    public function store_data(Request $request)
    {
        ///Validate the data coming from create view
        $validated = $request->validate([
            'name' => 'required',
            'description' => 'required',
            'image' => 'nullable|mimes:jpeg,jpg,png'
        ]);

        ///Inserting the data to the table 'post' coming from crate view
        $post = new Post();
        $post->name = $request->name;
        $post->description = $request->description;
        //$post->image = $request->image; //stores the file name as it is in the database
        if (isset($request->image))
            $post->image = time() . '.' . $request->image->extension(); //ensuring unique file name of image

        ///Storing Image in the app 'public' folder which is chosen in the form
        if (isset($request->image)) {
            $imageName = time() . '.' . $request->image->extension();
            $request->image->move(public_path('images'), $imageName);
        }

        $post->save();
        return redirect()->route('home')->with('success', 'your post has been CREATED!');
    }

    public function edit_data($id)
    {
        $post = Post::findOrFail($id);
        return view('edit', ['post' => $post]);
    }

    public function update_data($id, Request $request)
    {
        ///Validate the data coming from create view
        $validated = $request->validate([
            'name' => 'required',
            'description' => 'required',
            'image' => 'nullable|mimes:jpeg,jpg,png'
        ]);

        ///Updating the data to the table 'post' coming from crate edit view
        $post = Post::findOrFail($id);
        $post->name = $request->name;
        $post->description = $request->description;
        //$post->image = $request->image; //stores the file name as it is in the database
        if (isset($request->image))
            $post->image = time() . '.' . $request->image->extension(); //ensuring unique file name of image

        ///Storing Image in the app 'public' folder which is chosen in the form
        if (isset($request->image)) {
            $imageName = time() . '.' . $request->image->extension();
            $request->image->move(public_path('images'), $imageName);
        }

        $post->save();
        return redirect()->route('home')->with('success', 'your post has been UPDATED!');
    }

    public function delete_data($id)
    {
        $post = Post::findOrFail($id);
        $post->delete();

        return redirect()->route('home')->with('success', 'your post has been DELETED!');
    }

    public function search_data(Request $request)
    {
        $search = $request->input('search');
        //$posts = Post::where('name', 'like', "%$search%")->get(); //all the result
        $posts = Post::where('name', 'like', "%$search%")->paginate(5);
        return view('welcome', ['posts' => $posts]);
    }
}
