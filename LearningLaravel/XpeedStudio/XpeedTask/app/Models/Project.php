<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Project extends Model
{
    use HasFactory;
    protected $guarded = []; //like $fillable

    // ///4i 1. create a ONE-TO-MANY relation: Project->User
    // public function users()
    // {
    //     return $this->hasMany(User::class);
    // }

    ///4i 5. create a HAS-MANY-THROUGH relation: Project->Tasks
    // hasManyThrough(jake_direct_access_korte_chai, jar_through_te_access_korte_parbo)
    //returns the collection of objects
    // public function tasks()
    // {
    //     //return $this->HasMany(Task::class); //this will get error karon 'tasks' table e kono 'project_id' nai
    //     return $this->hasManyThrough(Task::class, User::class);
    // }

    ///4ii 1. create a HAS-ONE-THROUGH relation: Project->Task
    // hasManyThrough(jake_direct_access_korte_chai, jar_through_te_access_korte_parbo)
    //returns the single object
    // public function task()
    // {
    //     //return $this->HasOne(Task::class); //this will get error karon 'tasks' table e kono 'project_id' nai
    //     return $this->hasOneThrough(Task::class, User::class);
    // }

    ///4iii. create a HAS-MANY-THROUGH relation: Project -> Tasks 
    //has-many-through(); for many-to-many relationship  
    //Project belongsToMany Tasks
    public function tasks()
    {
        return $this->belongsToMany(
            Task::class,
            Team::class,
            'project_id', //foreign key in users table
            'user_id',    //foreign key in tasks table
            'id',         //local key in projects table
            'user_id'     //user_id of the pivot table 'project_user' 
        );
    }

    ///4iv. has-one-through() relation: Project -> Task
    public function task()
    {
        //return $this->HasOne(Task::class); //this will get error karon 'tasks' table e kono 'project_id' nai
        return $this->hasOneThrough(
            Task::class,
            Team::class,
            'project_id', //foreign key in users table
            'user_id',    //foreign key in tasks table
            'id',         //local key in projects table
            'user_id'     //user_id of the pivot table 'project_user' 
        );
    }
}
