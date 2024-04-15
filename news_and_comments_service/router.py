from fastapi import APIRouter, HTTPException
from .utils import load_data, get_news_comments


router = APIRouter()


@router.get("/")
async def get_news():
    news = await load_data("news.json")
    comments = await load_data("comments.json")
    data = {"news": []}

    for news_item in news["news"]:
        if not news_item["deleted"]:
            news_item_comments = await get_news_comments(comments, news_item["id"])
            news_item["comments_count"] = len(news_item_comments)
            data["news"].append(news_item)

    data["news_count"] = len(data["news"])
    return data


@router.get("/news/{id}")
async def get_news_item(id: int):
    news = await load_data("news.json")
    comments = await load_data("comments.json")

    for news_item in news["news"]:
        if news_item["id"] == id and not news_item["deleted"]:
            comments = await get_news_comments(comments, id)
            news_item["comments"] = comments
            news_item["comments_count"] = len(comments)
            return news_item

    return HTTPException(status_code=404, detail="News not found")