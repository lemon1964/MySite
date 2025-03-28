menu = [
        {'title': "Главная", 'url_name': 'home_main'},
        {'title': "Статьи", 'url_name': 'posts:home'},
        {'title': "Курсы", 'url_name': 'course_list'},
        {'title': "Магазин", 'url_name': 'shop:product_list'},
        {'title': "Галерея", 'url_name': 'images:list'},
        {'title': "Обратная связь", 'url_name': 'posts:contact'},
        # {'title': "Все статьи", 'url_name': 'posts:about'},
        ]


class DataMixin:
    paginate_by = 5
    title_page = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
