Creating a Laravel Project
Before creating your first Laravel project, make sure that your local machine has PHP and Composer installed. If you are developing on macOS or Windows, PHP, Composer, Node and NPM can be installed in minutes via Laravel Herd. And XXAMP is running.

After you have installed PHP and Composer, you may create a new Laravel project via Composer's create-project command:
-----------------------------------

=====>1. composer create-project laravel/laravel example-app

Or, you may create new Laravel projects by globally installing the Laravel installer via Composer. The Laravel installer allows you to select your preferred testing framework, database, and starter kit when creating new applications:

=====>1. composer global require laravel/installer
 
=====>2. laravel new example-app

Once the project has been created, start Laravel's local development server using Laravel Artisan's serve command:
-------------------------

=====>3. cd example-app
 
=====>4. php artisan serve

Once you have started the Artisan development server, your application will be accessible in your web browser at http://localhost:8000. Next, you're ready to start taking your next steps into the Laravel ecosystem. Of course, you may also want to configure a database.

If you would like a head start when developing your Laravel application, consider using one of our starter kits. Laravel's starter kits provide backend and frontend authentication scaffolding for your new Laravel application.

Initial Configuration
All of the configuration files for the Laravel framework are stored in the config directory. Each option is documented, so feel free to look through the files and get familiar with the options available to you.

Laravel needs almost no additional configuration out of the box. You are free to get started developing! However, you may wish to review the config/app.php file and its documentation. It contains several options such as timezone and locale that you may wish to change according to your application.

Environment Based Configuration
Since many of Laravel's configuration option values may vary depending on whether your application is running on your local machine or on a production web server, many important configuration values are defined using the .env file that exists at the root of your application.

Your .env file should not be committed to your application's source control, since each developer / server using your application could require a different environment configuration. Furthermore, this would be a security risk in the event an intruder gains access to your source control repository, since any sensitive credentials would be exposed.

For more information about the .env file and environment based configuration, check out the full configuration documentation.

Databases and Migrations
Now that you have created your Laravel application, you probably want to store some data in a database. By default, your application's .env configuration file specifies that Laravel will be interacting with a SQLite database.

During the creation of the project, Laravel created a database/database.sqlite file for you, and ran the necessary migrations to create the application's database tables.

If you prefer to use another database driver such as MySQL or PostgreSQL, you can update your .env configuration file to use the appropriate database. For example, if you wish to use MySQL, update your .env configuration file's DB_* variables like so:
------------------------------------------------------------------------

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

If you choose to use a database other than SQLite, you will need to create the database and run your application's database migrations:
-------------------------------------------

=====>5. php artisan migrate