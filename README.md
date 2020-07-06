# furport-back

[![deploy](https://github.com/lapi-hotel-group/furport-back/workflows/deploy/badge.svg)](https://github.com/lapi-hotel-group/furport-back/actions?query=workflow%3Adeploy)
[![Lint](https://github.com/lapi-hotel-group/furport-back/workflows/Lint/badge.svg)](https://github.com/lapi-hotel-group/furport-back/actions?query=workflow%3ALint)

## Requirements

- docker
- docker-compose
- node
- pip

## Build

```
npm install
pip install -r requirements.txt
docker-compose up -d
```

access http://localhost:8080

## `manage.py` のコマンドをやるためにコンテナに入る

```
docker-compose exec app bash
# python manage.py migrate
# python manage.py collectstatic
```

## `docker/app/requirements.txt` を編集した時

```
docker-compose up -d --build
```
