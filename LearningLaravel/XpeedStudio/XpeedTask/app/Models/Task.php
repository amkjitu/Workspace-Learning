<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    use HasFactory;
    protected $guarded = []; //like $fillable

    ///4i 4. create a MANY-TO-ONE relation: Task->User
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
