<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class Check
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        if ($request->varify > 30) {
            //Check pass na korle -> display nijer moto
            echo "Global Middleware says, Age = " . $request->varify . "<br>Sorry tmr chakrir boyosh sesh";
            die;

            //Check pass na korle -> Forbitten 
            //abort(403);

            //Check pass na korle -> redirect to some url
            //return redirect('/');
        }
        return $next($request);
    }
}
