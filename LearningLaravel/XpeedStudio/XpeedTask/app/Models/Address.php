<?php
//Task-2

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Address extends Model
{
    use HasFactory;

    protected $fillable = ['user_id', 'country'];

    //1b.create a ONE-TO-ONE INVERSE relation: Address->User
    //the relation is:1 ta address er shapekkhe  1 ta user thakbe
    //'function name' must be match to the ModelName converted to lowercase
    //baki ja ja poriborton korar ache shob hasOne() er poriborton er motoi
    // public function user()
    // {
    //     return $this->belongsTo(User::class);
    // }

    //2b.create a ONE-TO-MANY INVERSE relation: Address->User
    //the relation is:ekadhik addresses er shapekkhe  1 ta user thakbe
    //'function name' must be match to the ModelName converted to lowercase
    //baki ja ja poriborton korar ache shob hasMany() er poriborton er motoi
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
