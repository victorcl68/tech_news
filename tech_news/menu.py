import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


# Requisito 12
def analyzer_menu():
    first_input = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.\n"""
    )

    second_options_dict = {
        0: "Digite quantas notícias serão buscadas:",
        1: "Digite o título:",
        2: "Digite a data no formato aaaa-mm-dd:",
        3: "Digite a fonte:",
        4: "Digite a categoria:",
    }

    final_options_dict = {
        0: lambda: get_tech_news(int(second_input)),
        1: lambda: search_by_title(second_input),
        2: lambda: search_by_date(second_input),
        3: lambda: search_by_source(second_input),
        4: lambda: search_by_category(second_input),
        5: lambda: top_5_news(),
        6: lambda: top_5_categories(),
        7: lambda: print("Encerrando script\n"),
    }

    if first_input.isdigit() is False or int(first_input) not in range(0, 8):
        sys.stderr.write("Opção inválida\n")
        return False
    elif int(first_input) in range(0, 5):
        second_input = input(second_options_dict[int(first_input)])
        if first_input == "0" and second_input.isdigit() is False:
            sys.stderr.write("Opção inválida\n")
            return False

    return final_options_dict[int(first_input)]()
