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
      .btn{
        @apply bg-green-600 text-white rounded py-2 px-4;
      }
      .btn-edit{
        @apply bg-purple-800 text-white rounded py-2 px-4;
      }
      .btn-dlt{
        @apply bg-red-600 text-white rounded py-2 px-4;
      }
    }
  </style>
</head>
<body>
<!-- ... -->
  <div class="container">
   
   <div class="flex justify-between my-5">
    <h2 class="text-red-500 text-xl">Home</h2>

    <form action="{{route('search')}}" method="GET">
      <input type="text" name="search" placeholder="Search Posters">
      <button type="submit" class="py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-800 bg-white text-gray-800 shadow-sm hover:bg-gray-50 focus:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-800 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-700 dark:focus:bg-neutral-700">
        Search
      </button>
   </form>

    <a href="/create" class="btn">Add New Post</a>
    {{-- <form action="{{ route('products.search') }}" method="GET"> --}}
    
   </div>

   @if(session('success'))
       <h2 class="text-green-600" py-5 mx-auto>{{session('success')}}</h2>
   @endif
      
   <div class="">
    <div class="flex flex-col">
      <div class="-m-1.5 overflow-x-auto">
        <div class="p-1.5 min-w-full inline-block align-middle">
          <div class="border rounded-lg shadow overflow-hidden">
            <table class="min-w-full divide-y divide-gray-400" >
              <thead>
                <tr>
                  <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">ID</th>
                  <th scope="col" class="px-6 py-6 text-start text-xs font-medium text-gray-500 uppercase">Name</th>
                  <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Description</th>
                  <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase">Image</th>
                  <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase">Action</th>
                </tr>
              </thead>
              <tbody>
                
                @foreach ($posts as $post)
            
                <tr class="odd:bg-white even:bg-gray-100">
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                  {{$post->id}}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">{{$post->name}}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800">{{$post->description}}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800"><img src="images/{{$post->image}}" width="50px" alt="img"></td>
                  <td class="px-6 py-4 whitespace-nowrap text-end text-sm font-medium">
                    <a href="{{route('edit',$post->id)}}" class="btn-edit">Edit</a>
                    <a href="{{route('delete',$post->id)}}" class="btn-dlt">Delete</a>
                  </td>
                </tr>

                @endforeach
    
              </tbody>
            </table>
            <hr>
            <div style="margin: 10px; padding: 10px;">
              {{$posts->links()}}
            </div>
            
          </div>
        </div>
      </div>
    </div>
   </div>
    
  </div>
</body>
</html>