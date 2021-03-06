from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()

    news.sort(
        key=lambda x: x["shares_count"] + x["comments_count"], reverse=True
    )
    # https://www.w3schools.com/python/ref_list_sort.asp

    top_5_news_list = news[:5]

    news_list = []
    for each_news in top_5_news_list:
        title_tuple = each_news["title"]
        url_tuple = each_news["url"]
        news_list.append((title_tuple, url_tuple))

    return news_list


# Requisito 11
def top_5_categories():
    categories_list = find_news()

    categories_list.sort(key=lambda x: x["title"])

    top_5_categories_list = []
    for category in categories_list:
        top_5_categories_list += category["categories"]

    top_5_categories_list.sort()

    return top_5_categories_list[:5]
