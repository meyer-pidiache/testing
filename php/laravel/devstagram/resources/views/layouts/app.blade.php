<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>@yield('titulo')</title>
        @vite('resources/css/app.css    ')
    </head>
    <body>
        <nav>
            <a href="/">Principal</a>
            <a href="/tienda">Tienda</a>
            <a href="/nosotros">Sobre Nosotros</a>
        </nav>
        <h1 class="text-4xl">@yield('titulo')</h1>
        <hr>
        <p>@yield('contenido')</p>
    </body>
</html>