# Manual da API Anime Stock

Sistema para o armazenamento de animes usando Flask, PostgreSQL, Blueprints e Psycopg2.

## Cadastrar anime:
POST http://{BASE_URL}/animes

```json
{
	"anime": "Sword Art Online",
	"released_date": "10/04/2009",
	"seasons": 5
}

```
#

## Ver todos os animes:
GET http://{BASE_URL}/animes

```json
{
  "data": [
    {
      "anime": "Sword Art Online",
      "id": 1,
      "released_date": "Fri, 10 Apr 2009 00:00:00 GMT",
      "seasons": 5
    },
    {
      "anime": "One Piece",
      "id": 2,
      "released_date": "Wed, 20 Oct 1999 00:00:00 GMT",
      "seasons": 21
    }
  ]
}

```
#

## Acessar um anime pelo ID:
GET http://{BASE_URL}/animes/anime_id
#

## Atualizar um anime:
PATCH http://{BASE_URL}/animes/anime_id

```json
{
    "<field>": "<value>",
}
```
#

## Deletar um anime:
DELETE http://{BASE_URL}/animes/anime_id
#