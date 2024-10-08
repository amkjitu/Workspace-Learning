<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{-- 3a. ONE TO MANY --}}
    <h2>Task-2: Many to Many relationship</h2> 
    <h3>tags table 'belongsToMany'</h3>

    <div border="2">

        <tr>
        @foreach ($tags as $tag)
        
        <h4> {{$tag->name}} </h4>
    
        <ul style="color: green">
            @foreach ($tag->posts as $post)
                <li>{{$post->title}}</li>
            @endforeach
        </ul>
        
        @endforeach
    </tr>
   
    </div>
</body>
</html>