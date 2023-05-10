## Instalación

```shell
docker compose up --build -d
```

### Configuración de PHP

Se ingresa al contenedor `php_8_app` y se inicia el proyecto

```shell
docker exec -it php_8_app bash
```

```shell
composer init
```

Se agrega `phpunit` al composer.json

```shell
    [...]
    "require-dev": {
        "phpunit/phpunit": "^9.5"
    }
```

```shell
composer install
```

## Levantar contenedores
```shell
docker compose up -d
```

## Tumbar contenedores

```shell
docker compose down
```

## Regenerar contenedores

```shell
docker compose build --no-cache
```
