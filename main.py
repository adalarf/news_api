from fastapi import FastAPI
from news_and_comments_service.router import router


app = FastAPI()
app.include_router(router)


# async def load_data(file_path):
#     with open(file_path) as file:
#         return json.load(file)
#
#
# async def get_news_comments(comments: dict, id: int) -> list:
#     return [i for i in comments["comments"] if i["news_id"] == id]
#
#
# @app.get("/")
# async def get_news():
#     news = await load_data("news.json")
#     comments = await load_data("comments.json")
#     data = {"news": []}
#
#     for news_item in news["news"]:
#         if not news_item["deleted"]:
#             news_item_comments = await get_news_comments(comments, news_item["id"])
#             news_item["comments_count"] = len(news_item_comments)
#             data["news"].append(news_item)
#
#     data["news_count"] = len(data["news"])
#     return data
#
#
# @app.get("/news/{id}")
# async def get_news_item(id: int):
#     news = await load_data("news.json")
#     comments = await load_data("comments.json")
#
#     for news_item in news["news"]:
#         if news_item["id"] == id and not news_item["deleted"]:
#             comments = await get_news_comments(comments, id)
#             news_item["comments"] = comments
#             news_item["comments_count"] = len(comments)
#             return news_item
#
#     return HTTPException(status_code=404, detail="News not found")
