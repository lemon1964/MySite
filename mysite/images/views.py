from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger
from .forms import ImageCreateForm
from .models import Image, translit_to_eng
from actions.utils import create_action
# import redis
from django.conf import settings
import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify

# # connect to redis
# r = redis.Redis(host=settings.REDIS_HOST,
#                 port=settings.REDIS_PORT,
#                 db=settings.REDIS_DB)


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            try:
                new_image = form.save(commit=False)
                # assign current user to the item
                new_image.user = request.user
                response = requests.get(cd['url'])
                response.raise_for_status()  # raise an exception if there's an HTTP error
                # download image from the given URL
                image_name = slugify(translit_to_eng(new_image.title)) + '.jpg'
                new_image.image.save(image_name, ContentFile(response.content), save=False)
                new_image.save()
                create_action(request.user, 'bookmarked image', new_image)
                messages.success(request, 'Image added successfully')
                # redirect to new created image detail view
                return redirect(new_image.get_absolute_url())
            except Exception as e:
                # handle the error
                messages.error(request, "This site does not allow downloading images for bookmarking. Please try another site.")
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    
    # Убираем использование Redis для подсчета просмотров:
    # total_views = r.incr(f'image:{image.id}:views')
    # Можно использовать обычное хранение в базе данных, если нужно подсчитать количество просмотров:
    image.total_views += 1
    image.save()

    # Убираем использование Redis для рейтинга:
    # r.zincrby('image_ranking', 1, image.id)
    # Вместо этого можно обновить рейтинг в базе данных (если это необходимо):
    image.ranking += 1
    image.save()

    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': image.total_views})
    
# def image_detail(request, id, slug):
#     image = get_object_or_404(Image, id=id, slug=slug)
#     # increment total image views by 1
#     total_views = r.incr(f'image:{image.id}:views')
#     # increment image ranking by 1
#     r.zincrby('image_ranking', 1, image.id)
#     return render(request,
#                   'images/image/detail.html',
#                   {'section': 'images',
#                    'image': image,
#                    'total_views': total_views})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # If AJAX request and page out of range
            # return an empty page
            return HttpResponse('')
        # If page out of range return last page of results
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request,
                      'images/image/list_images.html',
                      {'section': 'images',
                       'images': images})
    return render(request,
                  'images/image/list.html',
                   {'section': 'images',
                    'images': images})


@login_required
def image_ranking(request):
    # Убираем использование Redis для получения рейтинга:
    # image_ranking = r.zrange('image_ranking', 0, -1,
    #                          desc=True)[:10]
    
    # Вместо этого используем обычный запрос в базу данных для получения наиболее популярных изображений
    most_viewed = Image.objects.order_by('-total_views')[:10]

    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})
    
# @login_required
# def image_ranking(request):
#     # get image ranking dictionary
#     image_ranking = r.zrange('image_ranking', 0, -1,
#                              desc=True)[:10]
#     image_ranking_ids = [int(id) for id in image_ranking]
#     # get most viewed images
#     most_viewed = list(Image.objects.filter(
#                            id__in=image_ranking_ids))
#     most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
#     return render(request,
#                   'images/image/ranking.html',
#                   {'section': 'images',
#                    'most_viewed': most_viewed})
