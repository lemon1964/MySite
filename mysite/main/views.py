from django.shortcuts import get_object_or_404, render
from .models import PostMain
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostMainForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def logo(request):
    return render(request, 'main/logo.html')


class PostsMain(ListView):
    template_name = 'main/index.html'
    context_object_name = 'posts'
    title_page = 'Главная страница сайта'
    queryset = PostMain.objects.all()


class AddPostMain(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = PostMainForm
    template_name = 'main/addpost.html'
    title_page = 'Добавление статьи'
    permission_required = 'posts.add_post' # <приложение>.<действие>_<таблица>

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)
    
class ShowPostMain(DetailView):
    template_name = 'main/post_main.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(PostMain.objects, slug=self.kwargs[self.slug_url_kwarg])

