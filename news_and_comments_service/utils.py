import json


async def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


async def get_news_comments(comments: dict, id: int) -> list:
    return [i for i in comments["comments"] if i["news_id"] == id]