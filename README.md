<h1>Тестовое на стажировку по направлению "Python разработчик" в UDV</h1>

<h2>Инструкция по запуску</h2>
<ol>
  <li>Склонировать репозиторий</li>
  <li>Установить зависимости через `pip install -r requirements.txt`</li>
  <li>Запустить проект через `uvicorn main:app --reload`</li>
</ol>
<h2>Эндпоинты:<br></h2>
<b>"/"</b> - возвращает данные в виде:

```
{
  "news": [
    {
      "id": 1,
      "title": "news_1",
      "date": "2024-01-01T20:56:35",
      "body": "The news",
      "deleted": false,
      "comments_count": 1
    }
  ],
  "news_count": 1
}
```
Игнорирует news с deleted: true<br>
<b>"news/id"</b> - возвращает данные в виде:
```
{
  "id": 1,
  "title": "news_1",
  "date": "2024-01-01T20:56:35",
  "body": "The news",
  "deleted": false,
  "comments": [
    {
      "id": 1,
      "news_id": 1,
      "title": "comment_1",
      "date": "2024-01-02T21:58:25",
      "comment": "Comment"
    }
  ],
  "comments_count": 1
}
```
При вызове с несуществующим id или с news, у которой deleted: true, вернет 404 код ошибки
