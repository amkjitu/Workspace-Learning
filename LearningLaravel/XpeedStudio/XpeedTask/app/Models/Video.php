<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Video extends Model
{
    use HasFactory;
    protected $guarded = [];

    ///5i 2. create One-to-Many Polymorphic Relationships: Video->Comment
    public function comments()
    {
        return $this->morphMany(Comment::class, 'commentable');
    }
}
