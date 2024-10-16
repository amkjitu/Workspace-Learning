<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    use HasFactory;
    protected $fillable = ['user_id', 'title'];


    public function user()
    {
        //return $this->belongsTo(User::class);

        //default value set kore belongsTo dile user er kono value na thakle post seta default e ja thake ta show kore
        return $this->belongsTo(User::class)->withDefault([
            'name' => 'Guest User'
        ]);
    }

    ///3b. create a MANY-TO-MANY INVERSE relation: Post->Tag
    ///the relation is: 1 ta post er ekhathik tag thakte pare abar 1 ta tag er ekhadhik post thakte pare.
    //amra jani m:m relation e ekta 3rd table lage relation establish korte hole and sei table er nam hobe 'pivot' table.
    //naming convention of pivot table: model name in alphabetical order
    //for example: post and tag tables, pivot table will be: post_tag
    //creating pivot table using cmd:
    //php artisan make:migration create_post_tag_tabte --create=post_tag
    //belongsToMany('je sathe relation', 'pivot_table_name', 'foreign_key_of_the_parent_model','foreign_key_of_the_related_model')
    ///Ei function er por kaj holo RELATIONSHIP execute kora
    ///Route e relationship exucute kora hoise
    public function tags()
    {
        //return $this->belongsToMany(Tag::class, 'post_tag', 'post_id', 'tag_id'); // amra naming convention follow kortesi
        // return $this->belongsToMany(Tag::class); // tai oporer tar last 3 parameter skip kore

        //by default pivot table foreign keys guli chara timestamp column gulir date update kore na tai return e etak explicitly bole dite hoy
        //return $this->belongsToMany(Tag::class)->withTimestamps();

        //pivot table e foreign keys chara onno column add kora jay er jonno update the migration file ekta 'status' column create korbo string typer
        // withPivot('column_name');
        return $this->belongsToMany(Tag::class)->withTimestamps()->withPivot('status');
    }

    ///5i 1. create One-to-Many Polymorphic Relationships: Post->Comment
    public function comments()
    {
        return $this->morphMany(Comment::class, 'commentable');
    }
}
