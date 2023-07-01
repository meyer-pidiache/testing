<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RegisterController extends Controller
{
    // GET: index | POST: store | DELETE: destroy
    // More: https://laravel.com/docs/10.x/controllers#actions-handled-by-resource-controller
    
    public function index()
    {
        return view('auth.register');
    }

    public function store()
    {
        dd('Post...');
    }
}
