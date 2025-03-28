
from mysite import settings
# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from posts.views import page_not_found, PostHome

from django.contrib.sitemaps.views import sitemap
from posts.sitemaps import PostSitemap

from courses.views import CourseListView, siteverview
from django.contrib.auth import views as auth_views

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from payment import webhooks


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # URL-адреса только на английском языке
    path("admin/", admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('goods/', CourseListView.as_view(), name='course_list'),
    path("posts/", include("posts.urls", namespace="posts")),
    path('users/', include('users.urls', namespace="users")),
    path("__debug__/", include("debug_toolbar.urls")),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('social-auth/',
         include('social_django.urls', namespace='social')),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('accounts/login/', auth_views.LoginView.as_view(),
          name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
          name='logout'),
    path('account/', include('account.urls')),
    path('images/', include('images.urls', namespace='images')),
    path('rosetta/', include('rosetta.urls')),
    path("", include("main.urls")),
    # URL-адреса магазина, обернутые в i18n_patterns
    *i18n_patterns(
        path(_('cart/'), include('cart.urls', namespace='cart')),
        path(_('orders/'), include('orders.urls', namespace='orders')),
        path(_('payment/'), include('payment.urls', namespace='payment')),
        path(_('coupons/'), include('coupons.urls', namespace='coupons')),
        path('shop/', include('shop.urls', namespace='shop')),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('accounts/profile/', 
        CourseListView.as_view(), name='profile')]
urlpatterns += [
    path('payment/webhook/', webhooks.stripe_webhook, name='stripe-webhook'),
]

handler404 = page_not_found

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Сайт"

# cd mysite

# https://mysite.com/
# docker-compose run web python mysite/manage.py migrate --noinput

# docker compose down
# docker compose up --build
# docker compose up celery_worker
# docker compose down celery_worker
# docker-compose stop celery_worker
# docker-compose start
# docker-compose restart nginx
# docker-compose restart celery_worker  daphne flower    rabbitmq
# docker rm имя/id контейнера
# docker kill c27a791e8015ca4ab58fd5073

# docker-compose exec web ls -l /code/mysite/static/
# docker-compose exec web ls -l /code/mysite/

# docker exec -it my_educa_prod-daphne /bin/bash

# python manage.py runserver --settings=mysite.settings.local
# python manage.py runserver

    # python manage.py runserver_plus --cert-file cert.crt
    # https://mysite.com:8000/  закладки не работают
    # https://127.0.0.1:8000/   закладки работают
# cd mysite

# python3 manage.py makemigrations
# python3 manage.py migrate

# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
    # docker stop name rabbitmq
    # RabbitMQ      http://localhost:15672   guest/guest     lemon/Q195375q
    
# celery -A mysite worker -l info
    # celery -A mysite flower
    # stripe login на 90 дней
# stripe listen --forward-to localhost:8000/payment/webhook/
    # stripe listen --forward-to localhost/payment/webhook/
    # stripe listen --forward-to mysite/payment/webhook/
    # stripe listen --forward-to https://mysite/payment/webhook/
# docker run -it --rm --name redis -p 6379:6379 redis

# lemon.design@mail.ru
# 4242 4242 4242 4242
# 12/29
# 123
# Джон
# Соединенные Штаты
# 100001


# user1
# user1@user.com
# 123123qweqq1

# usertestemail
# lemon.design@mail.ru
# Джон
# Смит
# 123123qweqq89644

# user_xxx
# Дюк
# Кор
# 123123qweqq89644ff


# user_it
# user_it@user.com
# 123123qweqq1hjg

# user_marketing
# user_marketing@user.com
# 123123qweqq1df


# user_history
# user_history@user.com
# 123123qweqq1


# user_music
# user_music@user.com
# 123123qweqq1ks6


# student_1
# student_1@mail.ru
# Студент
# Вечный
# 1231weqq8644

# lemon
# lemon@lemon.ru
# 12345


# writer
# writer@mail.ru
# Джек
# Лондон
# 1231w34h4q8644