from django.urls import path
from . import views
from .views import IndexView, DirectionView, PostView, SubPostView, PostViewOOP, SubPostViewOOP, PostViewAlgoritm, \
    SubPostViewAlgoritm, PostViewAsync, SubPostViewAsync

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('direction/<slug:dir_slug>/', DirectionView.as_view(), name='direction'),
    path('posts/<slug:post_slug>/', PostView.as_view(), name='posting'),
    path('posts/sub/<slug:sub_slug>/', SubPostView.as_view(), name='sub_lesson'),
    path('posts/oop/<slug:cat_oop_slug>/', PostViewOOP.as_view(), name='posting_oop'),
    path('posts/oop/sub/<slug:sub_slug>/', SubPostViewOOP.as_view(), name='sub_lesson_oop'),
    path('posts/algoritm/<slug:algoritm_slug>/', PostViewAlgoritm.as_view(), name='posting_algoritm'),
    path('posts/algoritm/sub/<slug:sub_algoritm>/', SubPostViewAlgoritm.as_view(), name='posting_sub_algoritm'),
    path('posts/async/<slug:async_slug>/', PostViewAsync.as_view(), name='posting_async'),
    path('posts/async/sub/<slug:sub_async>/', SubPostViewAsync.as_view(), name='posting_sub_async'),
]
