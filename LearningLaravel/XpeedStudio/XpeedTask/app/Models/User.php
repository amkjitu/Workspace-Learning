<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Relations\HasOne;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name',
        'email',
        'password',
        'project_id'
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }

    ///1a. create a ONE-TO-ONE relation: User->Address
    //the relation is: 1 ta user er 1 ta address thakbe
    // ei ralation er jonno sample table dekhle valo hoy
    /*
    'users' table
    ===|===========
    id | name
    ===|===========
    1  | jitu 
    ---|-----------
    2  | titu 
    ---|-----------

    'addresses' table
    ===|=============|===========|
    id | user_id(FK) | country   |
    ===|=============|===========|
    1  |1            | bangladesh|
    ---|-------------|-----------|
    2  |2            | usa       |
    ---|-------------|-----------|
    
    ekhane 'id-1' er couuntry only 1 ta bangladesn.
    abar 'id-2' er country only 1 ta usa.
    */

    // 'function name' must be match to the ModelName converted to lowercase
    // public function address()
    // {
    //     /// hasOne() is a function which establishes a one-to-one relation
    //     /// hasOne('Jar sathe relation hobe', 'foreign_key', 'primarykey_parentmodel');
    //     /// 'foreign_key': if 'relative model' does not use the foreigh key as per the name of 'parent model_id' 
    //     /// 'primarykey_parentmodel': if 'parent model' does not use 'id' as its primary key

    //     ///return the relation finally using hasOne(RelativeModel::class) which has the query behind the scene:
    //     //select name, country 
    //     //FROM addresses 
    //     //INNER JOIN users 
    //     //ON addresses.id = user_id
    //     return $this->hasOne(Address::class);

    //     ///return the relation finally using hasOne(RelativeModel::class,'foreign_key') which has the query behind the scene:
    //     //select name, country 
    //     //FROM addresses 
    //     //INNER JOIN users 
    //     //ON addresses.id = uid
    //     //return $this->hasOne(Address::class, 'uid');

    //     ///return the relation finally using (RelativeModel::class,'foreign_key','primarykey_parentmodel') which has the query behind the scene:
    //     //select name, country 
    //     //FROM addresses 
    //     //INNER JOIN users 
    //     //ON addresses.id = uid
    //     //return $this->hasOne(Address::class, 'uid', 'user_id');
    // }

    ///2a. create a ONE-TO-MANY relation: User->Address
    //the relation is: 1 ta user er ekadhik addresses thakbe
    //ei ralation er jonno sample table dekhle valo hoy
    /*
    'users' table
    ===|===========
    id | name
    ===|===========
    1  | jitu 
    ---|-----------
    2  | titu 
    ---|-----------

    'addresses' table
    ===|=============|===========|
    id | user_id(FK) | country   |
    ===|=============|===========|
    1  |1            | bangladesh|
    ---|-------------|-----------|
    2  |2            | usa       |
    ---|-------------|-----------|
    3  |1            | uk        |
    ---|-------------|-----------|
    4  |2            | pakistan  |
    ---|-------------|-----------|

    ekhane 'id-1' er couuntry 2 ta bangladesh, uk
    abar 'id-2' er country 2 ta usa, pakistan
    */

    // 'function name' must be match to the ModelName converted to lowercase
    public function addresses()
    {
        return $this->hasMany(Address::class);
    }

    ///2a. create a ONE-TO-MANY relation: User->Post
    public function posts()
    {
        return $this->hasMany(Post::class);
    }

    ///4i 2. create a MANT-TO-ONE relation: User->Project
    public function project()
    {
        return $this->belongsTo(Project::class);
    }

    ///4i 3. create a ONE-TO-MANY relation: User->Task
    public function tasks()
    {
        return $this->hasMany(Task::class);
    }

    ///4iii. has-many-through() 
    //Users belongsToMany Project
    public function projects()
    {
        return $this->belongsToMany(Project::class);
    }
}
