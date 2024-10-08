<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <h1>XpeedStudio Tasks</h1>
        {{-- 2b. ONE TO MANY Inverse--}}
        {{-- <h2>Task-2: One to Many relationship</h2> --}}
        {{-- <h3>posts table 'belongsToMany'</h3> --}}
    <div class="container">
        <table border="2">
            <thead> 
            {{-- @foreach ($posts as $post)    --}}
            {{-- <th>{{$post->title}}</th> --}}
            </thead>
            <tbody>
            {{-- <tr> {{optional($post->user)->name}} </tr>    --}}
            </tbody>
            {{-- jodi default value use kora thake tahole nicher ta 
            <p>{{$post->user->name}}</p> --}}           
            {{-- @endforeach --}}
            
        </table>
    </div>

    {{-- 2a. ONE TO MANY --}}
    {{-- <h2>Task-2: One to Many relationship</h2> --}}
    {{-- <h3>users table 'hasMany'</h3> --}}
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                {{-- @foreach ($users as $user) --}}
                <div class="card">
                    {{-- <h2>{{$user->name}}</h2> --}}
                    {{-- @foreach($user->posts as $post) --}}
                    {{-- <p>{{$post->title}}</p> --}}
                    {{-- @endforeach --}}
                </div>
                {{-- @endforeach --}}
            </div>
        </div>
    </div>

    {{-- 3b. ONE TO MANY INVERSE--}}
    <h2>Task-2: Many to Many Inverse relationship</h2> 
    <h3>posts table 'belongsToMany'</h3>

    <div border="2">

        <tr>
        @foreach ($posts as $post)
        
        <h4> {{$post->title}} </h4>
    
        <p> {{$post->user->name}} </p>
        <ul style="color: green">
            @foreach ($post->tags as $tag)
                <li>{{$tag->name}} [created at: {{ $tag->pivot->created_at}}]</li>
                <li>[status: {{ $tag->pivot->status}}]</li>
            @endforeach
        </ul>
        
        @endforeach
    </tr>
   
    </div>
    
    
</body>
</html>
