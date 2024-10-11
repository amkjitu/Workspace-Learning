@extends('layouts.master')

@section('main-body')
    
    @php
    $arr = ['Main section-1' , 'Main section-2' , 'Main section-3' , 'Main section-4'] ;
    @endphp
    <p>This page have these values:</p>
    @foreach($arr as $val)
    <p>{{$val}}</p>
    @endforeach

    <p>This value is coming from HomeController : {{$value}}</p>


@endsection