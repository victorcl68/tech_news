from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    news_list = []
    for each_news in news:
        title_tuple = each_news["title"]
        url_tuple = each_news["url"]
        news_list.append((title_tuple, url_tuple))

    return news_list


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    # https://qastack.com.br/programming/16870663/how-do-i
    # -validate-a-date-string-format-in-python

    query = {"timestamp": {"$regex": date}}
    news = search_news(query)
    news_list = []
    for each_news in news:
        title_tuple = each_news["title"]
        url_tuple = each_news["url"]
        news_list.append((title_tuple, url_tuple))

    return news_list


# Requisito 8
def search_by_source(source):
    query = {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
    news = search_news(query)
    news_list = []
    for each_news in news:
        title_tuple = each_news["title"]
        url_tuple = each_news["url"]
        news_list.append((title_tuple, url_tuple))

    return news_list


# Requisito 9
def search_by_category(category):
    query = {
        "categories": {"$elemMatch": {"$regex": category, "$options": "i"}}
    }
    news = search_news(query)
    news_list = []
    for each_news in news:
        title_tuple = each_news["title"]
        url_tuple = each_news["url"]
        news_list.append((title_tuple, url_tuple))

    return news_list
