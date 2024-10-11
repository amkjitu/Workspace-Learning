<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp,container-queries"></script>
  <style type="text/tailwindcss">
    @layer utilities {
      .container {
        @apply px-10 mx-auto;
      }
    }
  </style>
</head>
<body>
<!-- ... -->
  <div class="container">
   
   <div class="flex justify-between my-5">
    <h2 class="text-blue-500 text-xl">Create Post</h2>
    <a href="/" class="bg-blue-600 text-white rounded py-2 px-4">Back to Home</a>
   </div>

   <div>
    {{-- <form method="POST" action="{{route('store')}}"> --}}
      {{-- Solves images type related issues enctype="multipart/form-data" --}}
    <form method="POST" action="{{route('store')}}" enctype="multipart/form-data">
        <!-- What is Cross-Site Request Forgery (CSRF)
        CSRF is a malicious activity that involves an attacker performing actions on behalf of an authenticated user.
        For each user session, Laravel generates secured tokens that it uses to ensure that the authenticated user is the one requesting the application.
        Each time there’s a request to modify user information on the server-side (back end) like POST, PUT, PATCH, and DELETE, you need to include a 'csrf' in the HTML form request. The 'csrf' is thus a Blade directive used to generate a hidden token validated by the application.
        -->
        @csrf
        <div class="flex flex-col gap-8">
            <label for="">Name</label>
            <input type="text" name="name" value="{{old('name')}}">
            @error('name')
                <p class="text-red-600">{{$message}}</p>
            @enderror

            <label for="">Description</label>
            <input type="text" name="description" value="{{old('description')}}">
            @error('description')
                <p class="text-red-600">{{$message}}</p>
            @enderror

            <input type="file" name="image">
            <div>
                <input type="submit" class="bg-green-600 text-white rounded py-2 px-4">
            </div>
            @error('image')
                <p class="text-red-600">{{$message}}</p>
            @enderror
            
        </div>
    </form>
   </div>
    
  </div>
</body>
</html>