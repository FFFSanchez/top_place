from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Page, Paginator
from django.db.models.query import QuerySet

ITEMS_PER_PAGE = 3


def pag(request: WSGIRequest, article_list: QuerySet) -> Page:
    """Функция для пагинации страниц"""
    paginator = Paginator(article_list, ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
