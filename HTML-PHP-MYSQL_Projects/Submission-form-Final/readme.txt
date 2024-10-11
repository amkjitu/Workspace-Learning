Visit below link for the live demo of the project 
http://subform.infinityfreeapp.com/
-------------------------------------------------

How to install the project on localhost
=======================================
Step-0 Unzip the project file into "xampp\htdocs\" on your PC.

Step-1 Goto http://localhost/phpmyadmin/index.php and Create a database named "auditors".

Step-2 Now import necessary table to that database. For this click on the database "auditors" after that click from the upper tab menu "Import". Choose File and upload: Goto the project file and find "submissions.sql". Finally click on "Import" at the bottom of the page. 

Step-3 Set the database connection credential in the file named "dbConnect.php" located in the project file as below and save it: 
      private $host = 'localhost';
      private $username = 'root';
      private $password = '';
      private $database = 'auditors';

Step-4 Open Xampp and start Apache and MySQL

Finally Run the project file "Submission-Form" from localhost: "http://localhost/Submission-Form/" from any browser of the local pc.
==================================================================================
######################################Thank You###################################