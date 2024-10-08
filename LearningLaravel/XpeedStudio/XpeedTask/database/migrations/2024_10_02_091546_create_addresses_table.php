<?php
//task-2:
/*
Create a one-one relationship model
User model is related to Address

address
-----------------------
id| user_id | country|
-----------------------
*user_id is foreign key

*/

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('addresses', function (Blueprint $table) {
            //first argument is always primary key
            //second argument is foreign key
            $table->id(); //primary key

            //here 'user_id' is by default -> foreign key; how: finds 'User' model then finds 'id' attribute in this model
            $table->bigInteger('user_id'); //foreignkey

            //here 'uid' is saying explicitly -> foreign key; how: finds 'User' model then finds 'id' attribute in this model
            //$table->bigInteger('uid'); foreignkey

            $table->string('country');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('addresses');
    }
};
