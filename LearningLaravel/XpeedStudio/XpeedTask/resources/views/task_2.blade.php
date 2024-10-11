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
        {{-- 1a. ONE TO ONE --}}
        {{-- <h2>Task-2: One to One relationship</h2> --}}
        {{-- <h3>users table 'hasOne'</h3>
            <table border="2">
            @foreach($users as $user)
                <th>{{$user->name}}</th>
                <th>{{$user->address->country}}</th>
            @endforeach
            </table> --}}

            {{-- 1b. ONE TO ONE INVERSE--}}
            {{-- <h3>addresses table 'belongsTo'</h3>
            <table border="2">
                @foreach($addresses as $address)
                <thead>
                    <th>{{$address->country}}</th>
                </thead>
                <tbody>
                    <tr>
                        <td>{{$address->user->name}}</td>
                    </tr>
                </tbody>
        
                @endforeach
            </table> --}}

            {{-- 2a. ONE TO MANY --}}
            <h2>Task-2: One to many relationship</h2>
            {{-- 
            <h3>users table 'hasMany'</h3>

            <table border="2">
            @foreach($users as $user)
            <thead>
                <th colspan="2">{{$user->name}}</th>
            </thead>
            <tbody>
                <tr>
                @foreach ($user->addresses as $address)
                    <td>{{$address->country}}</td>
                @endforeach
                </tr>
            </tbody>
            @endforeach
            </table> --}}

            {{-- 2b. ONE TO MANY  INVERSE --}}
            {{-- <h3>addresses table 'belongsTo'</h3>
            <table border="2">
                @foreach($addresses as $address)
                <thead>
                    <th>{{$address->country}}</th>
                </thead>
                <tbody>
                    <tr>
                        <td>{{$address->user->name}}</td>
                    </tr>
                </tbody>
                @endforeach
            </table> --}}
            
</body>
</html>