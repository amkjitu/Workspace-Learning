<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Comment extends Model
{
    use HasFactory;
    protected $guarded = [];

    ///5i 3. create One-to-Many Polymorphic Relationship: Comment-> can only have one 'Post' or 'Video'
    public function commentable()
    {
        return $this->morphTo();
    }
}
