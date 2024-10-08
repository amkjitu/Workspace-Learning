<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Tag extends Model
{
    use HasFactory;
    protected $fillable = ['name'];

    ///3a. create a MANY-TO-MANY Relation: Post->Tag
    ///the relation is: 1 ta post er ekhathik tag thakte pare abar 1 ta tag er ekhadhik post thakte pare.
    //amra jani m:m relation e ekta 3rd table lage relation establish korte hole and sei table er nam hobe 'pivot' table.
    //naming convention of pivot table: model name in alphabetical order
    //for example: post and tag tables, pivot table will be: post_tag
    //creating pivot table using cmd:
    //php artisan make:migration create_post_tag_tabte --create=post_tag
    //belongsToMany('je sathe relation', 'pivot_table_name', 'foreign_key_of_the_parent_model','foreign_key_of_the_related_model')
    ///Ei function er por kaj holo RELATIONSHIP execute kora
    ///Route e relationship exucute kora hoise
    public function posts()
    {
        //return $this->belongsToMany(Tag::class, 'post_tag', 'post_id', 'tag_id'); // amra naming convention follow kortesi
        return $this->belongsToMany(Post::class); // tai oporer tar last 3 parameter skip kore
    }
}
