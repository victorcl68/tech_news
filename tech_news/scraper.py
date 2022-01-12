import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    css_selector_string = "div.tec--list.tec--list--lg h3 > a ::attr(href)"
    return selector.css(css_selector_string).getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    css_string = "div.tec--list.tec--list--lg > a ::attr(href)"
    return selector.css(css_string).get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    notice_dict = dict()
    only_numbers_regex = "[0-9]+"

    url_css = "link[rel=canonical] ::attr(href)"
    notice_dict["url"] = selector.css(url_css).get()

    title_css = "#js-article-title ::text"
    notice_dict["title"] = selector.css(title_css).get()

    timestamp_css = "#js-article-date ::attr(datetime)"
    notice_dict["timestamp"] = selector.css(timestamp_css).get()

    comments_css = "#js-comments-btn ::text"
    comment_selector = selector.css(comments_css).re_first(only_numbers_regex)
    notice_dict["comments_count"] = (
        int(comment_selector) if (comment_selector) is not None else 0
    )

    summary_css = "div.tec--article__body > p:nth-child(1) ::text"
    summary_selector = selector.css(summary_css).getall()
    notice_dict["summary"] = "".join(summary_selector).strip()

    shares_css = "#js-author-bar > nav > div.tec--toolbar__item ::text"
    shares_selector = selector.css(shares_css).re(only_numbers_regex)
    if len(shares_selector) > 1:
        shares_count = int(shares_selector[0])
    else:
        shares_count = 0

    notice_dict["shares_count"] = shares_count

    writer_css_older = (
        "#js-main > div > article > "
        + "div.tec--article__body-grid > "
        + "div.z--pt-40.z--pb-24 > div.z--flex.z--items-center > "
        + "div.tec--timestamp.tec--timestamp--lg > "
        + "div.tec--timestamp__item.z--font-bold > a ::text"
    )
    writer_css_newer = (
        "#js-author-bar > div > p.z--m-none.z--truncate.z--font-bold ::text"
    )
    writer_css_newer_selector = selector.css(writer_css_newer).getall()
    if selector.css(writer_css_older).get() is not None:
        notice_dict["writer"] = selector.css(writer_css_older).get().strip()
    else:
        notice_dict["writer"] = "".join(writer_css_newer_selector).strip()

    source_css = (
        "#js-main article > div.tec--article__body-grid >"
        + "div.z--mb-16 > div > a ::text"
    )
    sources_selector = selector.css(source_css).getall()
    sources_list = []
    for source in sources_selector:
        sources_list.append(source.strip())
    notice_dict["sources"] = sources_list

    categories_selector = selector.css(
        "#js-categories > a.tec--badge.tec--badge--primary ::text"
    ).getall()
    categories_list = []
    for category in categories_selector:
        categories_list.append(category.strip())
    notice_dict["categories"] = categories_list

    return notice_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
