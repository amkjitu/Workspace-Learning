<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>
    </head>

    <body>   
        <h1>XpeedStudio Tasks</h1>
        <h2>Task-1: Creating a Custom Helper Function:</h2>
        <h3>Arr::findJitu($array)</h3>
        
        <p>
            <?php
            $array = ['jitu' => 'fixit', 'one' => 'none', 'help' => 'every one'];
            $name = 'jitu';
            echo "\$array contains: <br>";
            foreach ($array as $key => $value) {
                echo "key: {$key}, value:{$value} <br>";
            }
            echo "<br>";
            ?>
        </p>

        <p>

            {{Arr::findJitu($array)}}
            {{Arr::findAny($name,$array)}}
            {{hey($name)}}
        </p>

    </body>

    <footer class="py-16 text-center text-sm text-black dark:text-white/70">
        Laravel v{{ Illuminate\Foundation\Application::VERSION }} (PHP v{{ PHP_VERSION }})
    </footer>

</html>
