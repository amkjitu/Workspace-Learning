<?php

use App\Http\Controllers\ProfileController;

use Carbon\Factory;
use Illuminate\Support\Facades\Route;

///Task-1
Route::get('/task_1', function () {
    return view('task_1');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});
/*---------------------------------------------------------------------------------*/

///Task-2
Route::get('/task_2', function () {
    ///1a.One-to-One Relationship
    ///i. hasOne()
    //dump data using factory is not working
    //factory(\App\Models\User::class, 3)->create();

    //insert this data to addresses table OBOSSOI insert korar por code ta comment kore dio tana hole same data bar bar add hobe
    // \App\Models\User::create([
    //     'name' => 'titu',
    //     'email' => 'tmkhanshadhin@gmail.com',
    //     'password' => 'titu'
    // ]);

    ///insert this data to addresses table OBOSSOI insert korar por code ta comment kore dio tana hole same data bar bar add hobe
    // \App\Models\Address::create([
    //     'user_id' => 1,
    //     'country' => 'Bangladesh'
    // ]);
    // \App\Models\Address::create([
    //     'user_id' => 2,
    //     'country' => 'Pakistan'
    // ]);
    // \App\Models\Address::create([
    //     'user_id' => 3,
    //     'country' => 'India'
    // ]);

    //fetching the data from User model
    //$users = \App\Models\User::all();
    //fetching(more efficiently) the data from User model using "Eager Loading"
    //$users = \App\Models\User::with('address')->get();
    //return view('task_2', compact('users'));

    ///ii. Inverse relation: belongsTo()
    //fetching the data from Address model
    //$addresses = \App\Models\Address::all();
    //fetching(more efficiently) the data from User model using "Eager Loading"
    // $addresses = \App\Models\Address::with('user')->get();
    // return view('task_2', compact('addresses'));

    ///another way to make relation
    // $user = factory(\App\Models\User::class)->create();
    // $address = new \App\Models\Address([
    //     'country' => 'UK'
    // ]);
    // $address->user()->assciate($user);
    // $address->save();
    //$addresses = \App\Models\Address::all();
    // return view('task_2', compact('addresses'));

    ///2a. One-to-Many Relationship
    ///i. hasOne()
    //fetching(more efficiently) the data from User model using "Eager Loading"
    // $users = \App\Models\User::with('addresses')->get();

    ///insert this data to addresses table OBOSSOI insert korar por code ta comment kore dio tana hole same data bar bar add hobe
    // \App\Models\Address::create([
    //     'user_id' => 1,
    //     'country' => "uk"
    // ]);
    // return view('task_2', compact('users'));

    ///ii. Inverse relation: belongsTo()
    //fetching(more efficiently) the data from User model using "Eager Loading"
    // $addresses = \App\Models\Address::with('user')->get();
    // return view('task_2', compact('addresses'));

    /*
    For understanding ONE-TO-MANY Relationships now we will create a "Post" model where a 'User' may have multiple posts. 
    kintu eta ekta vinno route e korbo route holo: 'task_2_posts'
    ekhane kichu methods shikhbo: existance, absence
    php artisan make:model Post -m
    */
});

Route::get('task_2_posts', function () {
    ///first insert some data for the posts table, insert kore obossoi comment
    // \App\Models\Post::create([
    //     'user_id' => 1,
    //     'title' => 'post title 1',
    // ]);
    // \App\Models\Post::create([
    //     'user_id' => 2,
    //     'title' => 'post title 2',
    // ]);
    // \App\Models\Post::create([
    //     // eta guest user tai user id nai say for example like blog
    //     // but jokhon eta oporer gulir moto print korte chaibo error ashbe
    //     // solve ta holo use a helper function: optional() 
    //     'title' => 'post title 3 [anonymous]',
    // ]);

    /// ONE-TO-MANY INVERSE Relation 
    ///now fetch the data from posts table
    // $posts = \App\Models\Post::all();
    //check kori user[2]->user ache kina
    //dd($posts[2]->user); // will print null
    // return view('/task_2_posts', compact('posts'));

    /// ONE-TO-MANY Relation 
    ///now fetch all data from posts table
    //$users = \App\Models\User::all();
    //fetch those users who has post
    //$users = \App\Models\User::has('posts')->all();
    //efficent fecth those users who has post
    //$users = \App\Models\User::has('posts')->with('posts')->get();
    //fetch the user who has 2 or more posts
    //$users = \App\Models\User::has('posts', ">=", 2)->with('posts')->get();
    //fetch the user where post has "tile" 
    // $users = \App\Models\User::whereHas('posts', function ($query) {
    //     $query->where('title', 'like', '%tile%');
    // })->with('posts')->get();
    //fetch only those users who has not created any post
    // $users = \App\Models\User::doesntHave('posts')->with('posts')->get();
    // return view('/task_2_posts', compact('users'));

    ///3b. Many-to-Many Inverse Relationship
    ///i. belongsToMany 
    ///Here the relationship is Post->Tag
    /*
    For understanding MANY-TO-MANY Relationships now we will create a "Tag" model where a 'Post' may have multiple 'Tag' and a 'Tag' may have multiple 'Post'. amra jani m:m relation e ekta 3rd table lage relation establish korte hole and sei table er nam hobe 'pivot' table.
    php artisan make:model Tag -m
    */

    ///step-0: Post model is allready created
    ///step-1: created 'Tag' model
    ///step-2: created post_tag pivot table in the 'Post' model see this "3a. create a MANY-TO-MANY relation: Post->Tag"
    ///step-3: execute the attachment of tags and posts
    ///step-4: post er user data abong oi post er tag data 'task_2_posts' view ta compact kore pass kora

    ///first insert some data for the posts table, insert kore obossoi comment
    // \App\Models\Tag::create([
    //     'name' => 'laravel'
    // ]);
    // \App\Models\Tag::create([
    //     'name' => 'php'
    // ]);
    // \App\Models\Tag::create([
    //     'name' => 'js'
    // ]);
    // \App\Models\Tag::create([
    //     'name' => 'vuejs'
    // ]);

    ///step-3: execute the attachment of tags and posts
    //relation attach kori: Tag er first 'id' ta Post er first 'id' er sathe
    //$tag = \App\Models\Tag::first();
    $post = \App\Models\Post::first();
    //execute the above relationship below:
    //$post->tags()->attach($tag);

    //aro relation attach kori: post er id-1 er sathe tag er id-2, id-3 id-4
    //$post->tags()->attach([2, 3, 4]);

    //ekhon detach kori id-1 ke: 
    // $post = \App\Models\Post::with('tags')->first();
    // $post->tags()->detach([1]);

    //ekhon attach update kori:
    // $post = \App\Models\Post::with('tags')->first();
    // $post->tags()->sync([2, 3]);

    //by default pivot table foreign keys guli chara timestamp column gulir date update kore na tai return e etak explicitly bole dite hoy
    //see how it is done in 'Post' model

    //pivot table e foreign keys chara onno column add kora jay er jonno update the migration file ekta 'status' column create korbo string typer
    //Post model e ei colum er kotha ullekh na korle show korbe na, Post model e 
    //lets create some attachs to tags table
    $post->tags()->attach([1 => ['status' => 'approved']]);


    ///step-4: post er user data abong oi post er tag data 'task_2_posts' view ta compact kore pass kora
    $posts = \App\Models\Post::with(['user', 'tags'])->get();
    return view('/task_2_posts', compact('posts'));

    ///3a. Many-to-Many Relationship
    ///ii. belongsToMany 
    ///Ei relation bojhar jonno notun route 'task_2_tags' ta dekhte hobe
});

Route::get('task_2_tags', function () {
    ///3a. Many-to-Many Relationship
    ///ii. belongsToMany 

    $tags = \App\Models\Tag::with('posts')->get();
    return view('task_2_tags', compact('tags'));

    ///Aro kichu Advanced Relationship dekhbo eta khub important
    ///4i. has-many-through() ; one-to-many relationship
    ///4ii. has-one-through() ; ont-to-one ralationship
    ///4iii. has-many-through() ; using Pivot model jekhane **many-to-many relationship thakbe
    ///ei tinta Relationship bojhar jonno amra notun ekta route create korbo seta holo 'task_2_projects'
    ///niche seta details ache

});

Route::get('task_2_projects', function () {
    ///4i. has-many-through()
    ///lets see a use case:
    /*
    Table 'Project'
    --------------


    Table 'User'
    ------------
        project_id

    Table 'Task'
    ------------
        user_id

    *Amra ja chai: $project->task
    //ei queryr spaciality ki? project er sathe task nai kintu tobuo amra project theke direct task anbo
    etar vitore THROUGH logic ashbe see: PROJECT theke TASK guli ashbe USER er THROUGH te
    eta pete hole amader 'Project' Model e tasks and user er Has-Many-Through relationship toiri korte hobe 
    //eta kivabe kaj kore eta 'Project' model e explain kora ache tasks(kake,through) er vitore
    */
    ///Steps:
    //create 'Project' model
    //create 'Task' model
    //'User' model ache already just table 'project_id' column ta add korbo
    ///Relationship ta jevabe ache:
    //1.Project hasMany Users
    //2.User belongsTo Project 
    //3.User hasMany Tasks
    //4.Task belongsTo User
    //5.Project hasManyThrough Tasks,Users
    ///After creating the above relationships to the respective Model lets insert some data

    // ///insert some projects to the table
    // $project = \App\Models\Project::create([
    //     'title' => 'Project A'
    // ]);
    // ///insert some users to the table
    // $user1 = \App\Models\User::create([
    //     'name' => 'User 1',
    //     'email' => 'user1@example.com',
    //     'password' => 'password1',
    //     'project_id' => $project->id
    // ]);
    // $user2 = \App\Models\User::create([
    //     'name' => 'User 2',
    //     'email' => 'user2@example.com',
    //     'password' => 'password2',
    //     'project_id' => $project->id
    // ]);
    // ///insert some tasks to the table
    // $task1 = \App\Models\Task::create([
    //     'title' => 'Task-1 for project-1 by user-1',
    //     'user_id' => $user1->id
    // ]);
    // $task2 = \App\Models\Task::create([
    //     'title' => 'Task-2 for project-1 by user-1',
    //     'user_id' => $user1->id
    // ]);
    // $task3 = \App\Models\Task::create([
    //     'title' => 'Task-3 for project-1 by user-2',
    //     'user_id' => $user2->id
    // ]);

    ///lets see amra ki ki access korte pari
    //$project = \App\Models\Project::find(1);
    //return $project; //project access korte pari using project-id:1 
    //return $project->users;  //project theke user access korte pari using project-id:1 
    //return $project->tasks;  //project theke task access korte parbo na, karon ekhono has through relation toiri hoy ni eta 'Project' Model e
    //see 'Project' Model how the hasManyThrough() relation is established 


    ///4ii. has-one-through()
    //data guli 4i e insert kora e ache
    //1.Project hasOneThrough Tasks,Users
    //$project = \App\Models\Project::find(1);
    //return $project->task;
    //see 'Project' Model how the hasManyThrough() relation is established 


    ///4iii. has-many-through() ; using Pivot model jekhane **many-to-many relationship thakbe
    //jemon ekhane 1 ta 'project' er ekadhik 'users' thakta pare abong 1 ta 'user' er akadhik 'projects' thakte pare.
    //'project' and 'user' er relation ta many-to-many jeta 'pivot' table dara toiri kora jay   
    //nicher use case lokkho korle dekha jay je ager moto project->task access kora jacche na
    //etar karon holo users table e project_id name kono column nai
    //
    /*
    'projects' Table
    ----------------
    id

    'users' Table
    -------------
    id

    'project_user' pivot Table
    --------------------
    project_id
    user_id

    'tasks' Table
    -------------
    id
    user id

    */

    ///*Amra ja chai: $project->task
    ///Steps:
    ///1. create pivot table 'project_user': php artisan make:migration create_project_user_table --create=project_user
    ///2. create a pivot model 'team': php artisan make:mode Team 
    ///3. goto Team model and extands to 'Pivot' instead of Model

    ///Relationship ta jevabe ache:
    //1.Project belongsToMany Users
    //2.User belongsToMany Projects

    /////3.User hasMany Tasks
    /////4.Task belongsTo User
    /////5.Project hasManyThrough Tasks,Users

    // ///insert some projects to the table
    // $project1 = \App\Models\Project::create([
    //     'title' => 'Project A'
    // ]);
    // $project2 = \App\Models\Project::create([
    //     'title' => 'Project B'
    // ]);
    // ///insert some users to the table
    // $user1 = \App\Models\User::create([
    //     'name' => 'User 1',
    //     'email' => 'user1@example.com',
    //     'password' => 'password1'
    // ]);
    // $user2 = \App\Models\User::create([
    //     'name' => 'User 2',
    //     'email' => 'user2@example.com',
    //     'password' => 'password2'
    // ]);
    // $user3 = \App\Models\User::create([
    //     'name' => 'User 3',
    //     'email' => 'user3@example.com',
    //     'password' => 'password3'
    // ]);

    // ///attach the projects and users to the pivot table 'project_user'
    // $project1->users()->attach($user1);
    // $project1->users()->attach($user2);
    // $project1->users()->attach($user3);

    // $project2->users()->attach($user1);
    // $project2->users()->attach($user3);


    // ///insert some tasks to the table
    // $task1 = \App\Models\Task::create([
    //     'title' => 'Task-1 for project-1 by user-1',
    //     'user_id' => 1 // $user1->id
    // ]);
    // $task2 = \App\Models\Task::create([
    //     'title' => 'Task-2 for project-1 by user-2',
    //     'user_id' => 2 // $user1->id
    // ]);
    // $task3 = \App\Models\Task::create([
    //     'title' => 'Task-3 for project-1 by user-3',
    //     'user_id' => 3 // $user2->id
    // ]);
    // $task4 = \App\Models\Task::create([
    //     'title' => 'Task-4 for project-1 by user-1',
    //     'user_id' => 1 // $user2->id
    // ]);

    ///lets see amra ki ki access korte pari
    // $project = \App\Models\Project::find(2);
    // //return $project; //project access korte pari using project-id:1 
    // //return $project->users;  //project theke user access korte pari using project-id:1 
    // return $project->tasks;  //project theke task access korte parbo na, karon ekhono has through relation toiri hoy ni eta 'Project' Model e
    // //see 'Project' Model how the hasManyThrough() relation is established 


    ///4iv. has-one-through() 
    ///lets see amra ki ki access korte pari
    $project = \App\Models\Project::find(1);
    //return $project; //project access korte pari using project-id:1 
    //return $project->users;  //project theke user access korte pari using project-id:1 
    return $project->task;  //project theke task access korte parbo na, karon ekhono has through relation toiri hoy ni eta 'Project' Model e
    //see 'Project' Model how the hasManyThrough() relation is established 


});

Route::get('task_2_projects', function () {
    /*
    5. Polymorphic Relationships
    5i. One-to-Many Polymorphic Relationships
    5ii. One-to-One Polymorphic Relationships
    5iii. Many-to-Many Polymorphic Relationships

    Use Cases: 5i. One-to-Many Polymorphic Relationships
    -----------------------------------------------------
    A user can comment in both Post and Video (and others type so far)
    Solution-1: normal not good
    *Post 
        PostComment
    *Video
        VideoComment
    Solution-2: common comment table not also good
    *Post 
        
    *Video

    *Podcast
        
    *Comment
        post_id
        video_id
        podcast_id
    Solution-3: polymorphic approach
    *Post 
        
    *Video

    *Podcast
        
    *Comment
        commentable_id
        commentable_type
    */

    ///Steps:
    //1. create 'Video' Model: php artisan make:model Video -m 
    //2. create 'Comment' Model: php artisan make:model Comment -m

    ///Relationship ta jevabe ache:
    //1. One-to-Many Polymorphic (ekta post er ekadhik comment thakte pare): Post morphMany Comment
    //2. One-to-Many Polymorphic (ekta video er ekadhik comment thakte pare): Video morphMany Comment

    ///Now:
    //1. create  One-to-Many Polymorphic relation to the Post model
    //2. create  One-to-Many Polymorphic relation to the Video model
    //3. create  One-to-Many Polymorphic relation to the Comment model

    ///Insert Data
    //users
    $user = \App\Models\User::create([
        'name' => 'titu',
        'email' => 'tmkhanshadhin@gmail.com',
        'password' => 'titu'
    ]);
    //posts
    $post = \App\Models\Post::create([
        'user_id' => $user->id,
        'title' => 'post title',
    ]);
    //comments
    $post->comments()->create([
        'user_id' => $user->id,

    ]);
});


require __DIR__ . '/auth.php';
